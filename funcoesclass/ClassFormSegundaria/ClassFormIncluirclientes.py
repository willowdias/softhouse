from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.FormCode.FormIncluiClientes import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *#IMPORA MENSAGEM BOX
from funcoesclass.databese.ClassQuery import*
import time
from datetime import datetime
import datetime
import os

class FormIncluirClientes(QDialog):
    def __init__(self,desativa=None,id=None,linBuscarCliente=None,FuncaoBuscaCliente=None):
        QWidget.__init__(self)

        self.ui = Ui_Cadastro_Clientes()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.mensagem=Mensagem()
        self.showFullScreen()
        
       
        self.ui.widget.move(self.mapToGlobal(self.rect().center() - self.ui.widget.rect().center()))#centralizafundo
        self.ui.Cidades.move(self.mapToGlobal(self.rect().center() - self.ui.Cidades.rect().center()))#centralizafundo
        self.ui.cadastro_cidades.move(self.mapToGlobal(self.rect().center() - self.ui.cadastro_cidades.rect().center()))#centralizafundo
        #puxa id da opçao altera
        self.ui.cadastro_cidades.close()#fechar cadastro_cidades
        self.ui.Cidades.close()#fechar cadastro_cidades
        #add action
        self.ui.tx_cod_ibge.addAction(self.ui.actionbusca_cep, QLineEdit.TrailingPosition)
        self.ui.actionbusca_cep.triggered.connect(lambda:self.ui.Cidades.show())

        self.ui.tableWidget_2.doubleClicked.connect(self.Fun_selecionar_cidade)
        #selecionar foto coloca label
        self.ui.bt_selecionar_foto.clicked.connect(self.Fun_Add_foto)
        #verifica id do cliente
        self.id=id
        #line Buscar Cliente
        self.txLineEditBuscaCliente=linBuscarCliente
        self.BuscaCliente=FuncaoBuscaCliente
        #essa funçao valida botao virifica se ele vai inserir ou fazer update informaçoes
        self.desativa=desativa
        if self.desativa=="alterar":
            self.ui.bt_Salvar.clicked.connect(self.Fun_altera_cliente)
            self.BuscaClienteEdita(self.id)
        else:
            codicliente=db.pega_dados(""" select id FROM tb_clientes ORDER BY id DESC LIMIT 1""")
            self.ui.tx_codigoCliente.setText(str(codicliente[0][0]+1))
            self.ui.bt_Salvar.clicked.connect(self.Fun_Adiciona_cliente)   #botao salvar Cliente
            self.ui.dt_nascimento.setDateTime(QtCore.QDateTime.currentDateTime())
            self.ui.dat_cadastro.setDateTime(QtCore.QDateTime.currentDateTime())
            self.ui.dt_compra.setDateTime(QtCore.QDateTime.currentDateTime())
        #busca cidade
        self.ui.line_busca_cidades.returnPressed.connect(self.fun_buscar_cidades)
        #CORRIGIR TAMANHO CIDADE
        self.arruma_colunar_tablewideg()
        #puxa tela Cadastro Fornecedor
        #Fehjcar tela
        self.ui.bt_sair.clicked.connect(self.CloseTela)
        #fechar Widget
        self.ui.bt_cancelarCadastrocidade.clicked.connect(self.CloseWidget)
        self.ui.bt_SairTelaCidade.clicked.connect(self.CloseWidgetcidade)
        #veirfica juridico ou fisico
       
        self.ui.comb_FisicoJuridico.activated[str].connect(self.VerificarAlteraJf)
        
        # AO PRESSIONAR A TECLA "F10" CONECTAR COM A FUNÇÃO "abrir_janela2"
        #QShortcut(Qt.Key_F10, self.lineEdit,  self.abrir_janela2, context=Qt.WidgetShortcut)
        #ativa abas
        self.ui.chefotos.clicked.connect(self.AtivaTabWiobjeto)
        self.ui.cheadicionais.clicked.connect(self.AtivaTabWiobjeto)
        self.ui.cheobs.clicked.connect(self.AtivaTabWiobjeto)
        self.ui.checontatos.clicked.connect(self.AtivaTabWiobjeto)
        #remove objeto tabela
        for i in range(5):
            self.ui.tab_fichaCliente.removeTab(0)
            self.ui.tab_fichaCliente.addTab(self.ui.dados, ('dados basico'))
        #armazema objeto
        self.listatab=[]   
        self.ui.frame_2.mousePressEvent = self.mousePressEvent
        self.ui.frame_2.mouseMoveEvent = self.mouseMoveEvent
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            x = event.globalX()
            y = event.globalY()
            x_w = self.offset.x()
            y_w = self.offset.y()
            self.ui.widget.move(x - x_w, y - y_w)

    def AtivaTabWiobjeto(self):#essa funçao consegue verifica abasa aberta
        clickedButton = self.sender()
        selecionar = str(clickedButton.text()).lower()
        if selecionar=='fotos':
            mob=self.ui.fotos
            nome='fotos'
        if selecionar=='adicionais':
            mob=self.ui.adicionais
            nome='adicionais'
        if selecionar=='obs':
            mob=self.ui.observacao
            nome='OBSERVAÇÃO'
        if selecionar=='contatos':
            mob=self.ui.contatos
            nome='contatos'
        if selecionar:    
            if selecionar not in self.listatab: 
                self.ui.tab_fichaCliente.addTab(mob, f"{nome}")  
                #self.ui.tab_fichaCliente.setCurrentWidget(mob)  
                self.listatab.append(selecionar) 
            else:
                for a, b in zip(range(1,self.ui.tab_fichaCliente.count()),self.listatab):
                    if b==selecionar:
                        self.ui.tab_fichaCliente.removeTab(a)
                        self.listatab.remove(b)    
    def CloseTela(self):
        self.confirma=Mensagem.confirmacao(self,'Sair Tela',"Deseja Sair Tela")
        if self.confirma:
            self.close()
    def CloseWidget(self):
        self.confirma=Mensagem.confirmacao(self,'Sair Tela',"Deseja Sair Tela")
        if self.confirma:
            self.ui.cadastro_cidades.close()
    def CloseWidgetcidade(self):
        self.confirma=Mensagem.confirmacao(self,'Sair Tela',"Deseja Sair Tela")
        if self.confirma:
            self.ui.Cidades.close()        
    def BuscaClienteEdita(self,id):#buscaCleinteNo Banco
        banco=db.pega_dados(f"""SELECT * FROM tb_clientes where id='{id}' """)
        self.ui.tx_NomeFantasia.setText(str(banco[0][1]))#nome
        self.ui.tx_RazaoSocial.setText(str(banco[0][2])) #razao social
        self.ui.tx_cnpj.setText(str(banco[0][3]))#cpf/cpj
        self.ui.tx_InscEstadual.setText(str(banco[0][4]))# inscriçao
        self.ui.tx_Celular.setText(str(banco[0][5]))# celular
        self.ui.tx_Telefone.setText(str(banco[0][6]))# telefone
        self.ui.tx_Email.setText(str(banco[0][7]))# email
        self.ui.tx_Obs.setPlainText(str(banco[0][8]))# obs
        self.ui.tx_cod_ibge.setText(str(banco[0][9]))# cod ibge
        self.ui.tx_Cep.setText(str(banco[0][10]))# cep
        self.ui.tx_Cidade.setText(str(banco[0][11]))#cidades
        self.ui.tx_Estado.setText(str(banco[0][12]))# estado
        self.ui.tx_Endereco.setText(str(banco[0][13]))# endereço
        self.ui.tx_Bairro.setText(str(banco[0][14]))# bairro
        self.ui.tx_Numero.setText(str(banco[0][15]))# cep
        #chama foto da pagina
        self.SelecionaImagenPasta(str(banco[0][0]))
        #data
        dataEmissao=datetime.datetime.strptime(f"{banco[0][16]}","%d/%m/%Y")
        self.ui.dat_cadastro.setDate(dataEmissao)
        
        
           
    def SelecionaImagenPasta(self,idImg):
        for nome_arquivo in os.listdir(f'{os.getcwd()}/config/FotosClientes'):
            if f'{idImg}' in nome_arquivo:#verifica se img na pasta
                
                pixmap = QtGui.QPixmap(f'{os.getcwd()}/config/FotosClientes/{nome_arquivo}') # Setup pixmap with the provided image        
                self.pixmap = pixmap.scaled(200,200, QtCore.Qt.KeepAspectRatio)
                self.ui.lb_fotoClientes.setPixmap( self.pixmap) # Set the pixmap onto the label
                self.ui.lb_fotoClientes.setAlignment(QtCore.Qt.AlignCenter)    
                
    def arruma_colunar_tablewideg(self):
    
        self.ui.tableWidget_2.horizontalHeader().setVisible(True)
        self.ui.tableWidget_2.setColumnWidth(0,120)#id
        self.ui.tableWidget_2.setColumnWidth(1,220)#nome
        self.ui.tableWidget_2.setColumnWidth(2,100)#cep
    @pyqtSlot()       
    def VerificarAlteraJf(self):
        rb=self.ui.comb_FisicoJuridico.currentText()
      
        if rb=='fisico':
           
            self.ui.lb_nome.setText("NOME*")
            self.ui.lb_sobrenome.setText("SOBRENOME*")
            self.ui.lb_rg.setText("RG*")
            self.ui.lb_cpfcnpj.setText("cpf*")
            self.ui.tx_cnpj.setMaxLength(14)
            self.ui.tx_cnpj.setInputMask("999.999.999-99;_")
           
        elif rb=='juridico':
     
            self.ui.tx_cnpj.setMaxLength(18)
            self.ui.lb_cpfcnpj.setText("cnpj*")
            self.ui.lb_nome.setText("razao social*")
            self.ui.lb_sobrenome.setText("nome fantasia*")
            self.ui.lb_rg.setText("inscriçao estadual*")
            self.ui.tx_cnpj.setInputMask("99.999.999/9999-99;_")
             

    
    @pyqtSlot()
    def Fun_close_botaocliente(self):
        self.ui.bt_Salvar.close()
        self.ui.bt_Voltar.close()
        self.ui.line_busca_cidades.setFocus()
        self.ui.bt__volta_cadastro.show()
    @pyqtSlot()
    def Fun_selecionar_cidade(self):#selecionar cidade para cliente
        try:
            self.seleciona=self.ui.tableWidget_2.selectedItems()
            self.ui.tx_cod_ibge.setText(str(self.seleciona[0].text()))
            self.ui.tx_Cidade.setText(str(self.seleciona[1].text()))
            self.ui.tx_Cep.setText(str(self.seleciona[2].text()))
            self.ui.tx_Estado.setText(str(self.seleciona[3].text()))
            
            
            self.ui.line_busca_cidades.clear()
            self.ui.Cidades.close()
            self.ui.tableWidget_2.setRowCount(0)
        except:
            print("")
    
    def fun_buscar_cidades(self):#busca cidade por buscar
      
        self.line_buscar= self.ui.line_busca_cidades.text()
            
        dados =db.pega_dados(f"SELECT *FROM Municipio WHERE Nome LIKE'%{self.line_buscar}%'")
           
        self.ui.tableWidget_2.setRowCount(0)
        for row_number,row_data in enumerate(dados):
            self.ui.tableWidget_2.insertRow(row_number)
            self.ui.tableWidget_2.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data[0])))#IBGE
            self.ui.tableWidget_2.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data[2])))#NOME
            self.ui.tableWidget_2.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(row_data[1])))#CEP
            self.ui.tableWidget_2.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(row_data[3])))
    def Fun_Add_foto(self):#adicionar foto LAbel
        
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", ":", "Image Files (*.png *.jpg *jpeg *.bmp);;All Files (*)") # Ask for file
        if fileName: # If the user gives a fileimagem, _ = QFileDialog.getOpenFileName(
                pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image        
                self.pixmap = pixmap.scaled(int(200), int(200), QtCore.Qt.KeepAspectRatio)
                self.ui.lb_fotoClientes.setPixmap( self.pixmap) # Set the pixmap onto the label
                #self.ui.label_fotos_clientes.setScaledContents(True)
                self.ui.lb_fotoClientes.setAlignment(QtCore.Qt.AlignCenter) 
        
       
    def Fun_altera_cliente(self):
        self.nome=self.ui.tx_NomeFantasia.text()
        self.sobrenome=self.ui.tx_RazaoSocial.text()
        self.cpf_cnpj=self.ui.tx_cnpj.text()
        self.rg_iscr=self.ui.tx_InscEstadual.text()
        self.telefone=self.ui.tx_Telefone.text()
        self.email=self.ui.tx_Email.text()
        self.obs=self.ui.tx_Obs.placeholderText()
        self.cod_ibge=self.ui.tx_cod_ibge.text()
        self.celula=self.ui.tx_Celular.text().replace(' ','')
        self.cep=self.ui.tx_Cep.text()
        self.cidade=self.ui.tx_Cidade.text()
        self.Uf=self.ui.tx_Estado.text()
        self.endereco=self.ui.tx_Endereco.text()
        self.bairro=self.ui.tx_Bairro.text()
        self.numeresidencia=self.ui.tx_Numero.text()
        self.DataEmissao=self.ui.dat_cadastro.text()
         ###########
        removeCaracteria = "!@#$1234567890.,-+*[]()''"#remove caracterias
        for i in range(0,len(removeCaracteria)):
            self.nome =self.nome.replace(removeCaracteria[i],"")
            self.sobrenome =self.sobrenome.replace(removeCaracteria[i],"")
        ####
        removecarecteria=".-()"#remove caracterias
        for remove in range(0,len(removecarecteria)):
            self.cpf_cnpj=self.cpf_cnpj.replace(removecarecteria[remove],"")
            self.rg_iscr=self.rg_iscr.replace(removecarecteria[remove],"")
            self.celula=self.celula.replace(removecarecteria[remove],"")
            self.telefone=self.telefone.replace(removecarecteria[remove],"")
            self.cep=self.cep.replace(removecarecteria[remove],"")
        
        while True:
            if self.nome=="":
             
                self.mensagem.ui.lbShowMessagem.setText("CAMPO NOME EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_NomeFantasia.setFocus()
                break
            if self.sobrenome=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO NOME EM SOBRENOME  \n RAZAO SOCIAL EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_RazaoSocial.setFocus()
                break
            if self.cpf_cnpj=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO CPF \n CNPJ EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_cnpj.setFocus()
                break
            if self.cod_ibge=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO COD-IBGE  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_cod_ibge.setFocus()
                self.ui.Cidades.show()
                break
            if self.cep=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO CEP  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_Cep.setFocus()
                break        
            if self.cidade=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO CIDADE  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_Cidade.setFocus()
                break
            if self.Uf=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO ESTADO  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_Estado.setFocus()
                break
            if self.endereco=="":   
                self.mensagem.ui.lbShowMessagem.setText("CAMPO ENDEREÇO  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_Endereco.setFocus()
                break
            if self.bairro=="":
                self.mensagem.ui.lbShowMessagem.setText( f"CAMPO BAIRRO  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_Bairro.setFocus()
                break
            if self.numeresidencia=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO NUMERO RESIDENCIA  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_Numero.setFocus()
                break
            else:    
                db.adicionar(f"""update   tb_clientes set   nome='{self.nome}',sobrenome='{self.sobrenome}',cpf_cnpj='{self.cpf_cnpj}',rg_inscricao='{self.rg_iscr}',
                celular='{self.celula}',telefone='{self.telefone}',email='{self.email}',obs='{self.obs}',cod_ibge='{self.cod_ibge}',cep='{self.cep}',cidade='{self.cidade}',
                estado='{self.Uf}',endereco='{self.endereco}',bairro='{self.bairro}',numeroresidencia='{self.numeresidencia}' ,data_emissao='{self.DataEmissao}' where id='{self.id}' """)
                try:
                    self.pixmap.save(f"config/FotosClientes/{self.id}.png")
                except:error
                Mensagem.mensagem(self,"CADASTRO","ALTERADO  COM SUCESSO")
                self.close()
                self.txLineEditBuscaCliente.setText(str(self.nome))
                self.txLineEditBuscaCliente.setFocus()
                self.BuscaCliente()
                alterareceber=db.pega_dados(f'''select * from tb_receber where codcliente='{self.id}' ''')
                for i in alterareceber:
                    db.adicionar(f''' update tb_receber set nome='{self.nome}' where id='{i[0]}' ''')
            break
        
    def Fun_Adiciona_cliente(self):
        self.nome=self.ui.tx_NomeFantasia.text()
        self.sobrenome=self.ui.tx_RazaoSocial.text()
        self.cpf_cnpj=self.ui.tx_cnpj.text()
        self.rg_iscr=self.ui.tx_InscEstadual.text().replace('e','')
        self.celula=self.ui.tx_Celular.text()
        self.telefone=self.ui.tx_Telefone.text()
        self.email=self.ui.tx_Email.text()
        self.obs=self.ui.tx_Obs.placeholderText()
        self.cod_ibge=self.ui.tx_cod_ibge.text()
        self.cep=self.ui.tx_Cep.text()
        self.cidade=self.ui.tx_Cidade.text()
        self.Uf=self.ui.tx_Estado.text()
        self.endereco=self.ui.tx_Endereco.text()
        self.bairro=self.ui.tx_Bairro.text()
        self.numeresidencia=self.ui.tx_Numero.text()
        self.DataEmissao=self.ui.dat_cadastro.text()
        ###########
        removeCaracteria = "!@#$1234567890.,-+()*''"#remove caracterias
        for i in range(0,len(removeCaracteria)):
            self.nome =self.nome.replace(removeCaracteria[i],"")
            self.sobrenome =self.sobrenome.replace(removeCaracteria[i],"")
        ####
        removecarecteria=".-()"#remove caracterias
        for remove in range(0,len(removecarecteria)):
            self.cpf_cnpj=self.cpf_cnpj.replace(removecarecteria[remove],"")
            self.rg_iscr=self.rg_iscr.replace(removecarecteria[remove],"")
            self.celula=self.celula.replace(removecarecteria[remove],"")
            self.telefone=self.telefone.replace(removecarecteria[remove],"")
            self.cep=self.cep.replace(removecarecteria[remove],"")
        
        while True:
            if self.nome=="":
             
                self.mensagem.ui.lbShowMessagem.setText("CAMPO NOME EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_NomeFantasia.setFocus()
                break
            if self.sobrenome=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO NOME EM SOBRENOME  \n RAZAO SOCIAL EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_RazaoSocial.setFocus()
                break
            if self.cpf_cnpj=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO CPF \n CNPJ EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_cnpj.setFocus()
                break
            if self.cod_ibge=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO COD-IBGE  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_cod_ibge.setFocus()
                self.ui.Cidades.show()
                break
            if self.cep=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO CEP  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_Cep.setFocus()
                break        
            if self.cidade=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO CIDADE  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_Cidade.setFocus()
                break
            if self.Uf=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO ESTADO  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_Estado.setFocus()
                break
            if self.endereco=="":   
                self.mensagem.ui.lbShowMessagem.setText("CAMPO ENDEREÇO  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_Endereco.setFocus()
                break
            if self.bairro=="":
                self.mensagem.ui.lbShowMessagem.setText( f"CAMPO BAIRRO  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_Bairro.setFocus()
                break
            if self.numeresidencia=="":
                self.mensagem.ui.lbShowMessagem.setText(f"CAMPO NUMERO RESIDENCIA  EM BRANCO")
                self.mensagem.exec_() 
                self.ui.tx_Numero.setFocus()
                break
                
            
            else:
                db.adicionar(f"""INSERT INTO tb_clientes(nome,sobrenome,cpf_cnpj,rg_inscricao,celular,
                telefone,email,obs,cod_ibge,cep,cidade,estado,endereco,bairro,numeroresidencia,data_emissao) 
                values('{self.nome}','{self.sobrenome}','{self.cpf_cnpj}','{self.rg_iscr}','{self.celula}','{self.telefone}',
                '{self.email}','{self.obs}','{self.cod_ibge}','{self.cep}','{self.cidade}','{self.Uf}','{self.endereco}',
                '{self.bairro}','{self.numeresidencia}','{self.DataEmissao}')""")
                self.mensagem.ui.lbShowMessagem.setText("CADASTRO COM SUCESSO")
                self.mensagem.exec_() 
                self.txLineEditBuscaCliente.setText(str(self.nome))
                self.txLineEditBuscaCliente.setFocus()
                self.BuscaCliente()
                self.close()
                try:
                    bancofoto=db.pega_dados(""" select id FROM tb_clientes ORDER BY id DESC LIMIT 1""")
                    self.pixmap.save(f"config/FotosClientes/{bancofoto[0][0]}.png")
                except:KeyError
             
            break

   
    