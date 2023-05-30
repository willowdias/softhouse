from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.FormCode.FormControleioEstoques import*

from funcoesclass.classestoque.ClassFormIncluirEstoque import*
from funcoesclass.databese.ClassQuery import*
from funcoesclass.classestoque.relatiosestoque.Formabrirelatorio import*
from funcoesclass.classestoque.relatiosestoque.imprimirrelatorioestoque import*
import os
class FormControleioEstoque(QDialog):#essa tela puxa os quarto
    def __init__(self):
        QWidget.__init__(self)
       
        self.ui = Ui_FormEstoque()
        self.ui.setupUi(self)
        
        self.showFullScreen()
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        #coluna table itens
        self.ui.Tab_Estoque.setColumnWidth(0, 150)
        self.ui.Tab_Estoque.setColumnWidth(1, 400)
        self.ui.Tab_Estoque.setColumnWidth(5, 300)
        self.ui.Tab_Estoque.setColumnWidth(5, 80)
        #add action na tabela estoque
        lista=[self.ui.actioneditar,self.ui.actionexcluri,self.ui.actionNOVOPRODUTO]
        for action in lista:
            self.ui.Tab_Estoque.addAction(action)
        #action trigrered
        self.ui.actionNOVOPRODUTO.triggered.connect(self.Fun_novoProduto)
        self.ui.actionexcluri.triggered.connect(self.DeleTaProduto)
        self.ui.actioneditar.triggered.connect(self.Fun_EditarIten)
        #novo produto
        self.ui.bt_novo_procuto.clicked.connect(self.Fun_novoProduto)
        #buscar item estoque
        self.ui.tx_BuscarEstoque.returnPressed.connect(self.Fun_BuscarItenEstoque)
        #seelciona item
        self.ui.Tab_Estoque.itemSelectionChanged.connect(self.FunPRevisualisarItens)
        self.selection = self.ui.Tab_Estoque.selectionModel()
        #altera
        self.ui.bt_altera.clicked.connect(self.Fun_EditarIten)
        #imprimir estoque
        self.ui.bt_imprimir.clicked.connect(self.imprirmirelatorio)
        #deleta produto
        self.ui.bt_apagar.clicked.connect(self.DeleTaProduto)
        form = ["descricao","codigo_barra","marca","fonecedor",'ncm']
        formapagamento = [item for item in form]
        self.ui.combox_localizaestoque.addItems(formapagamento)
        self.ui.combox_localizaestoque.activated.connect(lambda:self.ui.tx_BuscarEstoque.setFocus())
        self.ui.combox_localizaestoque.activated.connect(lambda:self.ui.tx_BuscarEstoque.selectAll())
    def Fun_novoProduto(self):#novo produto
        self.FormIncluirEstoque=FormIncluirEstoque('N','None')
        self.FormIncluirEstoque.setModal(True)
        #self.FormIncluirEstoque.ui.tx_codigoBarra.setText(str(self.geracodigobarra()))

        self.FormIncluirEstoque.exec_()
    def Fun_BuscarItenEstoque(self):
        self.ui.lb_fotoitem.clear()
        
        
        if self.ui.ch_ativo.isChecked():
            ativo="S"
            self.buscaEstoque=self.ui.tx_BuscarEstoque.text()
            descricao=(self.ui.combox_localizaestoque.currentText())
            try:
                dados =db.pega_dados(f'''SELECT *FROM tb_estoque WHERE {descricao} LIKE '%{self.buscaEstoque}%' and ativo ='{ativo}' ''')
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
                    self.ui.tx_quantidadeprodutoestoque.setText(str(len(dados)))
                    for i in range(len(dados)):
                        for linha in range(0,4):
                            self.ui.Tab_Estoque.item(i,linha).setTextAlignment(Qt.AlignCenter)
            except:error 
        if self.ui.ch_inativo.isChecked():
            ativo="I"
            self.buscaEstoque=self.ui.tx_BuscarEstoque.text()
            descricao=(self.ui.combox_localizaestoque.currentText())
            try:
                dados =db.pega_dados(f'''SELECT *FROM tb_estoque WHERE {descricao} LIKE '%{self.buscaEstoque}%' and ativo ='{ativo}' ''')
                if self.buscaEstoque=='':
                    self.ui.Tab_Estoque.setRowCount(0) 
                if not dados:
                    Mensagem.mensagem_erro(self,"ERRO",'item nao existe no estoque')
            
                else:  
                    self.ui.Tab_Estoque.setRowCount(0)
                        
                    for linha, row_data in enumerate (dados): 
                    
                        self.ui.Tab_Estoque.insertRow(linha)
                        codigobarra = QTableWidgetItem(str(f'{row_data[1]}'))
                        text_color = QColor(255, 0, 0)
                        codigobarra.setForeground(text_color)
                        self.ui.Tab_Estoque.setItem(linha, 0,codigobarra)#codigo barra
                        
                        descricao = QTableWidgetItem(str(f'{row_data[2]}'))
                        descricao.setForeground(text_color)
                        self.ui.Tab_Estoque.setItem(linha, 1, descricao)#DESCRICAO
                        
                        quant = QTableWidgetItem(str(f'{row_data[6]}'))
                        quant.setForeground(text_color)
                        self.ui.Tab_Estoque.setItem(linha, 2, quant)#QUANTIDADE
                        
                        
                        valorestoque = ('%.2f'%(row_data[8]))
                        vl_custo = QTableWidgetItem(str(f'{valorestoque}'))
                        vl_custo.setForeground(text_color)
                        self.ui.Tab_Estoque.setItem(linha, 3,vl_custo)#VALOR custo
                        
                    self.ui.tx_quantidadeprodutoestoque.setText(str(len(dados)))
                    for i in range(len(dados)):
                        for linha in range(0,4):
                            self.ui.Tab_Estoque.item(i,linha).setTextAlignment(Qt.AlignCenter)
            except:error 

    def DeleTaProduto(self):
        try:
        
            selecionaProdutoApagar=self.ui.Tab_Estoque.selectedItems()
            self.apagaitem=Mensagem.confirmacao(self,"DESEJA","DESEJA APAGAR ITEM SELECIONADO")
            if self.apagaitem:
                self.bancoitemapaga=db.pega_dados(f""" SELECT * FROM tb_estoque where codigo_barra='{selecionaProdutoApagar[0].text()}'""")
                
                recupera_imagen = f'{os.getcwd()}/config/FotosEstoque'
                for nome_arquivo in os.listdir(recupera_imagen):
                    if f'{str(self.bancoitemapaga[0][0])}' in nome_arquivo:#verifica se img na pasta
                        removefoto=nome_arquivo
                        os.remove(os.path.join(recupera_imagen, removefoto))
                db.apaga(f''' DELETE FROM tb_estoque where id='{str(self.bancoitemapaga[0][0])}' ''') 
                self.Fun_BuscarItenEstoque()      
            else:       
                error
        except:return
       
    def Fun_EditarIten(self):
        try:
            Selecionar_iten=self.ui.Tab_Estoque.selectedItems()

       
            self.FormIncluirEstoque=FormIncluirEstoque('S',str(Selecionar_iten[0].text()))
            self.FormIncluirEstoque.setModal(True)
            self.FormIncluirEstoque.exec_()
        except:error
  
    def FunPRevisualisarItens(self):
        
        try:
            
            vesiualisar=self.ui.Tab_Estoque.selectedItems()
            self.ui.tx_codigoBarra.setText(vesiualisar[0].text())
            self.ui.tx_descricao.setText(vesiualisar[1].text())
            self.ui.tx_QuantidaDeProduto.setText(vesiualisar[2].text())

            bancoestoque=db.pega_dados(f"""SELECT * FROM tb_estoque where codigo_barra='{vesiualisar[0].text()}'   """)
            for nome_arquivo in os.listdir(f'{os.getcwd()}/FotosEstoque'):
                if f'{str(bancoestoque[0][0])}' in nome_arquivo:#verifica se img na pasta
                    
                    pixmap = QtGui.QPixmap(f'{os.getcwd()}/FotosEstoque/{nome_arquivo}') # Setup pixmap with the provided image        
                    self.pixmap = pixmap.scaled(100,100, QtCore.Qt.KeepAspectRatio)
                    self.ui.lb_fotoitem.setPixmap( self.pixmap) # Set the pixmap onto the label
                    self.ui.lb_fotoitem.setAlignment(QtCore.Qt.AlignCenter) 
           
     
        except:error
    
    def imprirmirelatorio(self):
        if self.ui.Tab_Estoque.rowCount()==0:
            pass
        else:
            relatorioitem(self.ui.Tab_Estoque)
            self.FormVisualisarPDf=relatorioestoque('relatorioestoque')
            self.FormVisualisarPDf.setModal(True) 
            self.FormVisualisarPDf.exec_()   
            
    
