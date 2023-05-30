from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.FormCode.FormIncluirFuncionario import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *#IMPORA MENSAGEM BOX
from funcoesclass.databese.ClassQuery import*
from datetime import timedelta
from datetime import datetime
import datetime

class IncluirFuncionario(QDialog):
    def __init__(self,nome=None,OBjetoFuncao=None,Botao=None,CodigoFuncionario=None):
        QWidget.__init__(self)

        self.ui = Ui_FormIncluirFuncionario()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()
        self.ui.tx_Cpf.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.ui.tx_codigoFuncionario.setText(str(CodigoFuncionario))
        self.ui.dt_DataAniversario.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.dt_DataCadastro.setDateTime(QtCore.QDateTime.currentDateTime())
        #carregar login usuario
        login=db.pega_dados(''' select nome from usuario ''')
        list_of_strings = [item[0] for item in login]
        self.ui.cb_login.addItems(list_of_strings)
        #######
        self.nome=nome
        self.objeto=OBjetoFuncao
        #botao fechar
        self.ui.Bt_Cancelar.clicked.connect(self.FecharTela)
        #opaçao do botao
        if Botao=="novo funcionario":
            self.ui.Bt_Salva.clicked.connect(self.FunIncluirFuncionario)
        elif Botao=="alterar":
            self.ui.Bt_Salva.clicked.connect(self.FunAltera)
            banco=db.pega_dados(f'''select * from tb_funcionario where codigo='{CodigoFuncionario}'  ''')
            for i in banco:
                self.ui.tx_NomeFuncionario.setText(str(i[1]))
                self.ui.tx_Sobrenome.setText(str(i[2]))
                self.ui.tx_Cpf.setText(str(i[3]))
                self.ui.tx_cidade.setText(str(i[4]))
                self.ui.tx_estado.setText(str(i[5]))
                status=str(i[6])
                
                niver=datetime.datetime.strptime(f"{i[7]}","%d/%m/%Y")
                cadastro=datetime.datetime.strptime(f"{i[8]}","%d/%m/%Y")
                self.ui.dt_DataAniversario.setDate(niver)
                self.ui.dt_DataCadastro.setDate(cadastro)
             
                if status=="S":
                    self.ui.rd_Ativo.setChecked(True)
                if status=="N":
                    self.ui.rd_cancelado.setChecked(True)
               
    def FecharTela(self):
        self.fechar=Mensagem.confirmacao(self,"Deseja","Deseja Fechar TEla")
        if self.fechar:
            self.close()
    def FunAltera(self):
   
        nome=self.ui.tx_NomeFuncionario.text().upper()
        sobrenome=self.ui.tx_Sobrenome.text().upper()
        cpf=self.ui.tx_Cpf.text().upper()
        cidade=self.ui.tx_cidade.text().upper()
        estado=self.ui.tx_estado.text().upper()
        dataniversario=self.ui.dt_DataAniversario.text()
        datacadastro=self.ui.dt_DataCadastro.text()
        status="S"
        
        while True:
            if nome=="":
                Mensagem.mensagem(self,'Nome',"nome em branco")
                break
            if self.ui.cb_login.currentText()=="":
                Mensagem.mensagem(self,'login',"login em branco")
                break
            else:
     
                if self.ui.rd_Ativo.isChecked():
                    status=='S'
                elif self.ui.rd_cancelado.isChecked():
                    status='N'
                login=db.pega_dados(f''' select * from usuario where nome='{self.ui.cb_login.currentText()}' ''')
                db.adicionar(f'''update tb_funcionario set nome='{nome}',
                sobronenome='{sobrenome}',cpf='{cpf}',cidade='{cidade}',estado='{estado}',status='{status}'
                ,data_aniversario='{dataniversario}',data_cadastro='{datacadastro}',codigo_usuario='{login[0][0]}',nome_usuario='{login[0][1]}'  where codigo ='{self.ui.tx_codigoFuncionario.text()}' ''')
                Mensagem.mensagem(self,"Funcionario","Funcionario alterado com sucesso")
                self.nome.setText(str(nome))
                self.objeto()
                self.close()  
            break 
    def FunIncluirFuncionario(self):
        nome=self.ui.tx_NomeFuncionario.text().upper().strip(" ")
        sobrenome=self.ui.tx_Sobrenome.text().upper().strip(" ")
        cpf=self.ui.tx_Cpf.text().upper()
        cidade=self.ui.tx_cidade.text().upper()
        estado=self.ui.tx_estado.text().upper()
        dataniversario=self.ui.dt_DataAniversario.text()
        datacadastro=self.ui.dt_DataCadastro.text()

        status="S"
        while True:
            if nome=="":
                Mensagem.mensagem(self,'Nome',"nome em branco")
                break
            if self.ui.cb_login.currentText()=="":
                Mensagem.mensagem(self,'login',"login em branco")
                break    
            else: 
                
                if self.ui.rd_Ativo.isChecked():
                    status=='S'
                elif self.ui.rd_cancelado.isChecked():
                    status='N'
                login=db.pega_dados(f''' select * from usuario where nome='{self.ui.cb_login.currentText()}' ''')
                
                db.adicionar(f''' insert into tb_funcionario (nome,sobronenome,cpf,cidade,
                estado,status,data_aniversario,data_cadastro,codigo_usuario,nome_usuario)
                values('{nome}','{sobrenome}','{cpf}','{cidade}','{estado}','{status}',
                '{dataniversario}','{datacadastro}','{login[0][0]}','{login[0][1]}')''')
                
                Mensagem.mensagem(self,"Funcionario","Funcionario Adicionado com sucesso")
                self.nome.setText(str(nome))
                self.objeto()
                self.close()  
            break 