from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *
from funcoesclass.FormCode.FormIncluirTipodocumento import*
from funcoesclass.databese.ClassQuery import*
import time
class FormTipoDocumento(QDialog):
    def __init__(self):
        QWidget.__init__(self)

        self.ui = Ui_FormIncluirTipodocumento()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()
        #close tipo
        self.FunBotoesAltera()
        #
        self.ui.bt_incluir.clicked.connect(self.FunIncluir)
        self.tab_Tipodocumento()
        #closee
        self.ui.bt_cancelaIcluir.clicked.connect(self.funClosetela)
        #altera
        self.ui.tab_Tipodocumento.doubleClicked.connect(self.FunAltera)
        #
        self.ui.bt_cancelar_Altera.clicked.connect(self.FunBotoesAltera)
        self.ui.bt_grava_altera.clicked.connect(self.FunGravaAlFunGravaAlteracaotera)
        self.ui.tab_Tipodocumento.addAction(self.ui.actionaltera_documento)
        self.ui.actionaltera_documento.triggered.connect(self.FunAltera)
        self.ui.bt_apagar.clicked.connect(self.FunApagaTipoDoc)
    def mostra(self):
        checked_list = []
        for i in range(0,self.ui.tab_Tipodocumento.currentItem()):
       
            self.ui.tab_Tipodocumento.removeRow(i-1)
            print(i)
            
    def funClosetela(self):
        self.confirma=Mensagem.confirmacao(self,'deseja','Deseja Fechar Tela')
        if self.confirma:
            self.close()
    def FunIncluir(self):
        codigo=str(self.ui.tx_codigo.text())
        descricao=self.ui.tx_descricao.text()
        self.confirma=Mensagem.confirmacao(self,"Deseja","deseja Cadastra Tipo Documento")
        if self.confirma:
            pegada=db.pega_dados(f'''select codigo from tb_tipodocumento where codigo='{codigo}' ''')
            
            if pegada:
                Mensagem.mensagem(self,'tipo documento',' tipo documento ja existe')
            else:
                db.adicionar(f'''insert into tb_tipodocumento (codigo,descricao)values ('{codigo}','{descricao}') ''')
                self.tab_Tipodocumento()
                self.ClearLine()
    def tab_Tipodocumento(self):
        banco=db.pega_dados('''select * from tb_tipodocumento ''')
        self.ui.tab_Tipodocumento.setRowCount(0)
        for linha,row in enumerate(banco):
            self.ui.tab_Tipodocumento.insertRow(linha)
            self.ui.tab_Tipodocumento.setItem(linha, 0, QTableWidgetItem(str(row[1])))#codigo
            self.ui.tab_Tipodocumento.setItem(linha, 1, QTableWidgetItem(str(row[2])))#descriçao
    def FunApagaTipoDoc(self):
        try:
            seleciona=self.ui.tab_Tipodocumento.selectedItems()[0].text()
            self.confirma=Mensagem.confirmacao(self,'Apagar','Deseja Apagar Tipo Documento')
            if self.confirma:
                db.apaga(f'''delete from tb_tipodocumento  where codigo='{seleciona}' ''')
                self.tab_Tipodocumento()
        except:error
    def FunAltera(self):
        try:
            seleciona=self.ui.tab_Tipodocumento.selectedItems()
            self.ui.tx_codigo.setText(seleciona[0].text())
            self.ui.tx_descricao.setText(seleciona[1].text())
            
            self.FunBotoesAltera('True')
        
        except:error
    def FunGravaAlFunGravaAlteracaotera(self,codigoid=None):
        
        codigo=self.ui.tx_codigo.text()
        descricao=self.ui.tx_descricao.text()
        self.confirma=Mensagem.confirmacao(self,'Deseja','Deseja alterar')
        if self.confirma:
            
            db.adicionar(f''' update tb_tipodocumento set codigo='{codigo}',
                         descricao='{descricao}' where codigo='{codigo}' ''')
            self.ClearLine()
            self.tab_Tipodocumento()
            self.FunBotoesAltera()
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
            self.ClearLine() 
    def ClearLine(self):
        self.ui.tx_codigo.clear()
        self.ui.tx_descricao.clear()
        