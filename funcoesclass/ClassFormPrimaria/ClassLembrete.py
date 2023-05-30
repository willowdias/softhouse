from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *
from funcoesclass.databese.ClassQuery import*
from funcoesclass.FormCode.FormLembreteal import*
class Formlembrete(QDialog):
    def __init__(self,atualiza=None,id=None):
        QWidget.__init__(self)

        self.ui = Ui_FormLembrete()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        #self.setWindowFlags(Qt.Tool)
        self.ui.bt_altera.close()
        self.showFullScreen()
        self.atualizar=atualiza
        self.ui.salva.clicked.connect(self.salvarLembrete)
        self.ui.cancelar.clicked.connect(self.close)
        #seleciona core
        self.ui.amarela.clicked.connect(self.selecioncore)
        self.ui.azul.clicked.connect(self.selecioncore)
        self.ui.laranja.clicked.connect(self.selecioncore)
        self.ui.preto.clicked.connect(self.selecioncore)
        self.ui.verde.clicked.connect(self.selecioncore)
        self.ui.vermelho.clicked.connect(self.selecioncore)
        print(id)
        if id==None:
            self.ui.plainTextEdit.clear()
            self.ui.lb_corest.setText(str('#FFFF00')) 
        else:
            self.ui.salva.close()
            self.ui.bt_altera.show()
            banco=db.pega_dados(f'''select *from lembrete where id='{id}' ''')
            self.ui.plainTextEdit.setPlainText(str(banco[0][1]))
            self.ui.lb_corest.setText(str(banco[0][2]).upper())
        self.ui.bt_altera.clicked.connect(lambda:self.AlteraLembrete(id))
    def selecioncore(self):
        core=self.sender()
        seleciona=str(core.text()).lower()
        self.listacore=['#FFFF00','#0000FF','#FF4500','#000000','#00FF00','#ff0000']   
        if seleciona=='amarelo':
            cores=self.listacore[0]
        if seleciona=='azul':
           cores=self.listacore[1]
        if seleciona=='laranja':
            cores=self.listacore[2]
        if seleciona=='preto':
            cores=self.listacore[3]
        if seleciona=='verde':
            cores=self.listacore[4]
        if seleciona=='vermelho':
            cores=self.listacore[5]
        self.ui.lb_corest.setText(str(cores)) 
    def salvarLembrete(self):
        tex=self.ui.plainTextEdit.toPlainText()
        cores=self.ui.lb_corest.text()
        self.confirma = Mensagem.confirmacao(None,"LEmbrete",'Deseja salvar')
        
        if self.confirma:
            if tex==''or cores=='':
                pass
            else:
                db.adicionar(f''' insert into lembrete (text,cores)values('{tex}','{cores}') ''')
                self.ui.plainTextEdit.clear()
                self.ui.lb_corest.clear()
                self.atualizar()
                self.close()
    def AlteraLembrete(self,id):
        tex=self.ui.plainTextEdit.toPlainText()
        cores=self.ui.lb_corest.text()
        self.confirma = Mensagem.confirmacao(None,"LEmbrete",'Deseja alterar')
        
        if self.confirma:
            if tex==''or cores=='':
                pass
            else:
                db.update(f''' update lembrete set  text='{tex}',cores='{cores}' where id='{id}' ''')
                self.ui.plainTextEdit.clear()
                self.ui.lb_corest.clear()
                self.atualizar()
                self.close()