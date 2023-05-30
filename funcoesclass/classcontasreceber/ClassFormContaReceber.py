from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, QObject, pyqtSignal, QMetaObject
import sys
from funcoesclass.databese.ClassQuery import*
#importa incluirClinetes
from funcoesclass.FormCode.FormContaReceber import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
#import baixa
from funcoesclass.classcontasreceber.ClassFormBaixaReceber import*
from datetime import datetime
from datetime import timedelta
from funcoesclass.ClassFormPrimaria.ClassFormControleioClientes import*
#importa PArcelas Clientes
from funcoesclass.ClassFormPrimaria.ClassFormIncluirPArcelas import*
#conta recebidas
from funcoesclass.classcontasreceber.ClassContaRecebidas import*
from funcoesclass.classcontasreceber.classgeralreceber import*
class FormContasReceber(QDialog):#essa tela puxa os quarto
    def __init__(self,x=None):
        QWidget.__init__(self)
      
        self.ui = Ui_FormContaReceber()
        self.ui.setupUi(self)
        #colocar tamano na tela 
        self.ui.widget_6.setMinimumSize(int(x)-41,0)
        self.Colunastab()
        #ocultar incluir parcelas
        self.ui.wb_incluirParcelas.close()
        self.ui.bt_Altera.close()
        self.ui.progressBar.close()
        #ADICIONAR ACTION TABLE
        self.ui.actioncaixa.triggered.connect(self.FunBaixaNotas)
    

        ##############################
        self.ui.bt_receber.clicked.connect(self.FunBaixaNotas)
        self.ui.tx_buscarCliente.returnPressed.connect(self.FunBuscaClienteContareceber)
        #verifa se apenas numero
        self.ui.tx_Numeronota.setValidator(QDoubleValidator(0.99999,99999999.9999999,2))
        self.ui.tx_codPArcelas.setValidator(QDoubleValidator(0.99999,99999999.9999999,2))
        self.ui.tx_quantPArcelas.setValidator(QDoubleValidator(0.99999,99999999.9999999,2))
        #incluir Receber
        self.ui.bt_incluirReceber.clicked.connect(lambda:self.ui.wb_incluirParcelas.show())
        #possiciona tela
        self.ui.wb_incluirParcelas.move(self.mapToGlobal(self.rect().center() - self.ui.wb_incluirParcelas.rect().center()))
        #salvar parcelas
        self.ui.bt_SalvarPagamento.clicked.connect(self.incluirParcelas)
        #pega data
        self.ui.dt_emissao.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        #selecionar cliente
        self.ui.tx_codCliente.mouseDoubleClickEvent =self.FunSelecionarClientes
        #selecionar PArcelas
        self.ui.tx_codPArcelas.mouseDoubleClickEvent=self.SelecionaPArcelas
        
        #fechar tela
        self.ui.bt_sairlancamento.clicked.connect(self.CloseFecharWiget)
        #contas Recebidas 
        #self.ui.bt_recebidos.clicked.connect(lambda:Recebidos(self.ui.lb_CodigoClinte.text()).exec_())
        
        #thread complete
        self.Threadcomplete()
        #
        self.ui.tabWidget.currentChanged.connect(self.qtabwidget_currentchanged)
        #baixanota
        self.ui.tab_receber.doubleClicked.connect(self.marcaNotasREceber)
        self.actionIncrement = QtWidgets.QShortcut(QtGui.QKeySequence("Space"), self.ui.tab_receber)
        self.actionIncrement.activated.connect(self.marcaNotasREceber)
        self.ui.bt_marcatodos.clicked.connect(self.marcatodasnota)
       

    def marcatodasnota(self):
        valor=[]
        run=0
        for quant in range(self.ui.tab_receber.rowCount()):
          
            self.ui.tab_receber.setItem(quant, 0,QTableWidgetItem(str("s")))
            self.ui.tab_receber.item(quant,0).setTextAlignment(Qt.AlignCenter)
            self.ui.tab_receber.selectRow(quant)
            time.sleep(0.5)  
            QApplication.processEvents()#carrega time 
            for i in range(0,self.ui.tab_receber.columnCount()):
                
                self.ui.tab_receber.item(quant,i).setBackground(QtGui.QColor(85, 170, 255))

            if self.ui.tab_receber.item(quant, 0).text()=='s': 
                valor.append(self.ui.tab_receber.item(quant, 5).text().replace('R','').replace('$',''))   
            else:
                self.ui.tx_valorTotalparcela.setValue(0) 
        for t in valor:
            run+=float(t)
            self.ui.tx_valorTotalparcela.setValue(run)         
    def marcaNotasREceber(self):#marca pra da baixa
        linha=self.ui.tab_receber.currentRow()
        if self.ui.tab_receber.item(linha,0).text()=='n':
            self.ui.tab_receber.setItem(linha, 0,QTableWidgetItem(str("s")))
            for i in range(0,self.ui.tab_receber.columnCount()):
                self.ui.tab_receber.item(linha,i).setBackground(QtGui.QColor(85, 170, 255))
             
        else:
            self.ui.tab_receber.setItem(linha, 0,QTableWidgetItem(str("n"))) 
            for i in range(0,self.ui.tab_receber.columnCount()):
                self.ui.tab_receber.item(linha,i).setBackground(QtGui.QColor(255, 255, 255))
        valor=[] 
        run = 0
        for i in range(self.ui.tab_receber.rowCount()):
            self.ui.tab_receber.item(i,0).setTextAlignment(Qt.AlignCenter)  
            if self.ui.tab_receber.item(i, 0).text()=='s': 
                valor.append(self.ui.tab_receber.item(i, 5).text().replace('R','').replace('$',''))   
            else:
                self.ui.tx_valorTotalparcela.setValue(0) 
        for t in valor:
            run+=float(t)
            self.ui.tx_valorTotalparcela.setValue(run) 
    def FunAlinhaTableWidget(self,linha=None):
        self.ui.tab_receber.item(linha,0).setTextAlignment(Qt.AlignCenter)  
        self.ui.tab_receber.item(linha,2).setTextAlignment(Qt.AlignCenter)  
    def Colunastab(self):
        #coluna table itens
        self.ui.tab_receber.setColumnWidth(0, 10)#chebox
        self.ui.tab_receber.setColumnWidth(1, 50)
        self.ui.tab_receber.setColumnWidth(2, 50)
        self.ui.tab_receber.setColumnWidth(4, 300)
        self.ui.tab_receber.setColumnWidth(5, 150)
        self.ui.tab_receber.setColumnWidth(6, 150)
        
        self.ui.tb_geral.setColumnWidth(0, 80)
        self.ui.tb_geral.setColumnWidth(1, 80)
        self.ui.tb_geral.setColumnWidth(2, 80)
        self.ui.tb_geral.setColumnWidth(3, 500)
        self.ui.tb_geral.setColumnWidth(4, 150)
        self.ui.tb_geral.setColumnWidth(5, 150)
    def qtabwidget_currentchanged(self, index):
        current_tab_text =self.ui.tabWidget.tabText(index)
        if current_tab_text=='geral':
            #ver geral receber
            GeralReceber(self)
            self.ui.tab_receber.setRowCount(0)
            self.limparCampos()
        if current_tab_text=='recebidos':
            Recebidos.CarregaRecebidosClientes(self,self.ui.lb_CodigoClinte.text())
            self.ui.tab_receber.setRowCount(0)
            self.ui.tb_geral.setRowCount(0)
    @pyqtSlot(str)
    def Threadcomplete(self):
        #VISUALIZA CLIENTES
        lista=db.pega_dados('''select nome from tb_clientes ''')
        lista1=[]
        for i in lista:
            lista1.append(str(i[0]).upper())
            
        completer = QCompleter(lista1, self.ui.tx_buscarCliente)
        completer.setCaseSensitivity(0)
        self.ui.tx_buscarCliente.setCompleter(completer)  
     
    def CloseFecharWiget(self):
        self.confirma=Mensagem.confirmacao(self,'Deseja','Deseja Fechar Tela')
        if self.confirma:
            self.ui.wb_incluirParcelas.close()
    def incluirParcelas(self):
        numeroDanota=db.pega_dados(""" select nota FROM tb_receber ORDER BY nota DESC LIMIT 1""") 
        if not numeroDanota:
            self.ui.tx_Numeronota.setText(str(1))
        else:
            self.ui.tx_Numeronota.setText(str(numeroDanota[0][0]+1))
        self.incluir=Mensagem.confirmacao(self,'Deseja','Deseja incluir parcelas!?')
        
        try:
            nota=self.ui.tx_Numeronota.text()
            codCliente=self.ui.tx_codCliente.text()
            descCliente=self.ui.tx_descricaocliente.text()
            quantPArcelas=int(self.ui.tx_quantPArcelas.text())
            dataemisssao=self.ui.dt_emissao.text()
            valortotalPArcela=self.ui.tx_incluirValorpagamento.value()
            
            valortotal=float(valortotalPArcela)/quantPArcelas
        except:error
        if self.incluir:
            while True:
                if nota=='':
                    Mensagem.mensagem(self,"Campo","campo Nota vazio")
                    self.ui.tx_Numeronota.setFocus() 
                
                    break 
                if codCliente=='':
                    Mensagem.mensagem(self,"Campo","campo codigo cliente vazio")
                    self.ui.tx_codCliente.setFocus() 
                    break   
            
                if self.ui.tx_codPArcelas.text()=='':
                    Mensagem.mensagem(self,"Campo","campo codigo parcelas vazio")
                    self.ui.tx_codPArcelas.setFocus() 
                    break 
                
                if float(valortotalPArcela)<1.00:
                    Mensagem.mensagem(self,"Campo","campo valor zerado")
                    self.ui.tx_incluirValorpagamento.setFocus() 
                    break       
                else:
                    import datetime
                    from datetime import timedelta
                    dados = datetime.datetime.strptime(f"{dataemisssao}","%d/%m/%Y")
                    run=0
                    for i in range(0,quantPArcelas):#fracionar datas
                        dados=dados + timedelta(days=30)
                        datafinal=dados.strftime("%d/%m/%Y")
                        run+=1
                        db.adicionar(f'''insert into tb_receber(nota,documento,nome,valortotal,parcelas,data_emissao,data_vencimento,codcliente)
                                    values ('{nota}','{nota}/{run}','{descCliente}','{valortotal}','{quantPArcelas}X','{dataemisssao}','{datafinal}','{str(codCliente)}')''')
                    self.ui.wb_incluirParcelas.close()
                    self.ui.tx_buscarCliente.setText(str(descCliente))    
                    self.FunBuscaClienteContareceber()
                    self.ui.tx_buscarCliente.clear()  
                    self.limparCampos()
                    
                break
    
    def SelecionaPArcelas(self,event):
        self.parcelas=FormIncluirParcelas()
        self.parcelas.ui.frame_3.close()
        self.parcelas.ui.frame.close()
        def selecioPArcelastext():
            lista=[]
            for i in range(0,4):
                seleciona=self.parcelas.ui.tab_PArcelas.selectedItems()[i].text()
                lista.append(seleciona)
            
            self.ui.tx_codPArcelas.setText(str(lista[0]))
            self.ui.tx_descricaoparcelas.setText(str(lista[1]))
            self.ui.tx_quantPArcelas.setText(str(lista[2]))
            self.parcelas.close()

        self.parcelas.ui.tab_PArcelas.doubleClicked.connect(selecioPArcelastext)
        self.parcelas.exec_()
    def FunSelecionarClientes(self,event):#essa funçao importa cadastro cliente pra dentro da venda
        self.FormCadastroClientes=FormCadastroClientes('S')
        def SelecionaCliente():
            try:
                sel_cliente=self.FormCadastroClientes.ui.tableWidget_usuario_2.selectedItems()
                banco=db.pega_dados(f'''select * from tb_clientes where id='{sel_cliente[0].text()}' ''')
                self.ui.tx_codCliente.setText(str(banco[0][0]))        
                self.ui.tx_descricaocliente.setText(str(banco[0][1]))    
                self.FormCadastroClientes.hide()
                
            except:
                error
        self.FormCadastroClientes.ui.tableWidget_usuario_2.doubleClicked.connect(SelecionaCliente)
        self.FormCadastroClientes.ui.bt_novo.hide()
        self.FormCadastroClientes.exec_() 
                  
    def FunBuscaClienteContareceber(self):
        self.line_busca_cliente=self.ui.tx_buscarCliente.text()
        dadosid =db.pega_dados(f"SELECT *FROM tb_clientes WHERE nome LIKE'%{self.line_busca_cliente}%'")
        
        if not dadosid:
            pass
        else:
            self.ui.lb_CodigoClinte.setText(str(dadosid[0][0]))
            self.ui.lb_NomeCliente.setText(str(dadosid[0][1]))
        if self.line_busca_cliente=='':
            self.limparCampos()
        else:
            try:
                dados =db.pega_dados(f"SELECT *FROM tb_receber WHERE codcliente='{dadosid[0][0]}'")
          
                if not dados:
                    self.ui.tab_receber.setRowCount(0)
                    pass
                    #Mensagem.mensagem_erro(self,"erro",'nao a contas a receber') 
                    
                else:
                    self.ui.actionMARCA_TODAS_RECEBER.setDisabled(False)  
                    self.ui.actionDESMARCAR_TODAS.setDisabled(False)
                    self.ui.actioncaixa.setDisabled(False)
                    self.ui.tab_receber.setRowCount(0)
                    self.ui.tx_valorTotalparcela.setValue(0) 
                    run=0 
                    for linha, row_data in enumerate (dados):
                        self.ui.tab_receber.insertRow(linha)
                        self.ui.tab_receber.setItem(linha, 0, QTableWidgetItem(str('n')))
                        self.ui.tab_receber.item(linha,0).setTextAlignment(Qt.AlignCenter)  
                        
                        real=(f'{("R$ {:.2f}".format(row_data[4]))}')
                        self.ui.tab_receber.setItem(linha, 1, QTableWidgetItem(str(row_data[0])))
                        self.ui.tab_receber.setItem(linha, 2, QTableWidgetItem(str(row_data[1])))
                        self.ui.tab_receber.setItem(linha, 3, QTableWidgetItem(str(row_data[2])))
                        self.ui.tab_receber.setItem(linha, 4, QTableWidgetItem(str(row_data[3])))
                        self.ui.tab_receber.setItem(linha, 5, QTableWidgetItem(str(real)))
                        self.ui.tab_receber.setItem(linha, 6, QTableWidgetItem(str(real)))
                        #data emmissao
                        dataemisao=QTableWidgetItem(str(row_data[6]))
                        text_color = QColor(38, 113, 55)
                        dataemisao.setForeground(text_color)
                        icon = QIcon(':/novo/telainicial/calendario.png')
                        dataemisao.setIcon(icon)
                        
                        self.ui.tab_receber.setItem(linha, 7, dataemisao)
                        #datavencimento
                        datavencimento=QTableWidgetItem(str(row_data[7]))
                        text_color = QColor(0, 0, 0)
                        datavencimento.setForeground(text_color)
                        icon = QIcon(':/novo/telainicial/calendario.png')
                        datavencimento.setIcon(icon)
                        self.ui.tab_receber.setItem(linha, 8,datavencimento)
        
                        
                        self.ui.tab_receber.setItem(linha, 9, QTableWidgetItem(str('0')))
                        self.VerificaDataVencida(linha,row_data[7],row_data[6])
                    for row in range(len(dados)):
                            
                            '''self.checkbox = QCheckBox()
                            #self.checkbox.setCheckState(Qt.Unchecked)
                            self.ui.tab_receber.setCellWidget(row, 0, self.checkbox)                  # <----
                            self.checkbox.clicked.connect(self.FunSelecionarContaReceber)'''
            except:error
    
    def VerificaDataVencida(self,linha,vencimento,emissao):
        data_vencimento = datetime.datetime.strptime(f"{vencimento}","%d/%m/%Y").date()
        hoje = datetime.date.today()

        if data_vencimento < hoje:
            item=QTableWidgetItem(str(vencimento))
            text_color = QColor(255, 0, 0)
            item.setForeground(text_color)
            icon = QIcon(':/novo/telainicial/calendario.png')
            item.setIcon(icon)
            self.ui.tab_receber.setItem(linha, 8,item)
            
            vencimentodata = datetime.datetime.strptime(f'{vencimento}',"%d/%m/%Y").date()
            emissaodata = datetime.datetime.strptime(f'{emissao}',"%d/%m/%Y").date()
            data=((vencimentodata)-emissaodata)
            d = data.days
            vencimentos=QTableWidgetItem(str(int(d)).replace('-',''))
            text_color = QColor(255, 0, 0)
            vencimentos.setForeground(text_color)
            icon = QIcon(':/novo/telainicial/calendario.png')
            vencimentos.setIcon(icon)
            self.ui.tab_receber.setItem(linha, 9,vencimentos) 
        else:
            pass 
        
        #datas
        
    def FunSelecionarContaReceber(self):
        self.ui.progressBar.show()
        run=0
        carregar=0
        valor = []
        for i in range(self.ui.tab_receber.rowCount()):
            if self.ui.tab_receber.cellWidget(i, 0).isChecked():
                self.ui.progressBar.setMaximum(i)
                valor.append(self.ui.tab_receber.item(i, 5).text().replace('R','').replace('$',''))
                carregar+=i
                time.sleep(0.1)
                self.ui.progressBar.setValue(carregar)   
            else:
                self.ui.tx_valorTotalparcela.setValue(0)
        run = 0
        for i in valor:
            run+=float(i)
            self.ui.tx_valorTotalparcela.setValue(run) 
        
       
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.close()

    
    def FunBaixaNotas(self):
            checked_list = []
            for i in range(self.ui.tab_receber.rowCount()):
                if self.ui.tab_receber.item(i, 0).text()=='s': 
                #if self.ui.tab_receber.cellWidget(i, 0).isChecked():
                    checked_list.append(self.ui.tab_receber.item(i, 3).text())        
            lista=[]
            for i in checked_list:
                lista.append(i)
        
            if len(lista)==0:
                pass
            else:
                self.FormBaixaRecebe=FormBaixaRecebe(lista,self.FunBuscaClienteContareceber)
                self.FormBaixaRecebe.exec_()
        
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