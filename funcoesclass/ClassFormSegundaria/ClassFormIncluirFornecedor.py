from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *#IMPORA MENSAGEM BOX
from funcoesclass.databese.ClassQuery import*
import time

from funcoesclass.FormCode.FormIncluirFornecedores import*
class FormIncluirFornecedor(QDialog):
    def __init__(self,desativa=None,id=None,classe=None):
        QWidget.__init__(self)

        self.ui = Ui_ct_FormFornecedor()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.bt_alterafornecedo.close()
        #salva Fonercedor
        self.ui.bt_Salvar.clicked.connect(self.Fun_AdicionarFornecedo)
        #buscar cep
        self.ui.bt_BuscaCep.clicked.connect(self.FunConsultaCep)
        #buscar fonecedor
        self.ui.tx_BuscarFonecedor.returnPressed.connect(self.FunBuscaFonecedorTab)
        self.ui.bt_Fornecedor.clicked.connect(self.FunBuscaFonecedorTab)
        self.ui.Wd_CadastroFonecedor.close()
        self.ui.bt_novo.clicked.connect(self.ui.Wd_CadastroFonecedor.show)
        self.ui.bt_sairaWbCadastro.clicked.connect(self.ui.Wd_CadastroFonecedor.hide)
        #excluir
        self.ui.bt_apagar.clicked.connect(self.FunExcluirFoncedor)
        #aletera
        self.ui.bt_altera.clicked.connect(self.funSelecionaFonecedorEditar)
      
        #closee
        self.ui.bt_closer.clicked.connect(self.closeTela)
        self.showFullScreen()
    def closeTela(self):
        self.confirma=Mensagem.confirmacao(None,'Deseja','Deseja Fechar')
        if self.confirma:
            self.close()
    def FunConsultaCep(self):
        self.ConsultaCep=self.ui.tx_Cep.text().replace('-','')
        BancoConsultacep=db.pega_dados(f'''SELECT * FROM Municipio where Cep='{self.ConsultaCep}' ''')
        if not BancoConsultacep:
            Mensagem.mensagem_erro(self,"Erro",f"CEP {self.ConsultaCep} NAO ESTAR CADASTRADO")
        else:
           self.ui.tx_Cidade.setText(str(BancoConsultacep[0][2]))
           self.ui.tx_Estado.setText(str(BancoConsultacep[0][3]))

    def Fun_AdicionarFornecedo(self):
        self.nomeFantasia=self.ui.tx_NomeFantasia.text()
        self.RazaoSocial=self.ui.tx_RazaoSocial.text()
        self.cnpj=self.ui.tx_cnpj.text()
        self.ieIscricao=self.ui.tx_InscEstadual.text()
        self.telefone=self.ui.tx_Telefone.text()
        self.email=self.ui.tx_Email.text()
        self.obs=self.ui.tx_Obs.text()
        self.cep=self.ui.tx_Cep.text()
        self.endereco=self.ui.tx_Endereco.text()
        self.numeroresidencia=self.ui.tx_Numero.text()
        self.bairro=self.ui.tx_Bairro.text()
        self.cidade=self.ui.tx_Cidade.text()
        self.estado=self.ui.tx_Estado.text()
        
        removecaracteria="!@#$1234567890.,-+*/_''"
        for remove in range(0,len(removecaracteria)):
            
            self.nomeFantasia=self.nomeFantasia.replace(removecaracteria[remove],'')
            self.RazaoSocial=self.RazaoSocial.replace(removecaracteria[remove],'')
        removecateriasseg="()-!@#.,-+*/_"

        for remove in range(0,len(removecateriasseg)):
            self.telefone=self.telefone.replace(removecateriasseg[remove],'')
            self.cep=self.cep.replace(removecateriasseg[remove],'')
            self.ieIscricao=self.ieIscricao.replace(removecateriasseg[remove],'')
            self.cnpj=self.cnpj.replace(removecateriasseg[remove],'')
        while True:
            if self.nomeFantasia=="":
                Mensagem.mensagem(self,"Erro","Nome Fantasia Em branco")
                self.ui.tx_NomeFantasia.setFocus()
                break
            if self.RazaoSocial=="":
                Mensagem.mensagem(self,"Erro","Nome razao Social Em branco")
                self.ui.tx_NomeFantasia.setFocus()
                break
            else:
                db.adicionar(f''' INSERT INTO tb_fornecedor(nome_fantasia,razao_social,cnpj,
                inscricao,telefone,email,obs,cep,endereco,numeroresidencia,bairro,cidade,
                estado)
                values('{self.nomeFantasia}','{self.RazaoSocial}','{self.cnpj}','{self.ieIscricao}','{self.telefone}',
                '{self.email}','{self.obs}','{self.cep}','{self.endereco}','{self.numeroresidencia}','{self.bairro}',
                '{self.cidade}','{self.estado}')  ''')
                Mensagem.mensagem(self,"Cadastro","Cadastro Com Sucesso")
                
            break
    def FunBuscaFonecedorTab(self):
        self.BuscaFonecedor=self.ui.tx_BuscarFonecedor.text()
        dados =db.pega_dados(f"SELECT *FROM tb_fornecedor WHERE nome_fantasia LIKE'%{self.BuscaFonecedor}%'")
        if not dados:
            Mensagem.mensagem_erro(self,"ERRO",'FORNCEDOR NAO EXISTE') 
            self.ui.tab_Fornecedor.setRowCount(0)
        else:  
            self.ui.tab_Fornecedor.setRowCount(0)
                    
            for linha, row_data in enumerate (dados): 
                self.ui.tab_Fornecedor.insertRow(linha)
                self.ui.tab_Fornecedor.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(row_data[0])))#id
                self.ui.tab_Fornecedor.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(row_data[1])))#nome
                self.ui.tab_Fornecedor.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(row_data[3])))#cnpj
                self.ui.tab_Fornecedor.setItem(linha, 3, QtWidgets.QTableWidgetItem(str(row_data[4])))#inscriçao estadual

    def FunExcluirFoncedor(self):
        try:
            self.delataForncededor=Mensagem.confirmacao(self,"Apagar","Deseja Apagar Fornecedor")
            if self.delataForncededor:
                selecionaFonecedorexcluir=self.ui.tab_Fornecedor.selectedItems()
                db.apaga(f'''DELETE FROM tb_fornecedor where id='{selecionaFonecedorexcluir[0].text()}' ''')    
                Mensagem.mensagem(self,'Forncedor','Forncedor Apago Com Sucesso') 
                
                self.FunBuscaFonecedorTab()   
        except:error

    def funSelecionaFonecedorEditar(self):
        self.ui.bt_alterafornecedo.show()
        self.ui.bt_Salvar.close()
        try:
            selecionaFonecedor=self.ui.tab_Fornecedor.selectedItems()
            bancoFonecedor=db.pega_dados(f'''SELECT * FROM tb_fornecedor where id='{selecionaFonecedor[0].text()}' ''')    
            self.ui.Wd_CadastroFonecedor.show()
        except:error
        self.ui.tx_Id.setText(str(bancoFonecedor[0][0]))
        self.ui.tx_NomeFantasia.setText(str(bancoFonecedor[0][1]))
        self.ui.tx_RazaoSocial.setText(str(bancoFonecedor[0][2]))
        self.ui.tx_cnpj.setText(str(bancoFonecedor[0][3]))
        self.ui.tx_InscEstadual.setText(str(bancoFonecedor[0][4]))
        self.ui.tx_Telefone.setText(str(bancoFonecedor[0][5]))
        self.ui.tx_Email.setText(str(bancoFonecedor[0][6]))
        self.ui.tx_Obs.setText(str(bancoFonecedor[0][7]))
        self.ui.tx_Cep.setText(str(bancoFonecedor[0][8]))
        self.ui.tx_Cidade.setText(str(bancoFonecedor[0][12]))
        self.ui.tx_Estado.setText(str(bancoFonecedor[0][13]))
        self.ui.tx_Bairro.setText(str(bancoFonecedor[0][11]))
        self.ui.tx_Endereco.setText(str(bancoFonecedor[0][10]))
        self.ui.tx_Numero.setText(str(bancoFonecedor[0][11]))
    
        
    def FunClearLineeditFonecedor(self):#essa funçao limpa line edite cadastro fornecedores
        self.ui.tx_Id.clear()
        self.ui.tx_NomeFantasia.clear()
        self.ui.tx_cnpj.clear()
        self.ui.tx_InscEstadual.clear()
        self.ui.tx_Telefone.clear()
        self.ui.tx_Email.clear()
        self.ui.tx_Obs.clear()
        self.ui.tx_Cep.clear()
        self.ui.tx_Cidade.clear()
        self.ui.tx_Estado.clear()
        self.ui.tx_Bairro.clear()
        self.ui.tx_Endereco.clear()
        self.ui.tx_Numero.clear()