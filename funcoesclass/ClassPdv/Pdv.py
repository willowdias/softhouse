from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *#IMPORA MENSAGEM BOX
from funcoesclass.ClassPdv.ClassVenda import *
from funcoesclass.FormCode.MAINPDV import*
from funcoesclass.databese.ClassQuery import*
from funcoesclass.ClassPdv.relatoriopdv.imprimir import*
from funcoesclass.ClassPdv.relatoriopdv.rl_itemvenda import*

#importa table cliente
from  funcoesclass.ClassFormPrimaria.ClassFormControleioClientes import*
from  funcoesclass.classestoque.ClassFormBuscarProduto import*
from datetime import datetime
import time
data=datetime.today().strftime("%d/%m/%Y").capitalize()
#from impor finalizavenda
from  funcoesclass.ClassPdv.ClassFormFinalizarVenda import*
#tela orcamentos
from  funcoesclass.ClassPdv.ClassvisualisarOrcamento import*
import json
#import nfce cupom
from funcoesclass.ClassPdv.relatoriopdv.rl_nfce import *
#abri caixa
from  funcoesclass.ClassPdv.classAberturaCaixaPdv import*
#from ClassFormSegundaria.ClassQuantidaVenda import*
from  funcoesclass.ClassFormSegundaria.ClassQuantidaVenda import*
from PyQt5.QtGui import QColor
import pywhatkit as kt
import os
import time

class PdvVenda(QDialog):
    instances = []
    def __init__(self,codigovendedor=None,nomevendedor=None):
        self.__class__.instances.append(self)
        QWidget.__init__(self)
        
        self.ui = Ui_PDV()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showMaximized()
        self.ui.tx_BuscaItem_2.setFocus()
       
            
        #coluna table itens
        self.ui.tb_Itens.setColumnWidth(0, 160)#codigo barra
        self.ui.tb_Itens.setColumnWidth(1, 500)
        self.ui.tb_Itens.setColumnWidth(2, 135)
        self.ui.tb_Itens.setColumnWidth(3, 135)
        self.ui.tb_Itens.setColumnWidth(4, 135)
        self.ui.tb_Itens.setColumnWidth(5, 80)
        #chama menu ajuda
        self.ui.bt_ajuda.clicked.connect(self.FunmenuAjuda)
        #digita codigo
        self.ui.tx_codigoCliente.setValidator(QDoubleValidator(0.99, 999999.999999, 2))
        #codigo nome vendedor
        self.ui.tx_codigovendedor.setText(str(codigovendedor))
        self.ui.tx_NomeVendedor.setText(str(nomevendedor))
        #close sistema
        self.ui.bt_cancelar.clicked.connect(self.CloseSistema)
        #inserir item venda
        self.ui.tx_BuscaItem_2.returnPressed.connect(self.FunInserirItens)
        self.ui.db_Quantidade.editingFinished.connect(lambda:self.ui.tx_BuscaItem_2.setFocus())
        #remove item
        self.shortcut = QShortcut(QKeySequence("-"), self)
        self.shortcut.activated.connect(self.Excluiritemvenda)
        #edita item
        self.ui.tb_Itens.doubleClicked.connect(self.editaQuantidade)
        #selecionar cliente
        self.ui.tx_codigoCliente.mouseDoubleClickEvent=self.FunSelecionarClientes
        self.ui.tx_codigoCliente.addAction(self.ui.actionChamaCliente)
        self.ui.actionChamaCliente.triggered.connect(self.FunSelecionarClientes)
        #add aciotn produto
        self.ui.tx_BuscaItem_2.addAction(self.ui.actionBUSCA_PRODUTO, QLineEdit.TrailingPosition)
        self.ui.actionBUSCA_PRODUTO.triggered.connect(self.BuscarProduto)

        #salva orçamento
        self.ui.bt_SalvaORcas.clicked.connect(self.SalvarOrcamento)
        #finalizar Venda
        self.ui.bt_finalizar.clicked.connect(self.FinalizarVenda)
        self.ui.bt_imprimir.clicked.connect(self.imprimiritemgrade)
        #abrir orçamento
        self.ui.bt_orca.clicked.connect(self.AbrirOrcamento)
        self.ordertype=Qt.DescendingOrder#descricao
        #verifica caixa esta aberto
        with open("config/caixa.json", encoding='utf-8') as meu_json:
            dados = json.load(meu_json)
        obs=[dados.get('caixa')]#aqui abrer aqurivo

        if obs[0]=='fechado':
            self.ui.Lb_caixaOcupado.setText("Caixa Fechado")
            self.ui.frame_3.setDisabled(True)
            self.timer = QtCore.QTimer(self, interval=20)
            self.timer.timeout.connect(self.FunDataHora) 
            self.timer.stop()
            self.FunmenuAjuda()
           
        else:
            self.ui.frame_3.setDisabled(False)
            self.timer = QtCore.QTimer(self, interval=20)
            self.timer.timeout.connect(self.FunDataHora) 
            self.timer.start()
           
        self.ui.bt_Abricaixa.clicked.connect(self.AbrirCaixa)  

    def FinalizarVenda(self):
            
            linha=(self.ui.tb_Itens.rowCount())
            if linha==0:
                pass
            else:
                valorTotalVenda=self.ui.db_ValorTotalvenda.value()
                CodCliente=self.ui.tx_codigoCliente.text()
                NomeCliente=self.ui.tx_nomeCliente.text()
                data=self.ui.tx_data.text()
                hora=self.ui.tx_Horas.text()
                self.FinalizaVenda=FinalizaVenda(valorTotalVenda,
                CodCliente,NomeCliente,data,hora,
                self.InserirPRodutoORca,self.LimparVenda,self.ui.tx_pedidonumb,self.imprimirnfce)
                self.FinalizaVenda.setModal(True)
               
                self.FinalizaVenda.exec_()

    def InserirPRodutoORca(self,nota):
        self.nota=nota
        linha=(self.ui.tb_Itens.rowCount())
        if linha==0:
            Mensagem.mensagem_erro(self,"erro","nao pode Finalizar venda  Sem itens na grade")
            
        else:
           
            for i in range(self.ui.tb_Itens.rowCount()):
                    
                codigobara=(self.ui.tb_Itens.item(i, 0).text())
                decricao=(self.ui.tb_Itens.item(i, 1).text())
                qnt=(self.ui.tb_Itens.item(i, 2).text())    
                valorunid=(self.ui.tb_Itens.item(i, 3).text()).replace('R','').replace('$','')
                valortotal=(self.ui.tb_Itens.item(i, 4).text()).replace('R','').replace('$','')
                unidade=(self.ui.tb_Itens.item(i, 5).text())
                db.adicionar(f''' INSERT INTO orca (nota,cod_barra,descricao,quantidade,valor_unit,
                valortotal,data_emissao,hora,unidade)values('{nota}','{codigobara}',
                '{decricao}','{qnt}',{valorunid},'{valortotal}',
                '{self.ui.tx_data.text()}','{self.ui.tx_Horas.text()}','{unidade}')''') 
                    
            self.LimparVenda()
            
    def imprimiritemgrade(self):
        try:
        
            relatorioitem(self.ui.tb_Itens,self.ui.db_ValorTotalvenda.value(),self.ui.tx_data.text())
            self.FormVisualisarPDf=relatoriopdv('itemvenda')
            self.FormVisualisarPDf.setModal(True)
            self.FormVisualisarPDf.exec_()
        except:error
    def imprimirnfce(self):
        rl_nfcecupom(self.ui.tb_Itens,self.ui.db_ValorTotalvenda.value(),self.ui.tx_data.text())
        self.FormVisualisarPDf=relatoriopdv('nfce')
        self.FormVisualisarPDf.setModal(True)
        self.FormVisualisarPDf.exec_()
    def LimparVenda(self):#finalizar venda e limpar cach
        self.ui.tb_Itens.setRowCount(0)
        self.ui.db_ValorTotalvenda.setValue(0)
        self.ui.tx_quantidadeitem.clear()
        self.ui.tx_codigoCliente.setText("0")
        self.ui.lb_fotosEstoque.clear()
        self.ui.tx_DescricaoITemTab.setText("")    
        self.ui.tx_nomeCliente.setText("")   
        self.ui.tx_codigoCliente.setText("") 
    def CloseSistema(self):
        
        linha=(self.ui.tb_Itens.rowCount())
        if linha==0:
            self.closesistema=Mensagem.confirmacao(self,"Fechar","deseja Fechar Tela PDv")
            if self.closesistema:
                self.close()
        else:
            self.SalvarOrcamento()
    def AbrirOrcamento(self):
        
        self.orcamentos=FormOrcamentos()
        def SelecionaOrca():
            nota=self.orcamentos.ui.tb_orcamento.selectedItems()[0].text()
            nomeCliente=self.orcamentos.ui.tb_orcamento.selectedItems()[1].text()
            self.ui.tx_nomeCliente.setText(str(nomeCliente))
            self.ui.tx_pedidonumb.setText(str(nota))
            banco=db.pega_dados(f'''select * from orca where nota='{nota}' ''')
            self.ui.tb_Itens.setRowCount(0)
            for linha,row in enumerate(banco):
                self.ui.tb_Itens.insertRow(linha)
                self.ui.tb_Itens.setItem(linha, 0, QTableWidgetItem(str(row[2])))#codigo barra
                self.ui.tb_Itens.setItem(linha, 1, QTableWidgetItem(str(row[3])))#DES
                quantaidade=(float(row[4]))
                self.ui.tb_Itens.setItem(linha,2, QTableWidgetItem(str(quantaidade)))#quantidade
                valorTotal=(quantaidade*float(banco[0][5]))
                self.ui.tb_Itens.setItem(linha,3, QTableWidgetItem(str(("R$ {:.2f}".format(banco[0][5])))))#valor UNITARIO
                self.ui.tb_Itens.setItem(linha,4, QTableWidgetItem(str(("R$ {:.2f}".format(valorTotal)))))#valor TOTAL
                self.ui.tb_Itens.setItem(linha,5, QTableWidgetItem(str(banco[0][10])))#unidade
                self.ui.tx_data.setText(str(data))
            self.orcamentos.close()    
            

        self.orcamentos.ui.tb_orcamento.doubleClicked.connect(SelecionaOrca)    
        self.orcamentos.exec()
        self.SomarColunaTabe()
    def SalvarOrcamento(self):
        linha=(self.ui.tb_Itens.rowCount())
        if linha==0:
            pass  
        else:
            resultado = db.pega_dados(f'''SELECT nota FROM orcas WHERE nota ='{self.ui.tx_pedidonumb.text()}' ''')
            
            if len(resultado):
                db.apaga(f'''delete from orca where nota='{self.ui.tx_pedidonumb.text()}' ''')
                    
                db.adicionar(f''' update orcas set Finalizar='N' , descricao='{self.ui.tx_nomeCliente.text()}',valortotal='{self.ui.db_ValorTotalvenda.value()}',
                                 data_final={self.ui.tx_data.text()},data_final='{self.ui.tx_data.text()}'
                                 where nota='{self.ui.tx_pedidonumb.text()}' ''')
                self.InserirPRodutoORca(self.ui.tx_pedidonumb.text()) 
                self.ui.tx_pedidonumb.clear()
                
            else:
                self.confirma=Mensagem.confirmacao(self,'','Deseja Salva orçamento')
                if self.confirma:
                    banco=db.pega_dados(""" select NOTA FROM orcas ORDER BY NOTA DESC LIMIT 1""")
                    
                    try:
                        self.nota=banco[0][0]+1
                    except:
                        self.nota=1
                   
                    if self.ui.tx_nomeCliente.text()=='':
                        
                        db.adicionar(f''' insert into orcas (nota,descricao,valortotal,data_emissao,data_final,Finalizar)values
                                ('{self.nota}','{'consumidor final'}','{self.ui.db_ValorTotalvenda.value()}','{self.ui.tx_data.text()}','{self.ui.tx_data.text()}','N')  ''')   
                        self.InserirPRodutoORca(self.nota)  
                    else:
                 
                        db.adicionar(f''' insert into orcas (nota,descricao,valortotal,data_emissao,data_final,Finalizar)values
                            ('{self.nota}','{self.ui.tx_nomeCliente.text()}','{self.ui.db_ValorTotalvenda.value()}','{self.ui.tx_data.text()}','{self.ui.tx_data.text()}','N')  ''')   
                        self.InserirPRodutoORca(self.nota)  
                else:
                    self.LimparVenda()

                '''Mensagem.messagem_personalizada(
                        self,self.InserirPRodutoORca,self.ui.tx_nomeCliente.text(),
                        self.ui.db_ValorTotalvenda.value(),self.ui.tx_data.text(),self.ui.tx_pedidonumb)''' 
    def BuscarProduto(self):
        self.ChamaEstoque=Buscarproduto()
        def selecionproduto():
            Selecionaprodutos=self.ChamaEstoque.ui.Tab_Estoque.selectedItems()[0].text()
            self.ui.tx_BuscaItem_2.setText(str(Selecionaprodutos))
            self.ChamaEstoque.hide()
        self.ChamaEstoque.ui.Tab_Estoque.doubleClicked.connect(selecionproduto)
        self.ChamaEstoque.setModal(True)
        self.ChamaEstoque.exec_() 
    def FunInserirItens(self):
        self.descricao=str(self.ui.tx_BuscaItem_2.text())
        self.quantidadeItem=self.ui.db_Quantidade.value()
      
        banco=db.pega_dados(f'''SELECT * FROM tb_estoque where codigo_barra='{self.descricao}' or descricao='{self.descricao}' ''')
        
        if not banco:
         
            mensagem=Mensagem()
            mensagem.ui.lbShowMessagem.setText('''Cadastro Produto Nao Existe''')
            mensagem.exec_()
        else:
            
            row = self.ui.tb_Itens.rowCount()
            self.ui.tb_Itens.insertRow(self.ui.tb_Itens.rowCount())
            
            item = QTableWidgetItem(str(banco[0][1]))
            item2=QTableWidgetItem(str(banco[0][2]))
            text_color = QColor(85, 170, 255)
        
            item.setForeground(text_color)

            
            self.ui.tb_Itens.setItem(row, 0, item)#codigo barra
            self.ui.tb_Itens.setItem(row, 1, item2)#DES
     
            
            self.ui.tx_DescricaoITemTab.setText(str(banco[0][2]))
            self.ui.tb_Itens.setItem(row,2, QTableWidgetItem(str(self.quantidadeItem)))#quantidade
            self.ui.tb_Itens.setItem(row,3, QTableWidgetItem(str(("R$ {:.2f}".format(banco[0][8])))))#valor UNITARIO
            valorTotal=(self.quantidadeItem*float(banco[0][8]))
            self.ui.tb_Itens.setItem(row,4, QTableWidgetItem(str(("R$ {:.2f}".format(valorTotal)))))#valor TOTAL
            
            self.ui.tb_Itens.setItem(row,5, QTableWidgetItem(str(banco[0][3])))#TIPO UNITARIO
            #cleaR
            self.ui.tx_BuscaItem_2.clear()#limpar campo
            self.ui.db_Quantidade.setValue(1)
            self.SomarColunaTabe()#soma total da tabelas
            self.FunRecuperaFotoPAsta(self.descricao)
            self.order()
    
    def order(self):
        time.sleep(0.1)
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
    def Excluiritemvenda(self):
        
        #print(self.ui.tb_vendaGrupo.columnWidth(0))
        confirma=Mensagem.confirmacao(self,'Apagar','Deseja Apagar Produto Da venda')
        
        if confirma:
            linha=self.ui.tb_Itens.currentRow()
            self.ui.tb_Itens.setItem(linha,2, QTableWidgetItem(str('0')))#quantidade
            self.ui.tb_Itens.setItem(linha,3, QTableWidgetItem(str('R$ 0')))#quantidade
            self.ui.tb_Itens.setItem(linha,4, QTableWidgetItem(str('R$ 0')))#quantidade
            for column in range(0,self.ui.tb_Itens.columnCount()):
                item = self.ui.tb_Itens.item(linha, column)
                
                item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
                item.setBackground(QtGui.QColor("red"))
                item.setForeground(QtGui.QColor("white"))
                
                
            self.SomarColunaTabe()
    def editaQuantidade(self):
            self.Quantidade=AlteraQuantProduto()
            quantidade=self.ui.tb_Itens.selectedItems()[2].text()    
            self.Quantidade.ui.db_Quant.setValue(float(quantidade))
            def altera():
                troca=self.ui.tb_Itens.currentRow()
                codigobara=self.ui.tb_Itens.selectedItems()[0].text()
                dados =db.pega_dados(f"SELECT *FROM tb_estoque where codigo_barra ='{codigobara}' ")
                
                
                self.ui.tb_Itens.setItem(troca,2, QtWidgets.QTableWidgetItem(str(self.Quantidade.ui.db_Quant.value())))#quantidade
                banco=(self.Quantidade.ui.db_Quant.value()*float(dados[0][8]))
                    
                self.ui.tb_Itens.setItem(troca, 4, QtWidgets.QTableWidgetItem(str(("R$ {:.2f}".format(banco)))))#valor
            
                self.SomarColunaTabe()
                self.Quantidade.close()
            self.Quantidade.ui.db_Quant.editingFinished.connect(altera)
            
            self.Quantidade.exec_()
    def FunRecuperaFotoPAsta(self,codigobarra=None):#essa opçao pega footo da pasta coloca label
        bancoestoque=db.pega_dados(f""" SELECT * FROM tb_estoque where codigo_barra='{codigobarra}'""")
             
        recupera_imagen = f'{os.getcwd()}/config/FotosEstoque'
        for nome_arquivo in os.listdir(recupera_imagen):
            if f'{str(bancoestoque[0][0])}' in nome_arquivo:#verifica se img na pasta
                pixmap = QtGui.QPixmap(f'{os.getcwd()}/config/FotosEstoque/{nome_arquivo}') # Setup pixmap with the provided image        
                self.pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
                self.ui.lb_fotosEstoque.setPixmap( self.pixmap) # Set the pixmap onto the label
                
                self.ui.lb_fotosEstoque.setAlignment(QtCore.Qt.AlignCenter)
    def FunSelecionarClientes(self,event):#essa funçao importa cadastro cliente pra dentro da venda
        self.FormCadastroClientes=FormCadastroClientes('S')
        def SelecionaCliente():
            try:
                sel_cliente=self.FormCadastroClientes.ui.tableWidget_usuario_2.selectedItems()
                banco=db.pega_dados(f'''select * from tb_clientes where id='{sel_cliente[0].text()}' ''')
                self.ui.tx_codigoCliente.setText(str(banco[0][0]))        
                self.ui.tx_nomeCliente.setText(str(banco[0][1]))    
                self.FormCadastroClientes.hide()
                self.ui.tx_BuscaItem_2.setFocus()
            except:
                error
        self.FormCadastroClientes.ui.tableWidget_usuario_2.doubleClicked.connect(SelecionaCliente)
        self.FormCadastroClientes.ui.bt_novo.hide()
        self.FormCadastroClientes.exec_()    
    def FunDataHora(self):#essa funçao faz currente da data e hora
        self.VerificaCaixaOcupado()
        self.ui.Quantidadetela.setText(f'Qt item: {str(self.ui.tb_Itens.rowCount())}')
        #abri Caixa
        self.ui.tx_data.setText(str(data))
        time=QDateTime.currentDateTime()
        timeDisplay=time.toString('hh:mm:ss')
        self.ui.tx_Horas.setText(timeDisplay) 
        
    
    def AbrirCaixa(self):
        self.FormAberturaCaixa=FormAberturaCaixa(self.timer,self.ui.Lb_caixaOcupado,self.ui.frame_3)
        self.FormAberturaCaixa.exec_()
   
    def VerificaCaixaOcupado(self):
        linha=(self.ui.tb_Itens.rowCount())
        if linha==0:
            self.ui.Lb_caixaOcupado.setText("caixa livre")
            self.ui.topdados.setStyleSheet("""QFrame{font: 87 20pt Arial Black;background-color: rgb(15, 138, 77);color: rgb(255, 255, 255);border:none;}""")
            self.ui.lb_fotosEstoque.clear() 
            self.ui.tx_DescricaoITemTab.clear() 
        else:
            self.ui.Lb_caixaOcupado.setText("caixa ocupado")
            self.ui.topdados.setStyleSheet("QFrame{font: 87 20pt Arial Black;background-color: rgb(203, 48, 27);color: rgb(255, 255, 255);border:none;}") 
                 
    def FunmenuAjuda(self):
        Mensagem.mensagem(self,'menu ajuda',
        ' (f11) buscar clientes\n'+
         str('*'*50)+
        ' (f10) salvar orçamentos\n'+
        str('*'*50)+
        '\n (f7) visualisar orçamentos\n'+
        str('*'*50)+
        '\n (crtl+f3) configura pdv\n'+
        str('*'*50)+
        '\n (-) APAGAR item tabela\n'+
        str('*'*50)+
        '\n (f4) abrir caixa'+
        str('*'*50)+
       '\n (f9) ativa cupom eletronico' )
    
    def FunSelecionarITen(self):
        try:
            selecionar=self.ui.tb_Itens.selectedItems()[0].text()
           
        except:error

