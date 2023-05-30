from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.databese.ClassQuery import*
#importa incluirClinetes
from funcoesclass.FormCode.FormContaApagar import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
#fornecedo
from funcoesclass.ClassFormSegundaria.ClassFormIncluirFornecedor import*
#incluri apagar
from funcoesclass.FormCode.FormIncluirApagar import*
from datetime import timedelta
from datetime import datetime
import datetime
class FormContasApagar(QDialog):#conta apagar
    def __init__(self,x=None):
        QWidget.__init__(self)
      
        self.ui = Ui_FormContaApagar()
        self.ui.setupUi(self)
        self.ui.widget.setMinimumSize(int(x)-41,0)
        #coluna table itens
        #self.ui.widget.setGeometry(0,0,int(x),0)
        self.ui.tab_contApagar.setColumnWidth(0, 1)
        self.ui.tab_contApagar.setColumnWidth(6, 450)
        self.ui.dt_final.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        self.ui.dt_inicial.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        self.ui.dt_pagamento.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        #numera
        self.ui.tx_ValorLquidopagamento.setValidator(QDoubleValidator(0.99999,99999999.9999999,2))
        self.ui.tx_valobrutopagamento.setValidator(QDoubleValidator(0.99999,99999999.9999999,2))
        self.ui.tx_valorTotaPAgamento.setValidator(QDoubleValidator(0.99999,99999999.9999999,2))
        #closeframe data
        self.ui.FrameDataemisao.close()
        self.ui.bt_ConsultaData.clicked.connect(self.ui.FrameDataemisao.show)
       
        self.ui.bt_novaNota.clicked.connect(lambda:FormIncluirApagar().exec_())
        #consulta banco
        self.ui.bt_ConfirmaData.clicked.connect(lambda:self.FunCarregarApagar('data'))
        self.ui.bt_FiltraNota.clicked.connect(lambda:self.FunCarregarApagar('consulta'))
        #close wb pagar
        self.ui.Wd_Pamento.close()
        #tipo documento

        self.ui.tab_contApagar.doubleClicked.connect(self.marca)
        self.ui.tab_contApagar.addAction(self.ui.actionmarca_todos)
        self.ui.tab_contApagar.addAction(self.ui.actiondesmarca)
        self.ui.actionmarca_todos.triggered.connect(self.MarcaTodos)
        self.ui.actiondesmarca.triggered.connect(self.DesmarcaTodos)
        #marca
        self.shortcut_open = QShortcut(QKeySequence('Space'), self)
        self.shortcut_open.activated.connect(self.marca)
        #baixaSelecionada
        self.ui.bt_baixa.clicked.connect(self.BaixaSelecionada)
    def FunCarregarApagar(self,item_nota):
        descricao=self.ui.tx_buscaNota.text()
        data=self.ui.dt_inicial.text()
        datafinal=self.ui.dt_final.text()
       
        if item_nota=='consulta':
            banco=db.pega_dados(f''' select * from tb_contasapagar where descricao like'%{descricao}%' or nota like'%{descricao}'  ''')
        if item_nota=='data':
           
            banco=db.pega_dados("SELECT *FROM tb_contasapagar WHERE data_inicial >= '{}' AND data_final <= '{}'".format(data,datafinal))
            
        self.ui.tab_contApagar.setRowCount(0)
        for linha,row in enumerate(banco):
            self.ui.tab_contApagar.insertRow(linha)
            
            self.checkbox = QCheckBox()
            self.checkbox.setCheckState(Qt.Unchecked)
            self.ui.tab_contApagar.setCellWidget(linha, 0, self.checkbox)
            self.checkbox.setLayoutDirection(Qt.RightToLeft)
            self.checkbox.toggled.connect(self.seleciona)
         
            self.ui.tab_contApagar.setItem(linha, 0, QTableWidgetItem(str(row[0])))#id
            self.ui.tab_contApagar.setItem(linha, 1, QTableWidgetItem(str(row[1])))#nota
            self.ui.tab_contApagar.setItem(linha, 2, QTableWidgetItem(str(row[2])))#descriçao
            self.ui.tab_contApagar.setItem(linha, 3, QTableWidgetItem(str(row[3])))#valor
            self.ui.tab_contApagar.setItem(linha, 4, QTableWidgetItem(str(row[4])))#dtinicial
            self.ui.tab_contApagar.setItem(linha, 5, QTableWidgetItem(str(row[5])))#dtfinal
            self.ui.tab_contApagar.setItem(linha, 6, QTableWidgetItem(str(row[7])))#fornecedo
            self.ui.tx_valorTotal.clear()
  
       
    def DesmarcaTodos(self):
        for i in range(self.ui.tab_contApagar.rowCount()):
            self.checkbox = QCheckBox()
            self.checkbox.setCheckState(Qt.Unchecked)
            self.ui.tab_contApagar.setCellWidget(i, 0, self.checkbox)
            self.checkbox.setLayoutDirection(Qt.RightToLeft)
            self.checkbox.toggled.connect(self.seleciona)
            self.seleciona()
    def MarcaTodos(self):
        for i in range(self.ui.tab_contApagar.rowCount()):
            self.checkbox = QCheckBox()
            self.checkbox.setCheckState(Qt.Checked)
            self.ui.tab_contApagar.setCellWidget(i, 0, self.checkbox)
            self.checkbox.setLayoutDirection(Qt.RightToLeft)
            self.checkbox.toggled.connect(self.seleciona)
            self.seleciona()
          
    def marca(self):#marca notinha por vez
        seleciona=self.ui.tab_contApagar.currentRow()
        self.checkbox = QCheckBox()
        self.checkbox.setCheckState(Qt.Checked)
        self.checkbox.setLayoutDirection(Qt.RightToLeft)
        self.ui.tab_contApagar.setCellWidget(seleciona, 0, self.checkbox)
        self.checkbox.toggled.connect(self.seleciona)
        self.seleciona()
        
    def seleciona(self):
        verificarvalor = []
        valor = []
        for i in range(self.ui.tab_contApagar.rowCount()):
            if self.ui.tab_contApagar.cellWidget(i, 0).isChecked():
                verificarvalor.append(self.ui.tab_contApagar.item(i, 0).text())
                valor.append(self.ui.tab_contApagar.item(i, 3).text().replace('R','').replace('$','').replace(',','.'))
                for  linha in range(0,7):
                    self.ui.tab_contApagar.item(i,linha).setBackground(QtGui.QColor(125,125,125))#marca Como listada
            else:
                self.ui.tx_valorTotal.clear()
                for  linha in range(0,7):
                    self.ui.tab_contApagar.item(i,linha).setBackground(QtGui.QColor(255,255,255))
        run = 0
        for i in valor:
            run+=float(i)
            tex=f'{run:_.2f}'
            tex=tex.replace('.',',').replace('_',('.'))
            self.ui.tx_valorTotal.setText(f"R$:{tex}")  
        
    def BaixaSelecionada(self):
        valor=[]
        for i in range(self.ui.tab_contApagar.rowCount()):
            if self.ui.tab_contApagar.cellWidget(i, 0).isChecked():
                valor.append(self.ui.tab_contApagar.item(i, 3).text().replace('R','').replace('$','').replace(',','.'))
             
          
        r = 0
        
        if len(valor)==0:
            Mensagem.mensagem(self,"campo",'nao foi selecionado nenhum pagamento')
        else:
            self.ui.Wd_Pamento.show() 
            for i in valor:
                r+=float(i)
                tex=f'R$ {r:_.2f}'
                tex=tex.replace('.',',').replace('_',('.'))
                
                self.ui.tx_ValorLquidopagamento.setText(str(tex))   
                self.ui.tx_valobrutopagamento.setText(str(tex))
                self.ui.tx_valorTotaPAgamento.setText(str(tex))
#######################################################################################################################################             
class FormIncluirApagar(QDialog):#conta apagar
    def __init__(self):
        QWidget.__init__(self)
      
        self.ui = Ui_FormIncluirApagar()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()
      
        self.ui.tab_contApagar.setColumnWidth(0, 2)
        self.ui.bt_proceSPagamento.clicked.connect(self.FunCacularPagamento)
        self.ui.dt_inicial.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        self.ui.tx_valortotalparcela.editingFinished.connect(self.valorP)
        #deixa como codigo
        self.ui.tx_valortotalparcela.setValidator(QDoubleValidator(0.99999,99999999.9999999,2))
        self.ui.tx_quantidadeparcela.setValidator(QDoubleValidator(0.99999,99999999.999999,2))
        self.ui.tx_codigoFornecedor.setValidator(QDoubleValidator(0.99999,99999999.999999,2))
        #
        self.ui.tx_codigoFornecedor.addAction(self.ui.actionbuscar_fornecedor, QLineEdit.TrailingPosition)
        self.ui.actionbuscar_fornecedor.triggered.connect(self.TelaFornecedor)
        #adicionar
        self.ui.bt_adicionar.clicked.connect(self.FunAdicioPagar)
    def TelaFornecedor(self):
        self.FormIncluirFornecedor=FormIncluirFornecedor()
        def selecionaForcedor():
            try:
                seleciona=self.FormIncluirFornecedor.ui.tab_Fornecedor.selectedItems()
                self.ui.tx_codigoFornecedor.setText(seleciona[0].text())
                self.ui.tx_descricaofornecedo.setText(seleciona[1].text())
                self.FormIncluirFornecedor.close()
            except:error 
        self.FormIncluirFornecedor.ui.tab_Fornecedor.doubleClicked.connect(selecionaForcedor)
        self.FormIncluirFornecedor.exec_()
    def valorP(self):
        try:
            valortotalparcela =int(self.ui.tx_valortotalparcela.text())
            tex=f'{valortotalparcela:_.2f}'
            tex=tex.replace('.',',').replace('_',('.'))
            self.ui.tx_valortotalparcela.setText(str(tex))
        except:error
    def FunCacularPagamento(self):
        try:
            valorTotalVenda=float(self.ui.tx_valortotalparcela.text().replace('.','').replace(',','.'))
            parcela=int(self.ui.tx_quantidadeparcela.text())
            final=(valorTotalVenda/parcela)
            tex=f'R$ {final:_.4f}'
            total=tex.replace('.',',').replace('_',('.'))
        except:
            Mensagem.mensagem(self,"Campos PArcela","campos vazio parcelas ou valo total")

        
        run=0 
        dados=datetime.datetime.strptime(f"{self.ui.dt_inicial.text()}","%d/%m/%Y")
        self.ui.tab_contApagar.setRowCount(0) 
        for i in range(0,parcela):#fracionar datas
            run+=1
            dados=dados + timedelta(days=30) 
            datafinal=dados.strftime("%d/%m/%Y")
            self.ui.tab_contApagar.insertRow(i)
            self.ui.tab_contApagar.setItem(i, 0, QTableWidgetItem(str(self.ui.tx_descricao.text())))#descriçao
            self.ui.tab_contApagar.setItem(i, 1, QTableWidgetItem(str(f'{run}/{run}')))#parcelas
            self.ui.tab_contApagar.setItem(i, 2, QTableWidgetItem(str(f'{total}')))#totalparcelas
            self.ui.tab_contApagar.setItem(i, 3, QTableWidgetItem(str(f'{self.ui.dt_inicial.text()}')))#data emissao
            self.ui.tab_contApagar.setItem(i, 4, QTableWidgetItem(str(f'{datafinal}')))#data emissao
            self.ui.tab_contApagar.setItem(i, 5, QTableWidgetItem(str(f'{self.ui.tx_descricaofornecedo.text()}')))#fornecedor
                
        for i in range(0,parcela):
            for linha in range(0,5):
                self.ui.tab_contApagar.item(i,linha).setTextAlignment(Qt.AlignCenter)    
                 
    def FunAdicioPagar(self):
        try:
            valorTotalVenda=float(self.ui.tx_valortotalparcela.text().replace('.','').replace(',','.'))
            parcela=int(self.ui.tx_quantidadeparcela.text())
            final=(valorTotalVenda/parcela)
            tex=f'R$ {final:_.4f}'
            total=tex.replace('.',',').replace('_',('.'))
        except:
            Mensagem.mensagem(self,"Campos PArcela","campos vazio parcelas ou valo total")

        
        run=0 
        dados=datetime.datetime.strptime(f"{self.ui.dt_inicial.text()}","%d/%m/%Y")
        self.ui.tab_contApagar.setRowCount(0) 
        for i in range(0,parcela):#fracionar datas
            run+=1
            dados=dados + timedelta(days=30) 
            datafinal=dados.strftime("%d/%m/%Y")
            
            db.adicionar(f''' insert into tb_contasapagar (nota,descricao,valor,data_inicial,data_final,
                         codigo_fornecedor,fornecedor)values ('{run}/{run}','{self.ui.tx_descricao.text()}','{total.replace('R','').replace('$','')}',
                         '{self.ui.dt_inicial.text()}','{datafinal}','{self.ui.tx_codigoFornecedor.text()}','{self.ui.tx_descricaofornecedo.text()}') ''')