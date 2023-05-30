from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.FormCode.FormControleioClientes import*

from funcoesclass.databese.ClassQuery import*
#importa incluirClinetes
from funcoesclass.ClassFormSegundaria.ClassFormIncluirclientes import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *
import os
#impor visualisar pdf
from funcoesclass.ClassFormPdf.visualisarPdf  import*
#from Gera pdf
from funcoesclass.ClassFormPdf.FichaCadastro import*
import pywhatkit as kt
class FormCadastroClientes(QDialog):#essa tela puxa os quarto
    def __init__(self,Verifica=None):
        QWidget.__init__(self)
      
        self.ui = Ui_ct_MainClientes()
        self.ui.setupUi(self)
        #focus
        
        #coluna table itens
        self.ui.tableWidget_usuario_2.setColumnWidth(0, 90)
        self.ui.tableWidget_usuario_2.setColumnWidth(1, 400)
        self.ui.tableWidget_usuario_2.setColumnWidth(2, 200)
        self.ui.tableWidget_usuario_2.setColumnWidth(3, 300)

        #Chama Tela Incluir Cliente
        self.ui.bt_novo.clicked.connect(self.Fun_NovoCliente)
       
        #busca clientes 
        self.ui.tx_BuscaClientes.editingFinished.connect(self.Fun_busca_clientes)
        self.ui.bt_BuscaClientes.clicked.connect(self.Fun_busca_clientes)
        self.ui.bt_alterar.clicked.connect(self.Fun_Edita_cliente)
        self.ui.bt_Excluir.clicked.connect(self.Fun_Excluir_cliente)
        self.ui.bt_Imprimir.clicked.connect(self.FunImPrimiFichaCliente)
        #verificapdf cliente double clicked
        self.verifica=Verifica
        if self.verifica=="S":
            pass
        else:
            self.ui.tableWidget_usuario_2.doubleClicked.connect(self.Fun_Edita_cliente)
        #ajuste label
        
        #seleciona clisen
        self.ui.tableWidget_usuario_2.itemSelectionChanged.connect(self.SelecionaImagenPasta)

        #envia mensagemWhatsap
        self.ui.bt_WhatssapEnvio.clicked.connect(self.enviarMensagemWhatsapp)
    
    def enviarMensagemWhatsapp(self):
        try:
            selecionar=self.ui.tableWidget_usuario_2.selectedItems()[0].text()
            dados =db.pega_dados(f"SELECT *FROM tb_clientes WHERE id='{selecionar}'")
            if dados[0][5]=='':
                Mensagem.mensagem(self,"","Cliente Sem telefone Cadastrado")
            else:
                while True:
                    time.sleep(0.05)
                    kt.sendwhatmsg_instantly(f"+55{dados[0][5]}",f'''bom dia  {dados[0][1]} atraves dessa mensagem venho fazer cobrança''',True)

                    break
             
        except:error
    def SelecionaImagenPasta(self):
        try:
            itens=self.ui.tableWidget_usuario_2.selectedItems()
            self.ui.Lb_nome.setText(str(itens[1].text()))
            for nome_arquivo in os.listdir(f'{os.getcwd()}/config/FotosClientes'):
                if f'{str(itens[0].text())}' in nome_arquivo:#verifica se img na pasta
                    pixmap = QtGui.QPixmap(f'{os.getcwd()}/config/FotosClientes/{nome_arquivo}') # Setup pixmap with the provided image        
                    self.pixmap = pixmap.scaled(100,100, QtCore.Qt.KeepAspectRatio)
                    self.ui.lb_fotoCliente.setPixmap( self.pixmap) # Set the pixmap onto the label
                    self.ui.lb_fotoCliente.setAlignment(QtCore.Qt.AlignCenter) 
           
        except:error
    def Fun_Excluir_cliente(self):#excluir clientes  
        try:
            self.apagar=Mensagem.confirmacao(self,"DESEJA","DESEJA APAGAR CLIENTE")
            if self.apagar:
                itens=self.ui.tableWidget_usuario_2.selectedItems()
                db.apaga(f''' DELETE FROM tb_clientes where id='{itens[0].text()}' ''')
                
                recupera_imagen = f'{os.getcwd()}/config/FotosClientes'
                for nome_arquivo in os.listdir(recupera_imagen):
                    if f'{str(itens[0].text())}' in nome_arquivo:#verifica se img na pasta
                        removefoto=nome_arquivo
                        os.remove(os.path.join(recupera_imagen, removefoto)) 
                self.Fun_busca_clientes()
        except:error
        
    def Fun_Edita_cliente(self):#edita Cliente
        
        try:
            itens=self.ui.tableWidget_usuario_2.selectedItems()
            self.FormIncluirClientes=FormIncluirClientes("alterar",str(itens[0].text()),self.ui.tx_BuscaClientes,self.Fun_busca_clientes)
            self.FormIncluirClientes.setModal(True)
            self.FormIncluirClientes.exec_()
        except:error
    def Fun_NovoCliente(self):#adiciona Novo clientes
        self.FormIncluirClientes=FormIncluirClientes("s",'',self.ui.tx_BuscaClientes,self.Fun_busca_clientes)
        self.FormIncluirClientes.setModal(True)
        self.FormIncluirClientes.exec_()

    def Fun_busca_clientes(self):
        self.line_busca_cliente=self.ui.tx_BuscaClientes.text()
        dados =db.pega_dados(f"SELECT *FROM tb_clientes WHERE Nome LIKE'%{self.line_busca_cliente}%'")
        if not dados:
            Mensagem.mensagem_erro(self,"ERRO",'CLIENTE NAO EXISTE') 
        else:  
            self.ui.tableWidget_usuario_2.setRowCount(0)
                
            for linha, row_data in enumerate (dados): 
                self.ui.tableWidget_usuario_2.insertRow(linha)
                self.ui.tableWidget_usuario_2.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(row_data[0])))
                self.ui.tableWidget_usuario_2.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(row_data[1])))
                self.ui.tableWidget_usuario_2.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(row_data[5])))
                self.ui.tableWidget_usuario_2.setItem(linha, 3, QtWidgets.QTableWidgetItem(str(row_data[7])))
        ''' self.ui.listWidget.clear()     
        for index, name in enumerate(dados):
            item = QListWidgetItem(QIcon(f'{os.getcwd()}/FotosClientes/{name[0]}.png'), name[1])
            #self.ui.listWidget.setIconSize(QtCore.QSize(50, 50))   '''
        '''self.ui.listWidget.insertItem(index, item) '''
    def FunImPrimiFichaCliente(self):
        try:
            self.imprimiFicha=self.ui.tableWidget_usuario_2.selectedItems()[0].text()
            FichaCadastro(f'{self.imprimiFicha}')
            self.FormVisualisarPDf=FormVisualisarPDf('Ficha',f'{self.imprimiFicha}','FichaCadastro')
            self.FormVisualisarPDf.setModal(True)
            self.FormVisualisarPDf.exec_()
        except:error
  