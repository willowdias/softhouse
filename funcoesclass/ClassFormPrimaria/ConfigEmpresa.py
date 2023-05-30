from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *
from funcoesclass.databese.ClassQuery import*
from funcoesclass.FormCode.FormConfigEmpresa import*
import requests
import base64
import io
import cryptocode
import datetime

class FormConfigParam(QDialog):
    def __init__(self):
        QWidget.__init__(self)

        self.ui = Ui_FormConfigEmpresa()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        #self.setWindowFlags(Qt.Tool)
        self.showFullScreen()
        #margin
        self.ui.lb_logo.setContentsMargins(10, 10, 10, 10)
        #botao fecha teka)
        self.ui.bt_close.clicked.connect(self.closetela)
        #salva
        self.ui.bt_salvar.clicked.connect(self.Configparam)
        form = db.pega_dados(f'''SELECT descricao FROM tb_pais  ''')
        paises = [item[0] for item in form]
        self.ui.comb_pais.addItems(paises)
        self.ui.comb_pais.currentTextChanged.connect(lambda:self.selecionapais('d'))
        self.ui.tx_cod_pais.returnPressed.connect(lambda:self.selecionapais('c'))
        #carregar cidade
        self.ui.tx_cep.returnPressed.connect(self.carregacidade)
        #seleciona logo
        self.ui.lb_logo.mouseDoubleClickEvent =self.selecionalogo
        #carrega cidade sintegra
        self.ui.bt_sintegra.clicked.connect(self.consulta_sintegra)
        #seelecionar empresa
        self.ui.com_tipo_empres.currentTextChanged.connect(self.selecionatipoempresa)
        self.visualisarfoto()
        self.carregaDados()
    
    def visualisarfoto(self):
        try:
            conn = sqlite3.connect('bancodados/database.db')
            cursor = conn.cursor()
            bancofoto=db.pega_dados(""" select id FROM param ORDER BY id DESC LIMIT 1""")
            # Fetch image data from SQLite
            cursor.execute(f"SELECT logo_sistema FROM param WHERE id='{bancofoto[0][0]}'")
            result = cursor.fetchone()
            image_data = result[0]
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            self.ui.lb_logo.setPixmap(pixmap)  
        except:
                error
    def closetela(self):
        confirma=Mensagem.confirmacao(self,"fechar","fechar tela")
        if confirma:
            self.close()
            
            
    def carregaDados(self):
        try:
            pegadados=db.pega_dados(""" select * FROM param """)
            if pegadados[0][1]=='juridica':
                self.ui.com_tipo_empres.setCurrentIndex(1)
            self.ui.tx_cnpj.setText(str(pegadados[0][2]))
            self.ui.tx_rg_ie.setText(str(pegadados[0][3]))
            self.ui.tx_razaosocio.setText(str(pegadados[0][5]))
            self.ui.tx_fantasia.setText(str(pegadados[0][6]))
            self.ui.tx_cep.setText(str(pegadados[0][7]))
            self.ui.tx_endereco.setText(str(pegadados[0][8]))
            self.ui.tx_numero.setText(str(pegadados[0][9]))
            self.ui.tx_complemento.setText(str(pegadados[0][10]))
            self.ui.tx_bairro.setText(str(pegadados[0][11]))
            self.ui.tx_cidade.setText(str(pegadados[0][12]))
            self.ui.tx_estado.setText(str(pegadados[0][13]))
            self.ui.tx_cod_pais.setText(str(pegadados[0][14]))
            #self.ui.comb_pais.setText(str(pegadados[0][15]))
            self.ui.tx_email.setText(str(pegadados[0][16]))
            self.ui.tx_site.setText(str(pegadados[0][17]))
            self.ui.tx_celular.setText(str(pegadados[0][18]))
            self.ui.tx_responsavel.setText(str(pegadados[0][19]))
            self.ui.tx_celularRep.setText(str(pegadados[0][20]))
        except:
            error
    
    def selecionatipoempresa(self):
        if self.ui.com_tipo_empres.currentText()=='fisica':
            self.ui.bt_sintegra.setDisabled(True)
        if self.ui.com_tipo_empres.currentText()=='juridica':  
            self.ui.bt_sintegra.setDisabled(False)
    def selecionapais(self,verifica=None):
        try:
            if verifica=='d':
                pais=self.ui.comb_pais.currentText()
                self.ui.tx_cod_pais.setText(str(db.pega_dados(f'''SELECT codigo FROM tb_pais where descricao='{pais}' ''')))
            if verifica=='c':
                
                p=self.ui.tx_cod_pais.text()
                self.ui.comb_pais.setCurrentText(str(db.pega_dados(f'''SELECT descricao FROM tb_pais where codigo='{p}' ''')))
        except:error
    def carregacidade(self):
        text=self.ui.tx_cep.text().replace('.','').replace('-','').replace('_','')
        cod = db.pega_dados(f'''SELECT * FROM Municipio where cep='{text}'  ''')
       
        self.ui.tx_codMunicipio.setText(str(cod[0][0]))
        self.ui.tx_cidade.setText(str(cod[0][2]))
        self.ui.tx_estado.setText(str(cod[0][3]))
    def selecionalogo(self,event):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", ":", "Image Files (*.png *.jpg *jpeg *.bmp);;All Files (*)") # Ask for file
        if fileName: # If the user gives a fileimagem, _ = QFileDialog.getOpenFileName(
                pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image        
                self.pixmap = pixmap.scaled(200,200, QtCore.Qt.KeepAspectRatio)
                self.ui.lb_logo.setPixmap(self.pixmap) # Set the pixmap onto the label
                self.pixmap.save('config/logo/logo.png')
                
        
    def Configparam(self):
        tipoempre=self.ui.com_tipo_empres.currentText()
        cnpj=self.ui.tx_cnpj.text()
        inscricao=self.ui.tx_rg_ie.text()
        regime=self.ui.comb_regime.currentText()
        razaosocial=self.ui.tx_razaosocio.text()
        nomefantasia=self.ui.tx_fantasia.text()
        cep=self.ui.tx_cep.text()
        endereco=self.ui.tx_endereco.text()
        numero=self.ui.tx_numero.text()
        complemento=self.ui.tx_complemento.text()
        bairro=self.ui.tx_bairro.text()
        cidade=self.ui.tx_cidade.text()
        uf=self.ui.tx_estado.text()
        codpais=self.ui.tx_cod_pais.text()
        descpais=self.ui.comb_pais.currentText()
        email=self.ui.tx_email.text()
        site=self.ui.tx_site.text()
        celularempre=self.ui.tx_celular.text()
        nomerepresentant=self.ui.tx_responsavel.text()
        celularresponsalvel=self.ui.tx_celularRep.text()
        removecarecteria=".-()/_"#remove caracterias
        for remove in range(0,len(removecarecteria)):
            cnpj=cnpj.replace(removecarecteria[remove],"")
            celularempre=celularempre.replace(removecarecteria[remove],"")
            celularresponsalvel=celularresponsalvel.replace(removecarecteria[remove],"")
            
        while True:
            if tipoempre=='':
                Mensagem.mensagem(self,'tipo empressa*','tipo empressa vazio')
                break
            
            if cnpj=='':
                Mensagem.mensagem(self,'cnpj*','cnpj vazio')
                break
            if inscricao=='':
                Mensagem.mensagem(self,'inscricao*','inscricao vazio')
                break
            if regime=='':
                Mensagem.mensagem(self,'regime tributario**','regime tributario* vazio')
                break
            if razaosocial=='':
                Mensagem.mensagem(self,'nome /razao  social*','nome /razao  social vazio')
                break
            if nomefantasia=='':
                Mensagem.mensagem(self,'apelido/fantasia*','apelido/fantasia vazio')
                break
            if cep=='':
                Mensagem.mensagem(self,'cep*','cep vazio')
                break
            if endereco=='':
                Mensagem.mensagem(self,'endereço*','endereço vazio')
                break
            if numero=='':
                Mensagem.mensagem(self,'numero*','numero vazio')
                break
            if complemento=='':
                Mensagem.mensagem(self,'complemento*','complemento vazio')
                break
            if bairro=='':
                Mensagem.mensagem(self,'bairro*','bairro vazio')
                break
            if cidade=='':
                Mensagem.mensagem(self,'cidade*','cidade vazio')
                break
            if uf=='':
                Mensagem.mensagem(self,'uf*','uf vazio')
                break
            if codpais=='':
                Mensagem.mensagem(self,'codpais*','codpais vazio')
                break
            if descpais=='':
                Mensagem.mensagem(self,'pais*','pais* vazio')
                break
            if email=='':
                Mensagem.mensagem(self,'email*','email vazio')
                break
            if site=='':
                Mensagem.mensagem(self,'site*','site vazio')
                break
            if celularempre=='':
                Mensagem.mensagem(self,'celular*','celular vazio')
                break
            if nomerepresentant=='':
                Mensagem.mensagem(self,'responsalve pela empresa*','responsalve pela empresa* vazio')
                break
            if celularresponsalvel=='':
                Mensagem.mensagem(self,'celular responsavel*','celular responsavel* vazio')
                break
            else:
                #inserir vermd5 data
                data_atual = datetime.date.today()
                data_futura = data_atual + datetime.timedelta(days=30)
                data_vecimento=data_futura.strftime("%d/%m/%Y")
                dataverifica = cryptocode.encrypt(f"{data_vecimento}","willow")#essa funçao criptografica data

                db.adicionar(f''' insert into param (tipo_empresa,cnpj,inscricao,
                             regime_tributario,razao_social,nome_fantasia,cep,endereco,
                             numero,complemento,bairro,cidade,uf,codigo_pais,descpais
                             ,email,site,celular_empresa,nome_responsalve,
                             celular_responsavel,liberacao)
                             values('{tipoempre}','{cnpj}','{inscricao}','{regime}','{razaosocial}',
                             '{nomefantasia}','{cep}','{endereco}'
                             ,'{numero}','{complemento}','{bairro}','{cidade}','{uf}','{codpais}',
                             '{descpais}','{email}','{site}','{celularempre}',
                             '{nomerepresentant}',
                             '{celularempre}','{dataverifica}')''')
                
                bancofoto=db.pega_dados(""" select id FROM param ORDER BY id DESC LIMIT 1""")
                db.adicionafoto(str(bancofoto[0][0]))
            break
        
    
    def consulta_sintegra(self):
            try:
                cnpj = self.ui.tx_cnpj.text().replace('.','').replace('/','').replace('-','')
                r = requests.get(f"https://receitaws.com.br/v1/cnpj/{cnpj}")
                empresa = r.json()
                lista=[empresa.get('situacao'),
                       empresa.get('nome'),
                       empresa.get('fantasia'),
                       empresa.get('logradouro'),
                       empresa.get('numero'),
                       empresa.get('bairro'),
                       empresa.get('complemento'),
                       empresa.get('municipio'),
                       empresa.get('cep'),
                       empresa.get('uf'),
                       empresa.get('telefone'),
                       empresa.get('email'),
                       empresa.get('porte'),
                       empresa.get('status')]
                if cnpj=="":
                    QMessageBox.information(self,"Erro ","cnpj")
                else:
                    self.ui.tx_razaosocio.setText(str(lista[1]))
                    self.ui.tx_fantasia.setText(str(lista[2]))
                    self.ui.tx_endereco.setText(str(lista[3]))
                    self.ui.tx_numero.setText(str(lista[4]))
                    self.ui.tx_bairro.setText(str(lista[5]))
                    self.ui.tx_complemento.setText(str(lista[6]))
                    self.ui.tx_cidade.setText(str(lista[7]))
                    self.ui.tx_cep.setText(str(lista[8]))
                    self.ui.tx_estado.setText(str(lista[9]))
                    self.ui.tx_celular.setText(str(lista[10]))
                    self.ui.tx_email.setText(str(lista[11]))
            
            except: 
                QMessageBox.information(self,"Erro ","cnpj")