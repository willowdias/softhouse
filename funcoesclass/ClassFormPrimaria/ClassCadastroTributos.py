from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *
from funcoesclass.FormCode.FormCadastroTributos import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
from funcoesclass.databese.ClassQuery import*
import time
class ForCadastroTributos(QDialog):
    def __init__(self):
        QWidget.__init__(self)

        self.ui = Ui_FormCadastroTributos()
        self.ui.setupUi(self)
        
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
    
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
       
        self.showFullScreen()

        self.ui.widget.move(self.mapToGlobal(self.rect().center() - self.ui.widget.rect().center()))
        self.ui.wb_Incluirtributos.move(self.mapToGlobal(self.rect().center() - self.ui.wb_Incluirtributos.rect().center()))

       
       
        #tabela
        self.ui.tab_tributos.setColumnWidth(0, 25)
        self.ui.tab_tributos.setColumnWidth(1, 250)
        self.ui.tab_tributos.setColumnWidth(2, 80)
        
        #close
        self.ui.wb_Incluirtributos.close()
        self.ui.bt_Altera.close()
        #buscar
        self.ui.tx_buscarTributo.editingFinished.connect(self.TabelaTributos)
        #novotributo
        self.ui.bt_incluir.clicked.connect(self.showIncluir)
        self.ui.bt_SalvarPagamento.clicked.connect(self.incluir)
        self.ui.bt_sairlancamento.clicked.connect(self.Closeinclui)
        #altera
        self.ui.bt_selecionaAltera.clicked.connect(self.showalterar)
        self.ui.bt_Altera.clicked.connect(self.altera)
        self.ui.tab_tributos.doubleClicked.connect(self.showalterar)
    def Closeinclui(self):
        self.confirma=Mensagem.confirmacao(self,'Fechar','Fechar Sistema')
        if self.confirma:
            self.ui.wb_Incluirtributos.close()
            self.ui.bt_Altera.close()
            self.clerLine()
    def showIncluir(self):
        self.ui.wb_Incluirtributos.show()
        self.ui.bt_SalvarPagamento.show()
        self.ui.widget.setDisabled(True)
    def incluir(self):
        self.ui.bt_Altera.close()
        codst=self.ui.tx_codst.text()
        descricao=self.ui.tx_descricaotributo.text()
        aliquota=str(self.ui.tx_aliquota.value())
        db.adicionar(f''' insert into tb_classtributaria(codst,descricao,icms)values('{codst}'
                         ,'{descricao}','{aliquota}') ''')
        self.ui.wb_Incluirtributos.close()
        self.TabelaTributos()
        self.clerLine()
    
    def showalterar(self):
        try:
            self.ui.widget.setDisabled(True)
            self.ui.wb_Incluirtributos.show()
            self.ui.bt_Altera.show()
            self.ui.bt_SalvarPagamento.close()
            descricao=self.ui.tab_tributos.selectedItems()[1].text()
            form = db.pega_dados(f'''SELECT * FROM tb_classtributaria where descricao ='{descricao}'  ''')
            self.ui.tx_id.setText(str(form[0][0]))
            self.ui.tx_codst.setText(str(form[0][1]))
            self.ui.tx_descricaotributo.setText(str(form[0][2]))
            self.ui.tx_aliquota.setValue(float(form[0][3]))
        except:error
    def altera(self):
        self.confirma:Mensagem.confirmacao(self,'Altera','Deseja Altera ?')
        if self.confirma:
            idtx=self.ui.tx_id.text()
            codst=self.ui.tx_codst.text()
            descricao=self.ui.tx_descricaotributo.text()
            aliquota=str(self.ui.tx_aliquota.value())
            db.update(f''' update tb_classtributaria set codst='{codst}' ,descricao='{descricao}',icms='{aliquota}'
                    where id='{idtx}' ''')
            
            self.ui.bt_Altera.close()
            self.ui.wb_Incluirtributos.close()
            self.TabelaTributos()
            self.clerLine()
    def clerLine(self):
        self.ui.tx_codst.clear()
        self.ui.tx_descricaotributo.clear()
        self.ui.tx_aliquota.setValue(0)
        self.ui.widget.setDisabled(False)
    def TabelaTributos(self):
        descricao=self.ui.tx_buscarTributo.text()
        banco=db.pega_dados(f'''select * from tb_classtributaria where descricao like '%{descricao}%' ''')
        self.ui.tab_tributos.setRowCount(0)
        for linha,row in enumerate(banco):
            self.ui.tab_tributos.insertRow(linha)
            self.ui.tab_tributos.setItem(linha, 0, QTableWidgetItem(str(row[1])))#codst
            self.ui.tab_tributos.setItem(linha, 1, QTableWidgetItem(str(row[2])))#descriçao
            self.ui.tab_tributos.setItem(linha, 2, QTableWidgetItem(str(row[3])))#icms