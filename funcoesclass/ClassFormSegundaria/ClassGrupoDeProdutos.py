from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *#IMPORA MENSAGEM BOX
from funcoesclass.databese.ClassQuery import*
import time
import os
from funcoesclass.FormCode.FormGrupoProdutos import*

from funcoesclass.ClassFormSegundaria.ClassFormIncluirFornecedor import*#importa Cadastro Fornecedor
class grupodeProdutos(QDialog):
    def __init__(self):
        QWidget.__init__(self)

        self.ui = Ui_FormGrupoProdutos()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()
        #fecha tela
        #centraliza
        self.ui.widget.move(self.mapToGlobal(self.rect().center() - self.ui.widget.rect().center()))#centralizafundo
        self.ui.wb_incluirgrupo.move(self.mapToGlobal(self.rect().center() - self.ui.wb_incluirgrupo.rect().center()))#centralizafundo
        self.ui.wb_incluirgrupo.close()
        self.ui.bt_alterar.close()
        #inclurir grupo
        self.ui.bt_incluir.clicked.connect(lambda:self.ui.widget.setDisabled(True))
        self.ui.bt_incluir.clicked.connect(lambda:self.ui.wb_incluirgrupo.show())
            
        self.ui.tx_buscarGrupos.editingFinished.connect(self.buscarGrupo)
        self.ui.bt_salvar.clicked.connect(self.incluirGrupo)
        #seleciona foto
        self.ui.lb_fotos.mouseDoubleClickEvent=self.Fun_Add_foto
        self.ui.bt_sair.clicked.connect(self.CloseTelaEve)
        #close tela
        self.ui.bt_cancelar.clicked.connect(self.CloseTelaIncluir)
        ###
        self.ui.frame_7.mousePressEvent = self.mousePressEvent
        self.ui.frame_7.mouseMoveEvent = self.mouseMoveEvent
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            x = event.globalX()
            y = event.globalY()
            x_w = self.offset.x()
            y_w = self.offset.y()
            self.ui.widget.move(x - x_w, y - y_w)

    def CloseTelaIncluir(self):
        confirma=Mensagem.confirmacao(self,'fechar','Deseja Fechar')
        if confirma:
            self.ui.wb_incluirgrupo.close()
            self.ui.widget.setDisabled(False)
    def CloseTelaEve(self):
        confirma=Mensagem.confirmacao(self,'fechar','Deseja Fechar')
        if confirma:
            self.hide()
            
    def Fun_Add_foto(self,event):#adicionar foto LAbel
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", ":", "Image Files (*.png *.jpg *jpeg *.bmp);;All Files (*)") # Ask for file
        if fileName: # If the user gives a fileimagem, _ = QFileDialog.getOpenFileName(
                pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image        
                self.pixmap = pixmap.scaled(150,140, QtCore.Qt.KeepAspectRatio)
                self.ui.lb_fotos.setPixmap( self.pixmap) # Set the pixmap onto the label
                #self.ui.label_fotos_clientes.setScaledContents(True)
                self.ui.lb_fotos.setAlignment(QtCore.Qt.AlignCenter) 
    def incluirGrupo(self):
        
        descricaogrupo=self.ui.tx_Descricaogrupo.text()
        if descricaogrupo=='':
            Mensagem.mensagem_erro(self,"ERRO",'campo descriçao em branco') 
        else:
            db.adicionar(f''' insert into grupos(descricaogrupo)values('{descricaogrupo}')''')
            self.buscarGrupo()
            self.ui.wb_incluirgrupo.close()
            self.ui.tx_Descricaogrupo.clear()
            try:
                bancofoto=db.pega_dados(""" select codigogrupo FROM grupos ORDER BY codigogrupo DESC LIMIT 1""")
                self.pixmap.save(f"config/FotosGrupos/{bancofoto[0][0]}.png")
                self.ui.widget.setDisabled(False)
            except:KeyError
    def buscarGrupo(self):
        self.line_busca_cliente=self.ui.tx_buscarGrupos.text()
        dados =db.pega_dados(f"SELECT *FROM grupos WHERE descricaogrupo LIKE'%{self.line_busca_cliente}%'")
        if not dados:
            Mensagem.mensagem_erro(self,"ERRO",'grupo NAO EXISTE') 
        else:  
            self.ui.tab_GrupoPRodutos.setRowCount(0)
                
            for linha, row_data in enumerate (dados): 
                self.ui.tab_GrupoPRodutos.insertRow(linha)
                self.ui.tab_GrupoPRodutos.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(row_data[0])))
                self.ui.tab_GrupoPRodutos.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(row_data[1])))
                