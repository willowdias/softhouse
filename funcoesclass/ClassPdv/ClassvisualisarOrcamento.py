from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *
from funcoesclass.ClassPdv.ClassVenda import *
from funcoesclass.FormCode.FormVisualisarOrcamentos import*
from funcoesclass.databese.ClassQuery import*

class FormOrcamentos(QDialog):
    def __init__(self):
        QWidget.__init__(self)
        
        self.ui = Ui_FormOrcamento()
        self.ui.setupUi(self)
   
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint|Qt.Drawer)
        #self.setWindowFlags(Qt.Tool)
        self.showFullScreen()
        self.ui.tx_Buscarorcamento.editingFinished.connect(self.BuscarORcamento)
        self.ui.bt_apagar.clicked.connect(self.FunExcluirOrcamento)
        self.ui.dt_Data_emissao.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        self.ui.dt_Data_final.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        self.ui.bt_sair.clicked.connect(self.Closetela)
        #tamanho coluna
        self.ui.tb_orcamento.setColumnWidth(0, 160)#codigo barra
        self.ui.tb_orcamento.setColumnWidth(1, 500)
        self.ui.tb_orcamento.setColumnWidth(2, 135)
    def BuscarORcamento(self):
        self.ui.tb_orcamento.setRowCount(0)
        nota=self.ui.tx_Buscarorcamento.text()
        
        banco=db.pega_dados(f''' select * from orcas where nota like'%{nota}%' and Finalizar='N' ''')
        for linha,row in enumerate(banco):
            self.ui.tb_orcamento.insertRow(linha)
            self.ui.tb_orcamento.setItem(linha, 0, QTableWidgetItem(str(row[1])))#codigo
            self.ui.tb_orcamento.setItem(linha, 1, QTableWidgetItem(str(row[2])))#codigo
            self.ui.tb_orcamento.setItem(linha, 2, QTableWidgetItem(str(("R$ {:.2f}".format(row[3])))))#valor TOTAL
    def Closetela(self):
        self.fechar=Mensagem.confirmacao(self,'deseja','deseja fechar tela')
        if self.fechar:
            self.close()
    def FunExcluirOrcamento(self):
        try:
            selecionaorca=self.ui.tb_orcamento.selectedItems()[0].text()
            self.apaga=Mensagem.confirmacao(self,"deseja apagar",f'deseja apagar orçamento {selecionaorca}')
            if self.apaga:
                db.apaga(f'''delete from orcas where nota ='{selecionaorca}' ''')
                self.BuscarORcamento()
                
        except:error