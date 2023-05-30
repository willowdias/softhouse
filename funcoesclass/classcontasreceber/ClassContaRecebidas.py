from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.databese.ClassQuery import*

from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
#importa PArcelas Clientes
from funcoesclass.FormCode.FormContaReceber import*
class Recebidos:
    def __init__(self):     
    
        pass
   
    def CarregaRecebidosClientes(self,dadosid=None,objeto=None):
        dados =db.pega_dados(f"SELECT *FROM tb_recebidos WHERE codcliente='{dadosid}'") 
        self.ui.tab_recebidos.setRowCount(0)
        for ds in dados:
      
            self.ui.lb_nome.setText(str(ds[4]))      
        for linha, row_data in enumerate (dados):
            self.ui.tab_recebidos.insertRow(linha)
            nominal=(f'{("R$ {:.2f}".format(row_data[5]))}')
            real=(f'{("R$ {:.2f}".format(row_data[7]))}')
            self.ui.tab_recebidos.setItem(linha, 0, QTableWidgetItem(str(row_data[1])))
            self.ui.tab_recebidos.setItem(linha, 1, QTableWidgetItem(str(row_data[2])))
            self.ui.tab_recebidos.setItem(linha, 2, QTableWidgetItem(str(row_data[4])))#nome
            self.ui.tab_recebidos.setItem(linha, 3, QTableWidgetItem(str(nominal)))#nominal
            self.ui.tab_recebidos.setItem(linha, 4, QTableWidgetItem(f'{str(row_data[6])}%'))#desconto
            self.ui.tab_recebidos.setItem(linha, 5, QTableWidgetItem(str(real)))
        total=0
        Nominal=0    
        for i in range(self.ui.tab_recebidos.rowCount()):
                nominalValor=(self.ui.tab_recebidos.item(i, 3).text()).replace('R','').replace('$','')
                Nominal+=float(nominalValor)
                self.ui.db_Nominmal.setValue(Nominal)
                
                valortotal=(self.ui.tab_recebidos.item(i, 5).text()).replace('R','').replace('$','')
                total+=float(valortotal)
                self.ui.tx_valorTotalparcela_2.setValue(total)