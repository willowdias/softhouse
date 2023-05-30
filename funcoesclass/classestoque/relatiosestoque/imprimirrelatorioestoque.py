from fpdf import FPDF
from funcoesclass.databese.ClassQuery import*

from funcoesclass.FormCode.FormMessagemWidget import*
from funcoesclass.databese.ClassQuery import*
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt, QThread, QTimer, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import time
from funcoesclass.classestoque.relatiosestoque.Formabrirelatorio import*
from funcoesclass.classestoque.relatiosestoque.imprimirrelatorioestoque import*
class relatorioitem:
    def __init__(self,Tablewo=None,valortotal=None,dataHora=None): 
       
        
        numero = '123456'
        data_emissao = f'{str(dataHora)}'
        # Criação do objeto FPDF
        pdf = FPDF()
        
        #pdf = FPDF('P', 'mm', (100, 150))#coloca tamanho
        pdf.add_page()
        # Configuração da fonte
        pdf.set_font('Arial', 'B', 10)
       
        # Cabeçalho
        pdf.cell(0, 10, 'NFC-e número {}'.format(numero), 0, 1)
        pdf.cell(0, 10, 'Emissão: {}'.format(data_emissao), 0, 1)

        # Tabela com os dados da NFC-e
        pdf.ln(10)
        pdf.cell(35, 10, 'codigo barra', 1)
        pdf.cell(100, 10, 'Descriçao', 1)
        pdf.cell(25, 10, 'Quantidade', 1)
        pdf.cell(25, 10, 'Valor Total', 1)
        pdf.ln()
       
    
        for i in range(Tablewo.rowCount()):
                
                
            codigo=( Tablewo.item(i, 0).text())
            descricao=( Tablewo.item(i, 1).text())    
            quant=( Tablewo.item(i, 2).text())
            valorcusto=(Tablewo.item(i, 3).text()).replace('R','').replace('$','')
            pdf.cell(35, 10, f'{codigo}', 1)
            pdf.cell(100, 10, f'{descricao}', 1)#quantidade
            pdf.cell(25, 10, f'{quant} ', 1)#valor
            pdf.cell(25, 10, f'{valorcusto}', 1)
            pdf.ln()
            
                
          
                
      
        
            
        pdf.cell(35, 10, 'ok', 1)
        pdf.cell(100, 10, f'Quant 15', 1)
        pdf.cell(25, 10, f'R$ {str(valortotal)}', 1)
        pdf.cell(25, 10, f'R$ {str(valortotal)}', 1)
        pdf.ln()

        # Salvando o PDF
        pdf.image("ajuda.png",180,  2, 20)
        pdf.output('config/relatorioestoque/relatorioestoque.pdf', 'F')

        QApplication.processEvents()  
        
    def carrega(self,text):
        self.Thread.start()
class Mensagem3(QDialog):
    def __init__(self):
        QWidget.__init__(self)

        self.ui = Ui_FormMessagemWidget()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.ui.pushButton.clicked.connect(self.CloseTelas)
        
    def CloseTelas(self):
        self.FormVisualisarPDf=relatorioestoque('relatorioestoque')
        self.FormVisualisarPDf.setModal(True) 
        self.FormVisualisarPDf.exec_()         
        
class Thread_Load(QThread):
    update_signal = pyqtSignal(str)
    def _init_(self, parent=None):
        QThread._init_(self, parent)
        
    def run(self):
        run=0
        while True:
            run+=1
            self.update_signal.emit(str(run))
            time.sleep(1)
            
            
            