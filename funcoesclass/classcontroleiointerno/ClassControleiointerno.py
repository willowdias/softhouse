from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.databese.ClassQuery import*

import datetime
from funcoesclass.classestoque.ClassFormControleioEstoque import*
from funcoesclass.FormCode.FormControleioInterno import*
from funcoesclass.classcontroleiointerno.classfinalzarvenda import*
class ControleioVendas(QDialog):#essa tela puxa os quarto
    def __init__(self):
        QWidget.__init__(self)
      
        self.ui = Ui_FormControleioInterno()
        self.ui.setupUi(self)
        #coluna table itens
        self.ui.tb_Itens.setColumnWidth(0, 160)#codigo barra
        self.ui.tb_Itens.setColumnWidth(1, 500)
        self.ui.tb_Itens.setColumnWidth(2, 135)
        self.ui.tb_Itens.setColumnWidth(3, 135)
        self.ui.tb_Itens.setColumnWidth(4, 135)
        self.ui.tb_Itens.setColumnWidth(5, 60)
        
        #INSERIR PRODUTO
        self.ui.tx_BuscaItem_2.returnPressed.connect(self.FunInserirItens)
        self.ui.db_Quantidade.editingFinished.connect(lambda:self.ui.tx_BuscaItem_2.setFocus())
        #finaliza vendqa
        self.ui.bt_finalizar.clicked.connect(self.FinalizarVenda)
        
    def FinalizarVenda(self):
        linha=(self.ui.tb_Itens.rowCount())
        if linha==0:
            pass
        else:
            FinalizaVenda(self.ui.db_ValorTotalvenda.value()).exec_()  
    def FunInserirItens(self):
        self.descricao=str(self.ui.tx_BuscaItem_2.text())
        self.quantidadeItem=self.ui.db_Quantidade.value()
      
        banco=db.pega_dados(f'''SELECT * FROM tb_estoque where codigo_barra='{self.descricao}' or descricao='{self.descricao}' ''')
        
        if not banco:
         
            #Mensagem.mensagem_erro(self,"PRODUTO","PRODUTO NAO CONTEM CADASTRO")
          
            self.ChamaEstoque=FormControleioEstoque('S')
   
            self.ChamaEstoque.ui.frameFoto.close()
            self.ChamaEstoque.ui.frame_edita.show()
            def SelecionarPRodutoEstoque():#essa opçao consulta item quando nao acha banco
                try:
                    selecionar=self.ChamaEstoque.ui.Tab_Estoque.selectedItems()[0].text()
                    self.ui.tx_BuscaItem_2.setText(str(selecionar))
                    self.ChamaEstoque.close()
                except:error
            self.ChamaEstoque.ui.Tab_Estoque.doubleClicked.connect(SelecionarPRodutoEstoque)
            self.ChamaEstoque.ui.bt_novo_procuto.close()
            self.ChamaEstoque.setModal(True)
            self.ChamaEstoque.exec_()
        else:
            
            row = self.ui.tb_Itens.rowCount()
            self.ui.tb_Itens.insertRow(self.ui.tb_Itens.rowCount())
            
            item = QTableWidgetItem(str(banco[0][1]))
            item2=QTableWidgetItem(str(banco[0][2]))
            text_color = QColor(85, 170, 255)
        
            item.setForeground(text_color)

            
            self.ui.tb_Itens.setItem(row, 0, item)#codigo barra
            self.ui.tb_Itens.setItem(row, 1, item2)#DES
            self.ui.tb_Itens.setItem(row,2, QTableWidgetItem(str(self.quantidadeItem)))#quantidade
            self.ui.tb_Itens.setItem(row,3, QTableWidgetItem(str(("R$ {:.2f}".format(banco[0][8])))))#valor UNITARIO
            valorTotal=(self.quantidadeItem*float(banco[0][8]))
            self.ui.tb_Itens.setItem(row,4, QTableWidgetItem(str(("R$ {:.2f}".format(valorTotal)))))#valor TOTAL
            
            self.ui.tb_Itens.setItem(row,5, QTableWidgetItem(str(banco[0][3])))#TIPO UNITARIO
            #cleaR
            self.ui.tx_BuscaItem_2.clear()#limpar campo
            self.ui.db_Quantidade.setValue(1)
            self.SomarColunaTabe()
            self.order()    
    def order(self):
        time.sleep(0.1)
        #self.ui.Quantidadetela.setText(f'Qt item: {str(self.ui.tb_Itens.rowCount())}')
        self.ui.tb_Itens.selectRow(self.ui.tb_Itens.rowCount()-1)
    
    def SomarColunaTabe(self):
        venda=[]
        quantidade=[]
        for i in range(self.ui.tb_Itens.rowCount()):
           
            venda.append(str(self.ui.tb_Itens.item(i, 4).text()).replace('R','').replace('$',''))
            quantidade.append(str(self.ui.tb_Itens.item(i, 2).text()).replace('R','').replace('$',''))
          
        valor=0
        for vendas in venda:
            valor += float(vendas) 
            self.ui.db_ValorTotalvenda.setValue(valor)
        qnt=0
        for quant in quantidade:
     
            qnt += float(quant)
            self.ui.tx_quantidadeitem.setText(str(qnt)) 
           
        linha=(self.ui.tb_Itens.rowCount())
        if linha==0:#remove coluna
            self.ui.db_ValorTotalvenda.setValue(0)
            self.ui.tx_quantidadeitem.setText(str('0,00')) 