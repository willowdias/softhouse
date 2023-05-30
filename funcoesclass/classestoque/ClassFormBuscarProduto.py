from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *
from funcoesclass.databese.ClassQuery import*

from funcoesclass.FormCode.FormBuscarProduto import*
class Buscarproduto(QDialog):
    def __init__(self):
        QWidget.__init__(self)

        self.ui = Ui_FormBuscarProduto()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.showFullScreen()
        self.ui.tx_BuscarEstoque_2.returnPressed.connect(self.Fun_BuscarItenEstoque)
    def Fun_BuscarItenEstoque(self):
    
        
        self.buscaEstoque=self.ui.tx_BuscarEstoque_2.text()
      
        dados =db.pega_dados(f'''SELECT *FROM tb_estoque WHERE descricao LIKE '%{self.buscaEstoque}%' ''')
        if self.buscaEstoque=='':
            self.ui.Tab_Estoque.setRowCount(0)
        if not dados:
            Mensagem.mensagem_erro(self,"ERRO",'item nao existe no estoque') 
        else:  
            self.ui.Tab_Estoque.setRowCount(0)
                
            for linha, row_data in enumerate (dados): 
              
                self.ui.Tab_Estoque.insertRow(linha)
                self.ui.Tab_Estoque.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(row_data[1])))#codigo barra
                self.ui.Tab_Estoque.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(row_data[2])))#DESCRICAO
                self.ui.Tab_Estoque.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(row_data[6])))#QUANTIDADE
                valorestoque = ('%.2f'%(row_data[8]))
                self.ui.Tab_Estoque.setItem(linha, 3, QtWidgets.QTableWidgetItem(f'R$ {str(valorestoque)}'))#VALOR
            
            for i in range(len(dados)):
                for linha in range(0,4):
                    self.ui.Tab_Estoque.item(i,linha).setTextAlignment(Qt.AlignCenter)
                