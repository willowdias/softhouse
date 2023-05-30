
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.FormCode.FormAlteraQuantidade import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
class AlteraQuantProduto(QDialog):#analise venda
    def __init__(self,):
        QWidget.__init__(self)
      
        self.ui = Ui_FormAlteraQuantidade()
        self.ui.setupUi(self)
        #self.showFullScreen()
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        self.ui.db_Quant.selectAll()