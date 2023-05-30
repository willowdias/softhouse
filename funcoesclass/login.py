
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QLabel, QDialog
from PyQt5 import QtWidgets, QtCore, QtPrintSupport, QtGui
import os
from funcoesclass.databese.ClassQuery import*
from funcoesclass.FormCode.FormTelaLogin import*
import time
from assets.file import*
from funcoesclass.main import*
from funcoesclass.ClassLiberauser.Classpermissoesusuario import*
import json
class Telalogin(QDialog):
    def __init__(self,logoff=None):
        QWidget.__init__(self)
        self.ui = Ui_FormTelalogin()
        self.ui.setupUi(self)
          
        '''check = self.isActiveWindow() 
        print(check'''
        #verifca objet
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
   
        self.ui.widget.move(self.mapToGlobal(self.rect().center() - self.ui.widget.rect().center()))
        
        self.ui.tx_senha.addAction(self.ui.actionsenha, QLineEdit.TrailingPosition)
        self.ui.actionsenha.triggered.connect(self.visualisarsenha)
        self.ui.bt_canelar.clicked.connect(self.close)
        self.logoff=logoff
   
        self.ui.bt_logar.clicked.connect(self.logaSistema)
        self.tentativas = 0
        self.max_tentativas = 5
    def logaSistema(self):
        login=self.ui.tx_login.text()
        senha= self.ui.tx_senha.text()
        logado=db.pega_dados(f'''select * from usuario where nome='{login}' and senha='{senha}'  ''')
       
        if logado:
            self.ui.lb_log.setText('Logado')
            self.ui.lb_log.repaint()
            time.sleep(1)
            self.ui.lb_log.setText('')
            '''self.inicial=telaincial(Telalogin())
            self.inicial.ui.centralwidget.setDisabled(False)
            self.hide()'''
            
            self.Verificaruser(login)
            self.accept()
            
        else:
            self.tentativas += 1
            if self.tentativas==4:
                Mensagem.mensagem(None,'Login',"ultima tentativa Erro sera desconnectador")
            if self.tentativas >= self.max_tentativas:
                Mensagem.mensagem(None,'Login',"Sistema sendo fechado")
                self.close()
            self.ui.lb_log.setText("Usuario senha incorreto")
            self.ui.lb_log.repaint()
            time.sleep(1)
            self.ui.lb_log.setText('')
    
    def visualisarsenha(self):
        ver=self.sender()
        if ver.isChecked()==True:
            self.ui.tx_senha.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.tx_senha.setEchoMode(QLineEdit.Password)
    def Verificaruser(self,login):
        if self.logoff=="relogar":
            self.inicial=telaincial(Telalogin,login).hide()
            self.hide()
        else:
            self.inicial=telaincial(Telalogin,login).showMaximized()
            self.hide()
           