
from distutils.log import error
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from relatorio.formPdf import *
from funcoesclass.FormCode.ForMVisualisarPDf import*
import os
from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
from funcoesclass.ClassFormPdf.EnviaEmail import*
class relatorioestoque(QDialog):#essa tela puxa sistema sintegra
    def __init__(self,nomepdf=None):
        QWidget.__init__(self)
        self.ui = Ui_form_pdf_gerado()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowFlags(Qt.Drawer|Qt.WindowStaysOnTopHint)

        filename=f'{os.getcwd()}/config/relatorioestoque/{nomepdf}.pdf'
        self.ui.web_browser.page().profile().setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.129 Safari/537.36")

        settings =self.ui.web_browser.settings()
        settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        url = QtCore.QUrl.fromLocalFile(filename)
        self.ui.web_browser.load(url)

       