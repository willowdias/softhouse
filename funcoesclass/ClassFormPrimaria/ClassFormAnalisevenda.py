from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.databese.ClassQuery import*
from datetime import timedelta
from datetime import datetime
import datetime
from funcoesclass.FormCode.FormAnaliseDevenda import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
class Formaanalisevenda(QDialog):#analise venda
    def __init__(self,x=None,y=None):
        QWidget.__init__(self)

        self.ui = Ui_FormAnaliseDevenda()
        self.ui.setupUi(self)
        self.ui.fundo.setMinimumWidth(x)
        #closse telas
        self.ui.wb_NumeroNotas.close()
        self.ui.FrameDataemisao.close()
        self.ui.wb_nomeCliente.close()
        self.ui.frameAnalisePoritem.close()
        self.ui.bt_notaSair.clicked.connect(self.CloseWideget)
        self.ui.bt_cancelarDatavenda.clicked.connect(self.CloseWideget)
        self.ui.bt_cancelarITens.clicked.connect(self.CloseWideget)
        self.ui.bt_sairCliente.clicked.connect(self.CloseWideget)
        #centraliza as telas busca
        self.listaobjestoitems=[self.ui.FrameDataemisao,
                                self.ui.frameAnalisePoritem,self.ui.wb_nomeCliente,self.ui.wb_NumeroNotas]
        for i in self.listaobjestoitems:
            i.move(self.mapToGlobal(self.rect().center()*1 - i.rect().center()))
           
        #data
        self.ui.dt_final.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        self.ui.dt_inicial.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        #numeronota
        self.ui.bt_notas.clicked.connect(lambda:self.showTela('Numero'))
        self.ui.bt_emissao.clicked.connect(lambda:self.showTela('data_emissao'))
        self.ui.bt_itens.clicked.connect(lambda:self.showTela('Itens'))
        self.ui.bt_clientes.clicked.connect(lambda:self.showTela('cliente'))
        self.ui.tx_numeroNota.setValidator(QDoubleValidator(0.99999,9.9999999,2))
        #consulta por numero
        self.ui.bt_CosultaNumeronota.clicked.connect(lambda:self.Consultanotas('numero'))
        self.ui.bt_ConfirmaDatavenda.clicked.connect(lambda:self.Consultanotas('data'))
        self.ui.bt_confirmaItens.clicked.connect(lambda:self.Consultanotas('itens'))
        
    def showTela(self,Tela):
        self.ui.fundo.setDisabled(True)
        if Tela=='Numero':
            self.ui.wb_NumeroNotas.show()
            #self.ui.wb_NumeroNotas.move(self.mapToGlobal(self.rect().center() - self.ui.wb_NumeroNotas.rect().center()))
        if Tela=="data_emissao":
            self.ui.FrameDataemisao.show()
           
        if Tela=='Itens':
            self.ui.frameAnalisePoritem.show()
    
        if Tela=='cliente':
            self.ui.wb_nomeCliente.show()
         
    def CloseWideget(self):
        self.confirma=Mensagem.confirmacao(self,'Fechar','deseja Fechar')
        if self.confirma:
            self.ui.wb_NumeroNotas.close()
            self.ui.FrameDataemisao.close()
            self.ui.frameAnalisePoritem.close()
            self.ui.wb_nomeCliente.close()
            self.ui.fundo.setDisabled(False)
    def Consultanotas(self,true):
        self.ui.fundo.setDisabled(False)
        self.ui.tb_analiseVenda.setRowCount(0)
        data=self.ui.dt_inicial.text()
        datafinal=self.ui.dt_final.text()
        
        if true=='numero':
            numeronota=self.ui.tx_numeroNota.text()
            banco=db.pega_dados(f'''select * from orcas where nota like '{numeronota}' ''')
            self.ui.wb_NumeroNotas.close()
        if true=='data':
            banco=db.pega_dados("SELECT *FROM orcas WHERE data_emissao >= '{}' AND data_final <= '{}'".format(data,datafinal))
            self.ui.FrameDataemisao.close()
        if true=='itens':
            iten=self.ui.tx_itens.text()
            itens=db.pega_dados(f'''select nota  from orca where cod_barra='{iten}' or descricao='{iten}'  ''')
       
            for i in itens:
                itens=db.pega_dados(f'''select * from orcas where nota ='{i[0]}' ''')
                for linha, row_data in enumerate (itens):
                
                    for linha, row_data in enumerate (itens):
                        
                        dataitem = QTableWidgetItem(str(row_data[4]))
                    
                        
                        icon = QIcon(':/novo/telainicial/calendario.png')
                        dataitem.setIcon(icon)
                        text_color = QColor(54, 162, 7)
                        dataitem.setForeground(text_color)
                        dataitem.setTextAlignment(Qt.AlignCenter)
                        self.ui.tb_analiseVenda.insertRow(linha)
                        numero_formatado = "{:.2f}".format(row_data[3])
                        self.ui.tb_analiseVenda.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(row_data[1])))#numero nota
                        self.ui.tb_analiseVenda.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(row_data[2])))#nome
                        self.ui.tb_analiseVenda.setItem(linha, 2, QtWidgets.QTableWidgetItem(f'R$ {str(numero_formatado)}'))#valor
                        self.ui.tb_analiseVenda.setItem(linha, 3,dataitem)#data emisao
                        self.ui.db_total.setValue(0)
                
                self.ui.tx_itens.clear()
                self.ui.frameAnalisePoritem.close()    
                self.somartabela()
        try:
            for linha, row_data in enumerate (banco):
                dataitem = QTableWidgetItem(str(row_data[4]))
                
                icon = QIcon(':/novo/telainicial/calendario.png')
                dataitem.setIcon(icon)
                text_color = QColor(54, 162, 7)
                dataitem.setForeground(text_color)
                dataitem.setTextAlignment(Qt.AlignCenter)
                numero_formatado = "{:.2f}".format(row_data[3])
                self.ui.tb_analiseVenda.insertRow(linha)
                self.ui.tb_analiseVenda.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(row_data[1])))#numero nota
                self.ui.tb_analiseVenda.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(row_data[2])))#nome
                self.ui.tb_analiseVenda.setItem(linha, 2, QtWidgets.QTableWidgetItem(f'R$ {str(numero_formatado)}'))#valor
                self.ui.tb_analiseVenda.setItem(linha, 3,dataitem)#data emisao
                self.ui.db_total.setValue(0)
                self.somartabela()
        except:error        
    def somartabela(self):        
        total=0      
        for credito in range(self.ui.tb_analiseVenda.rowCount()):
          
            valortotal=(str(self.ui.tb_analiseVenda.item(credito, 2).text().replace('R','').replace('$','')))
            total += float(valortotal)
            self.ui.db_total.setValue(total)
           
        self.ui.tx_nomecliente.clear()
        self.ui.tx_numeroNota.clear()
        self.ui.tx_itens.clear()