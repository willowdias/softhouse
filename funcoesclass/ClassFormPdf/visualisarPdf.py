



from distutils.log import error
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from relatorio.formPdf import *
from funcoesclass.FormCode.ForMVisualisarPDf import*
import os
from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
from funcoesclass.ClassFormPdf.EnviaEmail import*
class FormVisualisarPDf(QDialog):#essa tela puxa sistema sintegra
    def __init__(self,Especie=None,Nome=None,Verifica=None):
        QWidget.__init__(self)
        self.ui = Ui_form_pdf_gerado()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowFlags(Qt.Drawer|Qt.WindowStaysOnTopHint)
        self.statusBar = QStatusBar()
        
        filename=f'{os.getcwd()}/config/pdf/{Verifica}.pdf'
        settings = self.ui.web_browser.settings()
        settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        url = QtCore.QUrl.fromLocalFile(filename)
        self.ui.web_browser.load(url)

        self.ui.lb_receberNome.setText(f'{Especie}:{Nome}')
        #boTAO FECHAR
        self.mensagem=Mensagem()
        #framse
        self.ui.bt_enviaEmail.clicked.connect(self.FunMostraFrameEmail)
        self.ui.bt_enviaEmail.setCheckable(True)
        self.ui.bt_cancelarEnvio.clicked.connect(self.stop)
        #envia email
        self.ui.bt_envia_email.clicked.connect(self.EnviaEmail)
        self.caminhoPdf=filename
        
    def EnviaEmail(self):
        emailDestinatatio=self.ui.tx_email.text()
        assunto=self.ui.tx_assunto.text()
        if emailDestinatatio=="" or assunto=="":
            pass
        else:
            
            Email(self.ui.lb_EmailEnviado)
            Email.EnviaEmail(self,emailDestinatatio,assunto,self.caminhoPdf)
    def FunMostraFrameEmail(self,botao):
        
        
       
        if botao:
            self.ui.frame_email.setFixedHeight(350)
            self.ui.frame_email.setFixedWidth(700)
            self.ui.frame_email.show()
            self.animation = QtCore.QPropertyAnimation(self.ui.frame_email, b"geometry")
            self.animation.setDuration(3000)
            
            self.animation.setStartValue(QRect(145,self.ui.frame_2.x(),100,100))
            self.animation.setEndValue(QRect(15,80,500,500))
            self.animation.start()
            
    def stop(self):
        self.ui.frame_email.close()
        self.animation.stop()                
            
            



    