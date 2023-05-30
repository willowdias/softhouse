from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.databese.ClassQuery import*
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox
from PyQt5.QtCore import Qt
from funcoesclass.FormCode.FormPagamentoControleioInterno import*
class FinalizaVenda(QDialog):#essa tela puxa os quarto
    def __init__(self,valorTotal=None):
        QWidget.__init__(self)
      
        self.ui = Ui_FormPagamentoControleioInterno()
        self.ui.setupUi(self)
        self.ui.tab_PAgamento_2.setColumnWidth(0, 10)#inde
        self.ui.tab_PAgamento_2.setColumnWidth(1, 80)#doc
        self.ui.tab_PAgamento_2.setColumnWidth(2, 220)#descricçao
        self.ui.tab_PAgamento_2.setColumnWidth(3, 180)#data
        self.ui.db_inde.setFocus()
        #carrega documentos
        self.CarregaDoc()
        self.ui.db_Valortotal.setValue(valorTotal)
        self.ui.db_valoindex.setValue(valorTotal)
        self.valorotal=valorTotal
    
        #finaliza venda
        #self.ui.bt_finalizaVenda.clicked.connect(self.FinalizaVenda)
        self.ui.db_inde.editingFinished.connect(lambda:self.ui.db_valoindex.setFocus())
        
        self.actionIncrement = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self.ui.db_inde)
        self.actionIncrement.activated.connect(self.inserirvalortabela)
        
        #liberaclientebusca
        self.ui.bt_Buscarcliente.clicked.connect(self.LiberaConsultacliente)
    def LiberaConsultacliente(self):#essa funçao libera busca clientes
       
        self.ui.tx_cliente.setDisabled(False)
        self.ui.tx_cliente.setFocus()
        lista=db.pega_dados('''select nome from tb_clientes ''')
        lista1=[]
        for i in lista:
            lista1.append(str(i[0]).upper())
            
        completer = QCompleter(lista1, self.ui.tx_cliente)
        completer.setCaseSensitivity(0)
        self.ui.tx_cliente.setCompleter(completer)  
    def inserirvalortabela(self):
        self.ui.db_Valortotal.setValue(self.valorotal)
        linha=self.ui.db_inde.value()
        valor=self.ui.db_valoindex.value()
        self.ui.tab_PAgamento_2.setItem(int(linha),4,QTableWidgetItem(f'R$ {str(valor)}'))
        test=0
        
        if self.ui.db_valoindex.value()<0:
            pass
        else:
            #essa funçao pega valores da tabelas com lista
            valortotal=[]
            tipodoc=[]
            for i in range(self.ui.tab_PAgamento_2.rowCount()):
                tipodoc.append(self.ui.tab_PAgamento_2.item(i,1).text())
                valortotal.append(self.ui.tab_PAgamento_2.item(i,4).text().replace('R','').replace('$',''))
        somarr=0
        #essa funçao verfica se tem algo a mais que valor real da erro
        my_list=[]
        for soma in valortotal:
            somarr+=float(soma)
            soma1=(somarr)
            if soma1>self.valorotal:
                my_list.append(soma) 
        for i in range(4,len(my_list)):
            QMessageBox.information(self,"Erro","Valor Pagamento incorre\n divergente do valor total")
        #essa funçao calcula valor totala e menos valor tabela
        run=0
        val=self.ui.db_Valortotal.value()
        for ind, numero in enumerate (valortotal):
                b=(tipodoc[ind],numero)
                run+=float(numero)
                valorfinal=(run)
                final=(val-valorfinal)
                self.ui.db_Valortotal.setValue(final)
                self.ui.db_valoindex.setValue(final)
    def CarregaDoc(self):#essa funlao carrega os documentos
        documento=db.pega_dados(''' select * from tb_tipodocumento ''')
        
        self.data=datetime.today().strftime("%d/%m/%Y").capitalize()
        self.ui.tab_PAgamento_2.setRowCount(0)
        
        for linha,doc in enumerate(documento):
            
            self.ui.tab_PAgamento_2.insertRow(linha)
            item0 = QTableWidgetItem(str(linha))  
            self.ui.tab_PAgamento_2.setItem(linha,0,item0)#doc
            
            item = QTableWidgetItem(str(doc[1]))
            item.setFlags(Qt.NoItemFlags)   
            self.ui.tab_PAgamento_2.setItem(linha,1,item)#doc
            
            item2 = QTableWidgetItem(str(doc[2]))
            item2.setFlags(Qt.NoItemFlags)       
            self.ui.tab_PAgamento_2.setItem(linha,2, item2)#descricaçao
            
            item3= QTableWidgetItem(str(self.data))
            item3.setFlags(Qt.NoItemFlags)       
            self.ui.tab_PAgamento_2.setItem(linha,3, item3)#descricaça
            
            item4= QTableWidgetItem(str('R$ 0.00'))
            item4.setFlags(Qt.NoItemFlags)       
            self.ui.tab_PAgamento_2.setItem(linha,4, item4)#valor
            
            
            
