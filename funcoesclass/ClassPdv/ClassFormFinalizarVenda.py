from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *
from funcoesclass.FormCode.FormFinalizaVenda import * 
from funcoesclass.databese.ClassQuery import*
from datetime import timedelta, date
import time
from datetime import timedelta
from datetime import datetime
import datetime
from  funcoesclass.ClassPdv.ClassVenda import*
class FinalizaVenda(QDialog):
    def __init__(self,ValorTotal=None,codCliente=None,nomecliente=None,Data=None,
                 hora=None,inserirITemorca=None,LimparTela=None,numeroORca=None,imprimirnfce=None):
        QWidget.__init__(self)

        self.ui = Ui_FormFinalizarVenda()
        self.ui.setupUi(self)
        #close pedido
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        #self.setWindowFlags(Qt.Tool)
        self.showFullScreen()
        self.ui.widget_4.close()
        #importa fora e tipo documento
        sis.tipdocumento(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|Qt.Drawer)
        self.ui.bt_cancelar.clicked.connect(self.fechar)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.tx_valortotal.setValue(ValorTotal)
        self.ui.tx_subTotal.setValue(ValorTotal)
        self.codCliente=codCliente
        self.nomeCliente=nomecliente
        self.data=Data
        print(self.data)
        self.hora=hora
        self.ui.bt_finalizar.clicked.connect(lambda:self.ui.widget_4.show())
        #limpara tablea wideg
        self.limpar=LimparTela
        #inserir itens orca
        self.InsertitemOrca=inserirITemorca
        #numeronota 
        self.Numeronota=numeroORca
       #imprimir nfce 
        self.impriminfce=imprimirnfce
        self.ui.bt_finalizaped.clicked.connect(self.FunFinalizaVenda)
    def fechar(self):
        self.confirma=Mensagem.confirmacao(self, "Deseja ", "Deseja Fechar Sistema")
        if self.confirma:
           self.close() 
    def FunFinalizaVenda(self):
        self.ui.widget_4.close()
        if self.ui.rd_nfce.isChecked():
            self.impriminfce()
        if self.ui.rd_pedido.isChecked():
            pass
        self.adicionarVenda=Mensagem.confirmacao(self,"DEseja finaliza venda",f"DEseja finaliza venda")
        if self.adicionarVenda:
            resultado = db.pega_dados(f'''SELECT *FROM tb_planopagamento where descricao='{self.ui.cb_FormaPagamento.currentText()}' ''')
            if resultado[0][1]==1:
                self.FunVendaAvista(self.nomeCliente)
              
            else:
                if int(self.codCliente)<1:#essa oppçao verifica se  cliente esta preenchido
                    Mensagem.mensagem(self,'Plano','forma parcelamento selecioanda Campo cliente vazio')
                else:
                    self.VendaParcelada(resultado[0][3])
            
    def VendaParcelada(self,resultado):
        if self.Numeronota.text()=='':
            parcela=int(resultado)
            dados=datetime.datetime.strptime(f"{self.data}","%d/%m/%Y")
                        
            parcela=int(resultado)
            dados=datetime.datetime.strptime(f"{self.data}","%d/%m/%Y")
                        
            list_date=[]
            valorTotalVenda=self.ui.tx_subTotal.value()
            valorparcelas=(valorTotalVenda/(parcela))
            bancoorca=db.pega_dados(""" select NOTA FROM orcas ORDER BY NOTA DESC LIMIT 1""")
            self.nota=1
            for orca in bancoorca:
                if orca[0]<1:
                    self.nota=orca[0]
                else:
                    self.nota=orca[0]+1           
            run=0
            for i in range(0,parcela):#fracionar datas
                dados=dados + timedelta(days=30)
                list_date.append(dados)
            for item in list_date:
                run+=1#aferi parcela
                datafinal=item.strftime("%d/%m/%Y")
                            
                            
                db.adicionar(f'''insert into tb_receber(nota,documento,nome,valortotal,parcelas,data_emissao,data_vencimento,codcliente)
                            values ('{self.nota}','{self.nota}/{run}','{self.nomeCliente}','{valorparcelas}','{parcela}X','{self.data}','{datafinal}','{str(self.codCliente)}')''')
                
                self.removeNotaTabelaOrcamento(self.nota)  
  

      
            db.adicionar(f''' insert into orcas (nota,descricao,valortotal,data_emissao,data_final)values
            ('{self.nota}','{self.nomeCliente}','{self.ui.tx_subTotal.value()}','{self.data}','{self.data}')  ''')
                
            db.adicionar(f''' update   orca set finalizado='S' where  nota='{self.nota}' ''')
            self.InsertitemOrca(self.nota) 
            self.limpar()  
            self.close()
        else:
            self.removeNotaTabelaOrcamento(self.Numeronota.text())
            db.apaga(f'''delete from orca where nota='{self.Numeronota.text()}' ''')
            self.InsertitemOrca(self.Numeronota.text()) 
            self.Numeronota.setText('')
            self.limpar()
            self.close()
    def FunVendaAvista(self,nome):
        #inserir orcas apos a venda
        if self.Numeronota.text()=='':
            
            bancoorca=db.pega_dados(""" select NOTA FROM orcas ORDER BY NOTA DESC LIMIT 1""")
            self.nota=1
            for orca in bancoorca:
                if orca[0]<1:
                    self.nota=orca[0]
                else:
                    self.nota=orca[0]+1
            self.Nomecliente=nome
            self.nomecaixa=''
            if nome=='':
                db.adicionar(f''' insert into orcas (nota,descricao,valortotal,data_emissao,data_final,Finalizar)values
                ('{self.nota}','{'consumidor final'}','{self.ui.tx_subTotal.value()}','{self.data}','{self.data}','S')  ''')   
                self.nomecaixa='consumidor final'
            else:
                db.adicionar(f''' insert into orcas (nota,descricao,valortotal,data_emissao,data_final,Finalizar)values
                ('{self.nota}','{self.Nomecliente}','{self.ui.tx_subTotal.value()}','{self.data}','{self.data}','S')  ''')   
                self.nomecaixa=self.Nomecliente
            db.adicionar(f''' update   orca set finalizado='S' where  nota='{self.nota}' ''')
            db.adicionar(f'''insert into tb_caixa (nota,nome,valortotal,tipodocumento,data_emissao,cd_doc) values
                         ('{self.nota}','{self.nomecaixa}','{self.ui.tx_subTotal.value()}',
                         '{self.ui.cb_FormaPagamento.currentText()}','{self.data}','c')''')
            self.InsertitemOrca(self.nota) 
            self.removeNotaTabelaOrcamento(self.nota)  
            self.limpar()
            self.close()
        else:
            #essa funçao verifica se nota estava em orçamento enviado
            self.removeNotaTabelaOrcamento(self.Numeronota.text())
            db.apaga(f'''delete from orca where nota='{self.Numeronota.text()}' ''')
            db.adicionar(f''' update orca set Finalizado='S' where nota='{self.Numeronota.text()}' ''')#colocar finalizado orcas item
            self.InsertitemOrca(self.Numeronota.text()) 
            self.Numeronota.setText('')
            self.limpar()
            self.close()
       
        
       
    def removeNotaTabelaOrcamento(self,nota):#quando finaliza remove a venda do orcçamento
        try:

            db.adicionar(f''' update orcas set Finalizar='S' where nota='{nota}' ''')#colocar como finalizado orçamento
            
            db.adicionar(f''' update orca set Finalizado='S' where nota='{nota}' ''')#colocar finalizado orcas item
        except:error
   