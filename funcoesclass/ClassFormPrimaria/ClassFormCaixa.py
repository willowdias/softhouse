from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.databese.ClassQuery import*
from datetime import timedelta
from datetime import datetime
import datetime
from funcoesclass.FormCode.FormCaixa import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
class Formcaixa(QDialog):#essa tela puxa os quarto
    def __init__(self,x=None,y=None):
        QWidget.__init__(self)
      
        self.ui = Ui_FormCaixa()
        self.ui.setupUi(self)
        #self.showFullScreen()
        self.ui.widget_2.setMinimumWidth(x)
        self.ui.widget.setMinimumWidth(x-45)
        self.ui.widget.setMinimumHeight(y-45)
        self.mensagem=Mensagem()
        self.ui.tab_caixa.setColumnWidth(0, 80)
        self.ui.tab_caixa.setColumnWidth(1, 80)
        self.ui.tab_caixa.setColumnWidth(2, 400)
        self.ui.tab_caixa.setColumnWidth(6, 10)#credito ou debito
        self.ui.fundoincluir.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.fundoincluir.setWindowFlags(Qt.Window | Qt.FramelessWindowHint|Qt.Drawer)
        
        
        
        self.ui.fundoincluir.move(self.mapToGlobal(self.rect().center() - self.ui.fundoincluir.rect().center()))
        self.ui.widgetFundovisutalitem.move(self.mapToGlobal(self.rect().center() - self.ui.widgetFundovisutalitem.rect().center()))
       
        #close itens
        self.ui.widgetFundovisutalitem.close()
        self.ui.fundoincluir.close()
        #botao close
        self.ui.bt_Altera.close()


        #ver item
        self.ui.bt_veritemVenda.clicked.connect(self.FunVisualisarITemVenda)
        #apagar
        self.ui.bt_apagarcaixa.clicked.connect(self.FunApagarNota)
        self.ui.bt_filtradoc.clicked.connect(lambda:self.FunPuxaDadosPorDAta('S'))
        self.ui.data_final.editingFinished.connect(lambda:self.FunPuxaDadosPorDAta("N"))
        data_atual = datetime.date.today()
        # converte a data em uma string formatada
        data_texto = data_atual.strftime("%d/%m/%Y")
        self.ui.data_emisao.setText(str(data_texto))
        self.ui.data_final.setText(str(data_texto))
        self.ui.dt_incluirdata.setText(str(data_texto))
        self.FunPuxaDadosPorDAta('S')
        #table wid
        self.ui.tab_caixa.addAction(self.ui.actionaltera_lan_amento)
        self.ui.tab_caixa.addAction(self.ui.actionincluir_lan_amento)
        #incluir pagamento
        self.ui.bt_incluircaixa.clicked.connect(self.incluirpaga)
        #
        self.ui.tab_caixa.doubleClicked.connect(lambda:self.SelecionaAltera('selecionar'))
        #self.ui.actionaltera_lan_amento.triggered.connect(self.SelecionaAltera)
        #self.ui.bt_alteracaixa.clicked.connect(self.SelecionaAltera)
        #
       
        #carrega
        form = db.pega_dados(f'''SELECT descricao FROM tb_tipodocumento  ''')
        formapagamento = [item[0] for item in form]
        self.ui.cb_incluirTipodocumento.addItems(formapagamento)
        #closete tesa
        self.ui.bt_sairlancamento.clicked.connect(self.CloseWidget)
        self.ui.bt_sairITens.clicked.connect(self.CloseWidget)
        
        self.ui.bt_Altera.clicked.connect(self.salvarAlteracao)
        self.ui.bt_SalvarPagamento.clicked.connect(self.incluir)
      
        
    def CloseWidget(self):
        self.confirma=Mensagem.confirmacao(self,'fechar','Deseja Fecha Tela')
        if self.confirma:
            self.ui.fundoincluir.close()
            self.ui.widgetFundovisutalitem.close()
            self.ui.widget.setDisabled(False)
            self.CleaTx()
            self.ui.bt_Altera.close()
            self.ui.bt_SalvarPagamento.close()
    def incluirpaga(self):
        self.ui.bt_Altera.close()
        self.ui.bt_SalvarPagamento.show()
        self.ui.widget.setDisabled(True)
        self.ui.tx_incluirDocumento.setDisabled(False)
        self.ui.label_5.setText("incluir lançamentos")
        self.ui.fundoincluir.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.ui.fundoincluir.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.fundoincluir.show()
        
    def incluir(self):

            documento=str(self.ui.tx_incluirDocumento.text())
            data=self.ui.dt_incluirdata.text()
            descricao=self.ui.tx_incluirdescricao.text()
            tipodoc=self.ui.cb_incluirTipodocumento.currentText()
            valor=float(self.ui.tx_incluirValorpagamento.value())
            
            if self.ui.rd_credito.isChecked():
                credito_debito='c'
            if self.ui.rd_debito.isChecked():
                credito_debito='d'
                
            bancocaixa=db.pega_dados(f'''select nota from tb_caixa where nota='{documento}' ''')
          
            if bancocaixa:
                Mensagem.mensagem(self,'ja existe','numero ja existe')
            else:
                
                while True:
                    if documento=="":
                        self.mensagem.ui.lbShowMessagem.setText("CAMPO DOCUMENTO VAZIO")
                        self.mensagem.exec_() 
                        self.ui.tx_incluirDocumento.setFocus()
                        break
                    if descricao=="":
                        self.mensagem.ui.lbShowMessagem.setText("CAMPO DECRIÇAO VAZIO")
                        self.mensagem.exec_() 
                        self.ui.tx_incluirdescricao.setFocus()
                        break 
                    if valor<1:
                        self.mensagem.ui.lbShowMessagem.setText("CAMPO VALOR IGUAL ZERO 0")
                        self.mensagem.exec_() 
                        self.ui.tx_incluirValorpagamento.setFocus()
                        break  
                    else:
                        db.adicionar(f'''insert into tb_caixa (nota,nome,valortotal,tipodocumento,
                                                data_emissao,cd_doc)values('{documento}','{descricao}','{valor}',
                                                '{tipodoc}','{data}','{credito_debito}') ''')
                        self.FunPuxaDadosPorDAta('S')  
                        self.ui.fundoincluir.close()    
                        self.ui.widget.setDisabled(False)
                        self.CleaTx()
                    break
    def SelecionaAltera(self,param):
        if param=='selecionar':
            self.ui.bt_Altera.show()
            self.ui.bt_SalvarPagamento.close()
            self.ui.widget.setDisabled(True)
            self.ui.tx_incluirDocumento.setDisabled(True)
            self.ui.label_5.setText("alterar lançamentos")
            
            pega=self.ui.tab_caixa.selectedItems()[1].text()
            id=self.ui.tab_caixa.selectedItems()[0].text()
            self.ui.tx_incluirDocumento.setText(pega)
            banco=db.pega_dados(f''' select *from tb_caixa where nota ='{pega}' and id='{id}' ''')
            
            self.ui.tx_IDText.setText(str(banco[0][0]))
            self.ui.tx_incluirdescricao.setText(banco[0][2])
            self.ui.tx_incluirValorpagamento.setValue(float(banco[0][3]))
            self.ui.cb_incluirTipodocumento.setCurrentText(banco[0][4])
            #data=datetime.datetime.strptime(f"{banco[0][5]}","%d/%m/%Y") 
            self.ui.dt_incluirdata.setText(str(banco[0][5]))
            if banco[0][6]=='c':
               self.ui.rd_credito.setChecked(True)
            else:
                self.ui.rd_debito.setChecked(True)    
            self.ui.fundoincluir.show()
            
    def salvarAlteracao(self):
    
        documento=str(self.ui.tx_incluirDocumento.text())
        data=self.ui.dt_incluirdata.text()
        descricao=self.ui.tx_incluirdescricao.text()
        tipodoc=self.ui.cb_incluirTipodocumento.currentText()
        valor=float(self.ui.tx_incluirValorpagamento.value())  
       
       
  
                
        while True:
                if documento=="":
                    self.mensagem.ui.lbShowMessagem.setText("CAMPO DOCUMENTO VAZIO")
                    self.mensagem.exec_() 
                    self.ui.tx_incluirDocumento.setFocus()
                    break
                if descricao=="":
                    self.mensagem.ui.lbShowMessagem.setText("CAMPO DECRIÇAO VAZIO")
                    self.mensagem.exec_() 
                    self.ui.tx_incluirdescricao.setFocus()
                    break 
                if valor<1:
                    self.mensagem.ui.lbShowMessagem.setText("CAMPO VALOR IGUAL ZERO 0")
                    self.mensagem.exec_() 
                    self.ui.tx_incluirValorpagamento.setFocus()
                    break  
                else:
                  
                    if self.ui.rd_credito.isChecked():
                        credito_debito='c'
                    if self.ui.rd_debito.isChecked():
                        credito_debito='d'
                    db.update(f'''update tb_caixa set nota='{documento}',nome='{descricao}',valortotal='{valor}',
                                                tipodocumento='{tipodoc}',data_emissao='{data}',cd_doc='{credito_debito}' where nota='{documento}' and id='{self.ui.tx_IDText.text()}' ''')
                    self.FunPuxaDadosPorDAta('S')
                    self.ui.fundoincluir.hide()
                    self.ui.widget.setDisabled(False)        
                    self.CleaTx()
                    break
    def CleaTx(self):
        self.ui.tx_incluirDocumento.clear()
        self.ui.tx_incluirdescricao.clear()
        self.ui.tx_incluirValorpagamento.setValue(0)
 
    def FunPuxaDadosPorDAta(self,Datadia=None):#essa funçao selecionar data do caixa
        self.ui.db_valorTotal.setValue(0)
        self.ui.db_valoreDebito.setValue(0)
        if Datadia=='S':
            self.data=self.ui.data_emisao.text()
            bancocaixa=db.pega_dados(f'''select *from tb_caixa where data_emissao like'%{self.data}%' ''')

        if Datadia=='N':
            self.emissao=self.ui.data_emisao.text()
            self.datafinal=self.ui.data_final.text()
            bancocaixa=db.pega_dados(f'''SELECT * FROM tb_caixa WHERE data_emissao BETWEEN '{self.emissao}' AND '{self.datafinal}' <= CURRENT_DATE ''')
            print(bancocaixa)
        self.ui.tab_caixa.setRowCount(0)
        for linha, row_data in enumerate (bancocaixa):
            
            real = row_data[3]
            a = "{:.2f}".format(real)
            self.ui.tab_caixa.insertRow(linha)
            self.ui.tab_caixa.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(row_data[0])))
            self.ui.tab_caixa.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(row_data[1])))
            self.ui.tab_caixa.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(row_data[2])))
            self.ui.tab_caixa.setItem(linha, 3, QtWidgets.QTableWidgetItem(str(f'R$ {a}')))
            self.ui.tab_caixa.setItem(linha, 4, QtWidgets.QTableWidgetItem(str(row_data[4])))
            
            dataitem = QTableWidgetItem(str(row_data[5]))
            icon = QIcon(':/novo/telainicial/calendario.png')
            dataitem.setIcon(icon)

            self.ui.tab_caixa.setItem(linha, 5,dataitem )
            
            if str(row_data[6])=='d':
                creditoodebito = QTableWidgetItem(str(row_data[6]))
                valor = QTableWidgetItem(str(f'R$ {a}'))
                text_color = QColor(255, 0, 0)
                valor.setForeground(text_color)
                creditoodebito.setForeground(text_color)
                
                self.ui.tab_caixa.setItem(linha, 3,valor)
                self.ui.tab_caixa.setItem(linha, 6, creditoodebito)#credito/debito
          
            else:
                creditoodebito = QTableWidgetItem(str(row_data[6]))
                valor = QTableWidgetItem(str(f'R$ {a}'))
                text_color = QColor(54, 162, 7)
                valor.setForeground(text_color)
                creditoodebito.setForeground(text_color)
                self.ui.tab_caixa.setItem(linha, 3,valor)
                self.ui.tab_caixa.setItem(linha, 6, creditoodebito)#credito/debito
            self.ui.tab_caixa.selectRow(self.ui.tab_caixa.rowCount()-1)
        debito=0
        crtido=0
        for credito in range(self.ui.tab_caixa.rowCount()):
            cr=(self.ui.tab_caixa.item(credito, 6).text())
            valortotal=(str(self.ui.tab_caixa.item(credito, 3).text().replace('R','').replace('$','')))
            
            if cr=='d':#
                debito += float(valortotal)
                self.ui.db_valoreDebito.setValue(debito)
            else:
                crtido += float(valortotal)
                self.ui.db_valorTotal.setValue(crtido)
    def FunApagarNota(self):
        try:
            
            itens=self.ui.tab_caixa.selectedItems()[0].text()
            self.confirma=Mensagem.confirmacao(self,'Apagar',"Deseja Apaga Nota")
            if self.confirma:
                db.apaga(f'''delete from tb_caixa where id='{itens}' ''')
                self.FunPuxaDadosPorDAta('S')
        except:error
    def FunVisualisarITemVenda(self):
        self.ui.widgetFundovisutalitem.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.ui.widgetFundovisutalitem.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
 
        self.ui.widget.setDisabled(True)
        try:
            
            itens=self.ui.tab_caixa.selectedItems()[1].text()
        
            banco=db.pega_dados(f'''select * from orca where nota='{itens}' ''')
            #headerH = ['codigo barra' , ' descriçao']
            #self.pos.setHorizontalHeaderLabels(headerH)
            self.ui.widgetFundovisutalitem.showMaximized()
            self.ui.tb_Caixa_itens.setRowCount(0)
            linha=0
            for linha,row in enumerate (banco):
                
                self.ui.tb_Caixa_itens.insertRow(linha)
                self.ui.tb_Caixa_itens.setItem(linha, 0, QTableWidgetItem(str(row[2])))
                self.ui.tb_Caixa_itens.setItem(linha, 1, QTableWidgetItem(str(row[3])))
                linha=linha+1
                self.ui.labelQuant.setText(f'Quantidade itens : {str(linha)}') 
   
 
        except:error