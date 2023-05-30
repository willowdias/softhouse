from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.databese.ClassQuery import*

from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
#importa PArcelas Clientes
from funcoesclass.FormCode.FormContaReceber import*

def GeralReceber(self):
       
        dados =db.pega_dados(f"SELECT *FROM tb_receber")
        if not dados:
            self.ui.tb_geral.setRowCount(0)
            pass
        else:  
            self.ui.tb_geral.setRowCount(0)
            run=0
            for linha, row_data in enumerate (dados):
                self.ui.tb_geral.insertRow(linha)
                
                real=(f'{("R$ {:.2f}".format(row_data[4]))}')
                self.ui.tb_geral.setItem(linha, 0, QTableWidgetItem(str(row_data[0])))
                self.ui.tb_geral.setItem(linha, 1, QTableWidgetItem(str(row_data[1])))
                self.ui.tb_geral.setItem(linha, 2, QTableWidgetItem(str(row_data[2])))
                self.ui.tb_geral.setItem(linha, 3, QTableWidgetItem(str(row_data[3])))
                self.ui.tb_geral.setItem(linha, 4, QTableWidgetItem(str(real)))
                self.ui.tb_geral.setItem(linha, 5, QTableWidgetItem(str(real)))
                self.ui.tb_geral.setItem(linha, 6, QTableWidgetItem(str(row_data[6])))
                self.ui.tb_geral.setItem(linha, 7, QTableWidgetItem(str(row_data[7])))
                
            for i in range(self.ui.tb_geral.rowCount()):
                valortotal=(self.ui.tb_geral.item(i, 4).text()).replace('R','').replace('$','')
                run+=float(valortotal)
                self.ui.valoGeral.setValue(run)
def limparCampos(self):
        self.ui.tx_Numeronota.clear()
        self.ui.tx_codCliente.clear()
        self.ui.tx_descricaocliente.clear()
        self.ui.tx_codPArcelas.clear()
        self.ui.tx_descricaoparcelas.clear()
        self.ui.tx_quantPArcelas.clear()
        self.ui.tx_incluirValorpagamento.setValue(0)
        self.ui.dt_emissao.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        self.ui.dt_vencimento.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        self.ui.tab_receber.setRowCount(0)
        self.ui.tx_valorTotalparcela.setValue(0)
        self.ui.lb_CodigoClinte.clear()
        self.ui.lb_NomeCliente.clear()