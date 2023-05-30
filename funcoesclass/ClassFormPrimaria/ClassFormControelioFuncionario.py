from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.databese.ClassQuery import*
#importa incluirClinetes
from funcoesclass.FormCode.FormConTroleioFuncionario import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
from funcoesclass.ClassFormSegundaria.ClassIncluirFuncionario import*
class FormControleioFuncio(QDialog):#essa tela puxa os quarto
    def __init__(self,verificar=None):
        QWidget.__init__(self)
      
        self.ui = Ui_FormCadasTroFuncionario()
        self.ui.setupUi(self)
        self.ui.Tab_funcionario.setColumnWidth(0, 80)
        self.ui.Tab_funcionario.setColumnWidth(1, 300)
        #self.ui.bt_novo.clicked.connect(lambda:IncluirFuncionario().exec_())
        self.ui.bt_novo.clicked.connect(self.FunChamaSegundaTEla)
        self.ui.Bt_Alterar.clicked.connect(self.FunChamaSegundaTEla)
        self.ui.tx_BuscaFuncionario.returnPressed.connect(self.FunBuscarFuncionario)
        self.ui.Tab_funcionario.doubleClicked.connect(self.ui.Bt_Alterar.click)
        #excluir
        self.ui.Bt_excluir.clicked.connect(self.FunexcluiRFuncionario)
    def FunBuscarFuncionario(self):
        buscaFuncionario=self.ui.tx_BuscaFuncionario.text()
        banco=db.pega_dados(f'''select *from tb_funcionario where  nome like '%{buscaFuncionario}%' ''')
        self.ui.Tab_funcionario.setRowCount(0)
        for linha,row in enumerate(banco):
            self.ui.Tab_funcionario.insertRow(linha)
            self.ui.Tab_funcionario.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(row[0])))#codigo
            self.ui.Tab_funcionario.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(row[1])))#nome
            self.ui.Tab_funcionario.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(row[2])))#sobrenome
            self.ui.Tab_funcionario.setItem(linha, 3, QtWidgets.QTableWidgetItem(str(row[6])))#status
            for i in range(0,4):
                self.ui.Tab_funcionario.item(linha,i).setTextAlignment(Qt.AlignCenter)
            self.FunVerificaFuncionarioAtivo(row[0],linha)
    def FunChamaSegundaTEla(self):
        clickedButton = self.sender()
        digitValue = str(clickedButton.text())
        if digitValue=="novo funcionario":
            self.form=IncluirFuncionario(self.ui.tx_BuscaFuncionario,self.FunBuscarFuncionario,str(digitValue))
            self.form.exec_()
        elif digitValue=="alterar":
            try:
                seleciona=self.ui.Tab_funcionario.selectedItems()[0].text()
                self.form=IncluirFuncionario(self.ui.tx_BuscaFuncionario,self.FunBuscarFuncionario,str(digitValue),str(seleciona))
                self.form.exec_()
            except:error
            
    def FunexcluiRFuncionario(self):
        self.confirma=Mensagem.confirmacao(self,'excluir Funcionario','Deseja Excluir Funcionario')
        if self.confirma:
            try:
                seleciona=self.ui.Tab_funcionario.selectedItems()[0].text()
                db.pega_dados(f''' DELETE FROM tb_funcionario WHERE CODIGO ='{seleciona}' ''')
                self.FunBuscarFuncionario()
            except:error
            
    def FunVerificaFuncionarioAtivo(self,Id,linha):
   
        banco=db.pega_dados(f'''select *from tb_funcionario where codigo='{Id}' ''')
        for i in banco:
            status=i[6]
            if status=="N" or status=="":
                for linhas in range(0,4):
                    self.ui.Tab_funcionario.item(linha,linhas).setBackground(QtGui.QColor(255, 0, 0))
    