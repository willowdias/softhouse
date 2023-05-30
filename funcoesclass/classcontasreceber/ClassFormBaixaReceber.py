from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.FormCode.FormBaixaReceber import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *
from funcoesclass.databese.ClassQuery import*
import time

from datetime import datetime

class FormBaixaRecebe(QDialog):
    def __init__(self,nota=None,FunçaoBusca=None):
        QWidget.__init__(self)

        self.ui = Ui_FormBaixaReceber()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()
        self.ui.dt_datapamento.setDateTime(QtCore.QDateTime.currentDateTime())
        self.PuxaNotareceber(nota)
        #corrigir tamanho tabela
        self.ui.tab_BaixaReceber.setColumnWidth(0, 80)#id
        self.ui.tab_BaixaReceber.setColumnWidth(1, 80)#id
        self.ui.tab_BaixaReceber.setColumnWidth(3, 80)#desconto
        self.ui.tab_BaixaReceber.setColumnWidth(4, 120)#valo nominal
        self.ui.tab_BaixaReceber.setColumnWidth(5, 120)#valo total
        self.ui.tab_BaixaReceber.setColumnWidth(6, 120)#data emissao
        #baixa Nota
        self.ui.bt_receber.clicked.connect(self.funBaixaNotaSelecionada)
        #carrega plano pagemnto
        documento=db.pega_dados(''' select descricao from tb_tipodocumento ''')
        documetos = [item[0] for item in documento]
        self.ui.cb_tipoDocumento.addItems(documetos)
        #da descontro na tela
        self.ui.Db_desconto.editingFinished.connect(self.DescontonoReceber)
        self.busca=FunçaoBusca
    def PuxaNotareceber(self,nota=None):
        self.ui.tab_BaixaReceber.setRowCount(0)
        run=0
        for i in nota:
            banco=db.pega_dados(f'''select *from tb_receber where documento='{i}' ''')
            for linha, row_data in enumerate (banco):
                self.ui.tab_BaixaReceber.insertRow(linha)
                
                real=(f'{("R$ {:.2f}".format(row_data[4]))}')
                calcular=row_data[4]
                self.ui.tab_BaixaReceber.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(row_data[0])))#id
                self.ui.tab_BaixaReceber.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(row_data[1])))#nota
                self.ui.tab_BaixaReceber.setItem(linha, 8, QtWidgets.QTableWidgetItem(str(row_data[2])))#documento
                self.ui.tab_BaixaReceber.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(row_data[3])))
                
                self.ui.tab_BaixaReceber.setItem(linha, 3, QtWidgets.QTableWidgetItem('R$ 0.00'))
                self.ui.tab_BaixaReceber.setItem(linha, 4, QtWidgets.QTableWidgetItem(str(real)))
                self.ui.tab_BaixaReceber.setItem(linha, 5, QtWidgets.QTableWidgetItem(str(real)))
                self.ui.tab_BaixaReceber.setItem(linha, 6, QtWidgets.QTableWidgetItem(str(row_data[6])))
                self.ui.tab_BaixaReceber.setItem(linha, 7, QtWidgets.QTableWidgetItem(f'{str(self.ui.dt_datapamento.text())}'))#dataemissao
                
                run+=float(calcular)
            
                self.ui.db_valorTotalparcela.setValue(run)
                self.ui.db_valortotal.setValue(run)
                self.verficadata(row_data[6])
    def verficadata(self,datatt=None):
        import datetime
        #verficar data
        for i in range(self.ui.tab_BaixaReceber.rowCount()):
            data=(self.ui.tab_BaixaReceber.item(i, 6).text())
            dados=datetime.datetime.strptime(f"{str(datatt)}","%d/%m/%Y")   
            hoje = datetime.datetime.today()  # Data atual
         
            if dados<=hoje:
                datavencimento = QTableWidgetItem(str(data))
                text_color = QColor(255, 0, 0)
                datavencimento.setForeground(text_color)
                self.ui.tab_BaixaReceber.setItem(i, 6, datavencimento)#dataemissao
                icon = QIcon(':/novo/telainicial/calendario.png')
                datavencimento.setIcon(icon)
            else:
                datavencimento1 = QTableWidgetItem(str(data))
                icon = QIcon(':/novo/telainicial/calendario.png')
                datavencimento1.setIcon(icon)
                text_color = QColor(0, 0, 0)
                datavencimento1.setForeground(text_color)
                self.ui.tab_BaixaReceber.setItem(i, 6, datavencimento1)#dataemissao      
                               
    def funBaixaNotaSelecionada(self):#baixa nota pega id e compara se exite e da baixa

        self.baixa=Mensagem.confirmacao(self,"Deseja","Deseja Baixa Nota?")
        if self.baixa:
            for i in range(self.ui.tab_BaixaReceber.rowCount()):
                id=(self.ui.tab_BaixaReceber.item(i, 0).text())
                numeronota=(self.ui.tab_BaixaReceber.item(i, 1).text())
                nomeCliente=(self.ui.tab_BaixaReceber.item(i, 2).text())
                desconto=(str(self.ui.tab_BaixaReceber.item(i, 3).text()).replace('%','').replace('R','').replace('$',''))
                valornominal=(str(self.ui.tab_BaixaReceber.item(i, 4).text()).replace('R','').replace('$',''))
                valor=(str(self.ui.tab_BaixaReceber.item(i, 5).text()).replace('R','').replace('$',''))
                dataEmissao=(str(self.ui.tab_BaixaReceber.item(i, 6).text()))
                documento=(str(self.ui.tab_BaixaReceber.item(i, 8).text()))
                #inserir caixa
                db.adicionar(f''' insert into tb_caixa (nota,nome,valortotal,tipodocumento,data_emissao,cd_doc) 
                values('{numeronota}','{nomeCliente}/rebidos','{valor}','{str(self.ui.cb_tipoDocumento.currentText())}','{self.ui.dt_datapamento.text()}','R')''')
                selecionacodCliente=db.pega_dados(f'''select codcliente from tb_receber where id='{id}' ''')
                #inserir recebidos
                db.adicionar(f''' insert into tb_recebidos (id,nota,documento,codcliente,nome,valornominal,desconto,valortotal,data_emissao) 
                values('{id}','{numeronota}','{documento}','{selecionacodCliente[0][0]}','{nomeCliente}','{valornominal}','{desconto}','{valor}','{dataEmissao}')''')
                
                db.apaga(f''' DELETE FROM tb_receber where id='{id}' ''')#deleta ou inserir
                self.close()
                self.busca()
    def DescontonoReceber(self):
        percentual_desconto = self.ui.Db_desconto.value()
        run=0
        for i in range(self.ui.tab_BaixaReceber.rowCount()):
            if float(percentual_desconto)<1.00:
                nominal=(str(self.ui.tab_BaixaReceber.item(i, 4).text()))
                self.ui.tab_BaixaReceber.setItem(i, 5, QtWidgets.QTableWidgetItem(str(nominal)))
                self.ui.db_valortotal.setValue(self.ui.db_valorTotalparcela.value())
            else:
                
                
                valor=(str(self.ui.tab_BaixaReceber.item(i, 4).text()).replace('R','').replace('$',''))
                valor_original = float(valor)
                valor_com_desconto = valor_original - (valor_original * (percentual_desconto / 100))
                self.ui.tab_BaixaReceber.setItem(i, 3, QtWidgets.QTableWidgetItem(f'{str(percentual_desconto)}%'))
                self.ui.tab_BaixaReceber.setItem(i, 5, QtWidgets.QTableWidgetItem(f'{("R$ {:.2f}".format(valor_com_desconto))}'))
                
                valorDesconto=(str(self.ui.tab_BaixaReceber.item(i, 5).text()).replace('R','').replace('$',''))
                run+=float(valorDesconto)#somar valores
            
                self.ui.db_valortotal.setValue(run)