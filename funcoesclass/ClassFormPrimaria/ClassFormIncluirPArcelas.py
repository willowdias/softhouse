from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.FormCode.FormIncluirParcela import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
from funcoesclass.databese.ClassQuery import*
class FormIncluirParcelas(QDialog):
    def __init__(self):
        QWidget.__init__(self)

        self.ui = Ui_FormIncluirParcelas()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()
        self.ui.bt_cancelaIcluir.clicked.connect(self.CloseTela)
        #ADICIONAR PARCELAS 
        self.ui.bt_incluir.clicked.connect(self.FunIncuirParcela)
        #valida apen numero 
        self.ui.tx_QuantidaPArcela.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.ui.tx_dia.setValidator(QDoubleValidator(0.99, 99.99, 2))
        #add action
        self.ui.tab_PArcelas.addAction(self.ui.actionaltera)
        self.ui.tab_PArcelas.doubleClicked.connect(self.SelecionaPlanoAltera)
        #carrega planos
        self.FuncarregaPlano()
        self.FunBotoesAltera()
        #botao cancela
        self.ui.bt_cancelar_Altera.clicked.connect(self.FunBotoesAltera)
        #pega ultimo codigo
        self.PEgaNumerobanco()
        #cacullar parcelas
        self.ui.tx_QuantidaPArcela.editingFinished.connect(self.Somarvaloresparcelas)
    def Somarvaloresparcelas(self):
        numeroparcela=int(self.ui.tx_QuantidaPArcela.text())*30
        self.ui.tx_dia.setText(str(numeroparcela))
    def CloseTela(self):
        self.fechar=Mensagem.confirmacao(self,"fechar","Deseja Fechar Tela?")
        if self.fechar:
            self.close()

    def FunIncuirParcela(self):
        
        codigo=self.ui.tx_codigo.text()
        descricao=self.ui.tx_descricao.text().upper()
        quantParcela=self.ui.tx_QuantidaPArcela.text()
        Dia=self.ui.tx_dia.text()
        resultado = db.pega_dados(f'''SELECT codigo FROM tb_planopagamento WHERE codigo ='{codigo}' ''')
        if codigo=="" or descricao==''or quantParcela=='':
            Mensagem.mensagem(self,"Atençao","CAMPOS EM BRANCO")
        elif len(resultado):  #Verifica se o retorno contém alguma linha
            Mensagem.mensagem(self,"Atençao","Codigo Parcela Ja Existe")
        else:
            self.Adicionar=Mensagem.confirmacao(self,"Deseja","deseja incluir novo plano Pagamento")
            
            if self.Adicionar:
                db.adicionar(f''' INSERT INTO tb_planopagamento (codigo,descricao,Quantidade_parcelas,dias)
                values ('{codigo}','{descricao}','{quantParcela}','{Dia}') ''')
                self.FuncarregaPlano()
                self.FunLimparaLineDite()
                self.PEgaNumerobanco()
    def PEgaNumerobanco(self):
        pegacodigo=db.pega_dados(""" select codigo FROM tb_planopagamento ORDER BY codigo DESC LIMIT 1""") 
        numero=int(pegacodigo[0][0])+1
        self.ui.tx_codigo.setText(f'{str(numero)}')
    def FunAlteraPlano(self):
        pass
    def SelecionaPlanoAltera(self):
        try:
            lista=[]
            for i in range(0,4):
                seleciona=self.ui.tab_PArcelas.selectedItems()[i].text()
                lista.append(seleciona)
            self.ui.tx_codigo.setText(str(lista[0]))
            self.ui.tx_descricao.setText(str(lista[1]))
            self.ui.tx_QuantidaPArcela.setText(str(lista[2]))
            self.ui.tx_dia.setText(str(lista[3]))
            self.FunBotoesAltera('True')
        except:error

    def FunBotoesAltera(self,botao=None):
        
        if botao=="True":
            self.ui.bt_grava_altera.show()
            self.ui.bt_cancelar_Altera.show()
            self.ui.bt_incluir.close()
            self.ui.bt_cancelaIcluir.close()
            
        else:
            self.ui.bt_grava_altera.close()
            self.ui.bt_cancelar_Altera.close()
            self.ui.bt_incluir.show()
            self.ui.bt_cancelaIcluir.show()
            self.FunLimparaLineDite()
            self.PEgaNumerobanco()
    def FuncarregaPlano(self):
        dados=db.pega_dados('SELECT *FROM tb_planopagamento')
        
        self.ui.tab_PArcelas.setRowCount(0)
        for linha, row_data in enumerate (dados): 
            self.ui.tab_PArcelas.insertRow(linha)
            self.ui.tab_PArcelas.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(row_data[1])))
            self.ui.tab_PArcelas.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(row_data[2])))
            self.ui.tab_PArcelas.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(row_data[3])))
            self.ui.tab_PArcelas.setItem(linha, 3, QtWidgets.QTableWidgetItem(str(row_data[4])))
        
        for lin in range(0,len(dados)):
            for i in range(0,4):
                self.ui.tab_PArcelas.item(lin,i).setTextAlignment(Qt.AlignCenter)
            
      
                
    def FunLimparaLineDite(self):#limpar os campo
        self.ui.tx_codigo.clear()
        self.ui.tx_descricao.clear()
        self.ui.tx_QuantidaPArcela.clear()
        self.ui.tx_dia.clear()