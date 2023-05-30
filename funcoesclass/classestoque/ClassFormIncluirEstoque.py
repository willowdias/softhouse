from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *
from funcoesclass.databese.ClassQuery import*
import time
import os
from funcoesclass.FormCode.FormIncluirEstoques import*
from datetime import datetime
import time
from funcoesclass.ClassFormSegundaria.ClassFormIncluirFornecedor import*#importa Cadastro Fornecedor
from funcoesclass.ClassFormSegundaria.ClassGrupoDeProdutos import*#imorta grupo
import random
import barcode
from barcode.writer import ImageWriter
class FormIncluirEstoque(QDialog):
    def __init__(self,*args):
        QWidget.__init__(self)
        self.args = args#essa funçao chama varias funça ouutra class sem precisa sintax
        self.ui = Ui_Form_Incluir_estoque()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        #self.setWindowFlags(Qt.Tool)
        self.showFullScreen()
        #lista objettab
        self.listaobjetab=[]
       
        #chamaCodigoproduto
        self.ui.tx_codGrupo.mouseDoubleClickEvent=self.Grupoproduto
        self.ui.tx_codfornecedo.mouseDoubleClickEvent=self.Fun_BuscarTelaFornecedo
        #
        #botao adicionar foto
        self.ui.bt_selecionar_foto.clicked.connect(self.Fun_Add_foto)
        #addicona validaddo
        self.ui.tx_codigoBarra.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.ui.tx_fracaoPRoduto.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.ui.tx_maximoproduto.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.ui.tx_minimoProduto.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.ui.tx_codGrupo.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.ui.tx_ncm.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.ui.tx_cfopSaida.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.ui.tx_CstSaida.setValidator(QDoubleValidator(0.99, 99.99, 2))
        form = db.pega_dados(f'''SELECT descricao FROM tb_classtributaria  ''')
        formapagamento = [item[0] for item in form]
        self.ui.cb_classificacao.addItems(formapagamento)
        #seleciona classificaçao tributaria
        self.ui.cb_classificacao.activated[str].connect(self.Tributacao)
        #puxa id pra altera estoque
        
        self.codigobarra=self.args[1]
        #essa funçao ativa ou Desativa botao devido sua tela 
        self.ativaModoaltera=self.args[0]
        if self.ativaModoaltera=="S":
            self.SelecionaAltera(self.codigobarra)
            self.ui.bt_Salvar.clicked.connect(self.Fun_AlteraProduto)
            self.MostraVendaDoProduto(str(self.codigobarra))
        else:
            #ADICIONA PRODUTO
            self.ui.bt_Salvar.clicked.connect(self.Fun_SalvarProduto)
        #fecha tela
        self.ui.bt_clostela.clicked.connect(self.closeTEla)
        
        #calcular valore
        self.ui.db_compra.editingFinished.connect(self.calculalucro)
        self.ui.db_custo.editingFinished.connect(self.calculalucro)
        self.ui.tx_porcentagemvenda.editingFinished.connect(self.calculalucro)
        
        #geraCodigo Barra
        self.ui.ch_codiBarra.toggled.connect(self.geracodigobarra)
        #removoe tab
        for i in range(self.ui.tabWidget.count()):
            self.ui.tabWidget.removeTab(0)
            self.ui.tabWidget.addTab(self.ui.dadosproduto,"dados produto")
        #cheeck clickar
        self.ui.chefotos.clicked.connect(self.AddTabwidget)
        self.ui.chetributos.clicked.connect(self.AddTabwidget)
        self.ui.chehistorico.clicked.connect(self.AddTabwidget)

        
       
            #self.ui.lb_codigoBarra.setCursor(QCursor(Qt.PointingHandCursor))
        
    def AddTabwidget(self):
        che=self.sender()
        checkde=str(che.text()).lower()
        
        if checkde=='fotos':
            objeto=self.ui.fotos
            name=checkde
        if checkde=='tributos':
            objeto=self.ui.tributos
            name=checkde 
        if checkde=='historico':
            objeto=self.ui.HISTORICO
            name=checkde       
        if checkde:
            if checkde  not in self.listaobjetab:
                self.ui.tabWidget.addTab(objeto,f"{name}")     
                self.listaobjetab.append(checkde)
            else:
                for inde,nameobjeto in zip(range(1,self.ui.tabWidget.count()),self.listaobjetab):
                    if checkde==nameobjeto:
                        self.listaobjetab.remove(checkde)
                        self.ui.tabWidget.removeTab(inde)
                        
    def calculalucro(self):
        try:
            compra=self.ui.db_compra.value()
            precocusto=self.ui.db_custo.value()
            if precocusto==0:
                self.ui.db_custo.setValue(compra)
            else:
                t=self.ui.tx_porcentagemvenda.value()
                self.ui.tx_valorVenda.setValue(compra + (compra * t / 100))
                self.ui.db_lucroreal.setValue(compra-precocusto)        
                self.ui.db_lucro.setValue((compra/precocusto)*100-100)
        except:error
   
    def closeTEla(self):
        self.confirma=Mensagem.confirmacao(self,"Fecha Tela","deseja Fechar Tela") 
        if self.confirma:
            self.close()    
    def geracodigobarra(self):
        
        self.ui.lb_codigoBarra.clear()
        if self.ui.ch_codiBarra.isChecked():
            bancoorca=db.pega_dados(""" select codigo_barra FROM codigobarra ORDER BY codigo_barra DESC LIMIT 1""")
            # Gera um número aleatório com 12 dígitos
            numero = ''.join(random.choices(f'{bancoorca[0][0]}', k=12))
            # Calcula o dígito verificador do número gerado
            soma = sum(int(d) * (3 if i % 2 == 0 else 1) for i, d in enumerate(numero))
            digito_verificador = (10 - (soma % 10)) % 10
            # Concatena o dígito verificador ao número para obter o código EAN-13 completo
            codigo = numero + str(digito_verificador)
            # Gera o código de barras
            ean = barcode.get('ean13', codigo, writer=ImageWriter())
            self.ui.tx_codigoBarra.setText(str(ean))
            # Salva o código de barras em um arquivo PNG
            filename = ean.save('config/imgcodigobarra/ean13_barcode')  
            img=QPixmap(filename)
            self.ui.lb_codigoBarra.setPixmap(img) # Set the pixmap onto the label
            self.ui.lb_codigoBarra.setAlignment(QtCore.Qt.AlignCenter)
            
            logo3d=(filename)
            self.original_img = QPixmap(logo3d)
            self.cursorlogo = QCursor(self.original_img,-1,-1)
            self.ui.lb_codigoBarra.setCursor(self.cursorlogo)
            self.ui.lb_codigoBarra.setMouseTracking(True)
        else:
            self.ui.lb_codigoBarra.setCursor(QCursor(Qt.PointingHandCursor))
            self.ui.tx_codigoBarra.clear()
    def Grupoproduto(self,event):
        self.grupodeProdutos=grupodeProdutos()
        self.grupodeProdutos.setModal(True)
        def selecionargrupo():
            seleciona=self.grupodeProdutos.ui.tab_GrupoPRodutos.selectedItems()
            self.ui.tx_DescricaoGrupo.setText(str(seleciona[1].text()))
            self.ui.tx_codGrupo.setText(str(seleciona[0].text()))
            self.grupodeProdutos.close()
        self.grupodeProdutos.ui.tab_GrupoPRodutos.doubleClicked.connect(selecionargrupo)    
        self.grupodeProdutos.exec_()
    def MostraVendaDoProduto(self,codigobarra):
        bando=db.pega_dados(f'''select * from orca where cod_barra='{codigobarra}' and Finalizado='S' ''')
        self.ui.tb_HistoricoComprasProduto.setRowCount(0)
        for linha, row_data in enumerate (bando): 
            
            self.ui.tb_HistoricoComprasProduto.insertRow(linha)
            self.ui.tb_HistoricoComprasProduto.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(row_data[6])))#data
            self.ui.tb_HistoricoComprasProduto.setItem(linha, 1, QtWidgets.QTableWidgetItem(f'{float(row_data[4])}0'))#quantidade
            self.ui.tb_HistoricoComprasProduto.setItem(linha, 2, QtWidgets.QTableWidgetItem(f'{float(row_data[5])}0'))#valor
    
    def SelecionaAltera(self,codigobarra):
        bancoestoque=db.pega_dados(f"""SELECT * FROM tb_estoque where codigo_barra='{codigobarra}'   """)
        self.ui.TX_IDpRODUTO.setText(str(bancoestoque[0][0]))
        self.ui.tx_codigoBarra.setText(str(bancoestoque[0][1]))
        self.ui.tx_DescricaoProduto.setText(str(bancoestoque[0][2]))
        self.ui.tx_tipoDeUnidade.setText(str(bancoestoque[0][3]))
        self.ui.tx_Fornecedor.setText(str(bancoestoque[0][4]))
        self.ui.tx_MarcaProduto.setText(str(bancoestoque[0][5]))
        self.ui.tx_QuantidadeProduto.setValue(bancoestoque[0][6])
        self.ui.tx_fracaoPRoduto.setText(str(bancoestoque[0][7]))
        self.ui.tx_valorVenda.setValue(bancoestoque[0][8])
        self.ui.tx_ObsProduto.setPlainText(bancoestoque[0][9])
        self.ui.tx_maximoproduto.setText(str(bancoestoque[0][10]))
        self.ui.tx_minimoProduto.setText(str(bancoestoque[0][11]))
        self.ui.tx_ncm.setText(str(bancoestoque[0][12]))
        self.ui.db_compra.setValue(bancoestoque[0][13])
        self.ui.db_custo.setValue(bancoestoque[0][14])
        self.ui.db_lucro.setValue(bancoestoque[0][15])
        self.ui.tx_codst.setText(str(bancoestoque[0][16]))
        self.ui.cb_classificacao.setCurrentText(str(bancoestoque[0][17]))
        self.ui.tx_cfopSaida.setText(str(bancoestoque[0][18]))
        self.ui.tx_CstSaida.setText(f'0{str(bancoestoque[0][19])}')
        self.ui.tx_codGrupo.setText(f'{str(bancoestoque[0][20])}')
        self.ui.tx_DescricaoGrupo.setText(f'{str(bancoestoque[0][21])}')
        if str(bancoestoque[0][23])=="S":
            self.ui.cheativo.setChecked(True)
        else:
            self.ui.cheativo.setChecked(False)
        recupera_imagen = f'{os.getcwd()}/config/FotosEstoque'
        for nome_arquivo in os.listdir(recupera_imagen):
            if f'{str(bancoestoque[0][0])}' in nome_arquivo:#verifica se img na pasta
                pixmap = QtGui.QPixmap(f'{os.getcwd()}/config/FotosEstoque/{nome_arquivo}') # Setup pixmap with the provided image        
                self.pixmap = pixmap.scaled(int(200), int(200), QtCore.Qt.KeepAspectRatio)
                self.ui.lb_fotos_estoque.setPixmap( self.pixmap) # Set the pixmap onto the label
                self.ui.lb_fotos_estoque.setAlignment(QtCore.Qt.AlignCenter)
        
         
    def Fun_Add_foto(self):#adicionar foto LAbel
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", ":", "Image Files (*.png *.jpg *jpeg *.bmp);;All Files (*)") # Ask for file
        if fileName: # If the user gives a fileimagem, _ = QFileDialog.getOpenFileName(
                pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image        
                self.pixmap = pixmap.scaled(200,200, QtCore.Qt.KeepAspectRatio)
                self.ui.lb_fotos_estoque.setPixmap( self.pixmap) # Set the pixmap onto the label
                #self.ui.label_fotos_clientes.setScaledContents(True)
                self.ui.lb_fotos_estoque.setAlignment(QtCore.Qt.AlignCenter) 
    def Fun_AlteraProduto(self):
        self.codigo_barra=self.ui.tx_codigoBarra.text()
        self.descricaoproduto=self.ui.tx_DescricaoProduto.text()
        self.unidadeproduto=self.ui.tx_tipoDeUnidade.text()
        self.fonecedorproduto=self.ui.tx_Fornecedor.text()
        self.marcaProduto=self.ui.tx_MarcaProduto.text()
        self.quantidadeproduto=self.ui.tx_QuantidadeProduto.value()
        self.fracoproduto=self.ui.tx_fracaoPRoduto.text()
        self.obs=self.ui.tx_ObsProduto.toPlainText()
        self.ncm=self.ui.tx_ncm.text()
        self.maximu=self.ui.tx_maximoproduto.text()
        self.minimo=self.ui.tx_minimoProduto.text()
        self.compra=self.ui.db_compra.value()
        self.custo=self.ui.db_custo.value()
        self.lucro=self.ui.db_lucro.value()
        self.codst=self.ui.tx_codst.text()
        self.clasificacao=self.ui.cb_classificacao.currentText()
        self.cfop_saida=self.ui.tx_cfopSaida.text()
        self.cst_saida=self.ui.tx_CstSaida.text()
        self.valorVendaProduto=self.ui.tx_valorVenda.value()
        self.codgrupo=self.ui.tx_codGrupo.text()
        self.descricaogrupo=self.ui.tx_DescricaoGrupo.text()
        if self.ui.cheativo.isChecked():
            ativo="S"
        else:
            ativo="I"
        removecaracteria="!@#$1234567890.,-+*/_''"
        for remove in range(0,len(removecaracteria)):
            self.unidadeproduto=self.unidadeproduto.replace(removecaracteria[remove],'')
    


        while True:
            if self.descricaoproduto=="":
                Mensagem.mensagem_erro(self,"Erro","Nome do produto é dado obrigatório")
                self.ui.tx_DescricaoProduto.setFocus()   
                break
            if self.unidadeproduto=="":
                Mensagem.mensagem_erro(self,"Erro","UNIDADE  VAZIA")
                self.ui.tx_tipoDeUnidade.setFocus()   
                break
            if self.quantidadeproduto=="":
                Mensagem.mensagem_erro(self,"Erro","QUANTIDADE VAZIA")
                self.ui.tx_QuantidadeProduto.setFocus()   
                break
            if int(self.valorVendaProduto<=0):
                Mensagem.mensagem_erro(self,"Erro","VALOR DE VENDA  VAZIO")
                self.ui.tx_valorVenda.setFocus()   
                break
            
            if self.codst=="":
                Mensagem.mensagem_erro(self,"Erro","codst tributario obrigatorio.")
                self.ui.cb_classificacao.setFocus()
                break
            if self.cfop_saida=="":
                Mensagem.mensagem_erro(self,"Erro","CFOP de saída é dado obrigatório.")
                self.ui.tx_cfopSaida.setFocus()
                break
            if len(self.cfop_saida)<4:
                Mensagem.mensagem_erro(self,"Erro","cfop saida menor que permitido\n sao 4 digitos ")
                self.ui.cb_classificacao.setFocus()
                break
            if len(self.cst_saida)<4:
                Mensagem.mensagem_erro(self,"Erro","cst saida menor que permitido\n sao 4 digitos ")
                self.ui.cb_classificacao.setFocus()
                break
            if self.cst_saida=="":
                Mensagem.mensagem_erro(self,"Erro","CST de saída é dado obrigatório.")
                self.ui.tx_CstSaida.setFocus()
                break   
            if self.codigo_barra=="":
                Mensagem.mensagem_erro(self,"Erro","CODIGO DE BARRA VAZIO")
                self.ui.tx_codigoBarra.setFocus()
                break
            if self.ncm=="":
                Mensagem.mensagem_erro(self,"Erro","NCM é um dado obrigatório")
                self.ui.tx_ncm.setFocus()
                break
            
            else:
                db.adicionar(f''' UPDATE tb_estoque set codigo_barra='{self.codigo_barra}', descricao='{self.descricaoproduto}',
                unidade='{self.unidadeproduto}',fonecedor='{self.fonecedorproduto}',marca='{self.marcaProduto}',
                quantidade='{self.quantidadeproduto}', fracao='{self.fracoproduto}',valor='{self.valorVendaProduto}'
                ,obs='{self.obs}',maximo_prod='{self.maximu}',minimo_prod='{self.minimo}',
                ncm='{self.ncm}',preco_compra='{self.compra}',preco_custo='{self.custo}',
                lucro='{self.lucro}',codst='{self.codst}',class_tributaria='{self.clasificacao}',
                cfop_saida='{self.cfop_saida}',cst_saida='{self.cst_saida}',descricaogrupo='{self.descricaogrupo}',
                codgrupo='{self.codgrupo}',ativo='{ativo}'
                where id='{self.ui.TX_IDpRODUTO.text()}' ''')
                try:
                
                    self.pixmap.save(f"config/FotosEstoque/{self.ui.TX_IDpRODUTO.text()}.png")
                except:KeyError
                Mensagem.mensagem(self,'Cadastro','Produto Alterado Com Sucesso')
                self.close()
            break
    def Fun_SalvarProduto(self):#funçao adicion produto
        self.codigo_barra=self.ui.tx_codigoBarra.text()
        self.descricaoproduto=self.ui.tx_DescricaoProduto.text()
        self.unidadeproduto=self.ui.tx_tipoDeUnidade.text()
        self.fonecedorproduto=self.ui.tx_Fornecedor.text()
        self.marcaProduto=self.ui.tx_MarcaProduto.text()
        self.quantidadeproduto=self.ui.tx_QuantidadeProduto.value()
        self.fracoproduto=self.ui.tx_fracaoPRoduto.text()
        self.obs=self.ui.tx_ObsProduto.toPlainText()
        self.ncm=self.ui.tx_ncm.text()
        self.maximu=self.ui.tx_maximoproduto.text()
        self.minimo=self.ui.tx_minimoProduto.text()
        self.compra=self.ui.db_compra.value()
        self.custo=self.ui.db_custo.value()
        self.lucro=self.ui.db_lucro.value()
        self.codst=self.ui.tx_codst.text()
        self.clasificacao=self.ui.cb_classificacao.currentText()
        self.cfop_saida=self.ui.tx_cfopSaida.text()
        self.cst_saida=self.ui.tx_CstSaida.text()
        self.valorVendaProduto=float(self.ui.tx_valorVenda.value())
        self.codgrupo=self.ui.tx_codGrupo.text()
        self.descricaogrupo=self.ui.tx_DescricaoGrupo.text()
        self.Dataemissao=datetime.today().strftime("%d/%m/%Y").capitalize()
        if self.ui.cheativo.isChecked():
            ativo="S"
        else:
            ativo="I"
        removecaracteria="!@#$1234567890.,-+*/_''"
        for remove in range(0,len(removecaracteria)):
            self.unidadeproduto=self.unidadeproduto.replace(removecaracteria[remove],'')
    
      

        while True:
            if self.descricaoproduto=="":
                Mensagem.mensagem_erro(self,"Erro","Nome do produto é dado obrigatório")
                self.ui.tx_DescricaoProduto.setFocus()   
                break
            if self.unidadeproduto=="":
                Mensagem.mensagem_erro(self,"Erro","UNIDADE  VAZIA")
                self.ui.tx_tipoDeUnidade.setFocus()   
                break
            if self.quantidadeproduto=="":
                Mensagem.mensagem_erro(self,"Erro","QUANTIDADE VAZIA")
                self.ui.tx_QuantidadeProduto.setFocus()   
                break
            if int(self.valorVendaProduto<=0):
                Mensagem.mensagem_erro(self,"Erro","VALOR DE VENDA  VAZIO")
                self.ui.tx_valorVenda.setFocus()   
                break
            
            if self.codst=="":
                Mensagem.mensagem_erro(self,"Erro","codst tributario obrigatorio.")
                self.ui.cb_classificacao.setFocus()
                break
            if self.cfop_saida=="":
                Mensagem.mensagem_erro(self,"Erro","CFOP de saída é dado obrigatório.")
                self.ui.tx_cfopSaida.setFocus()
                break
            if len(self.cfop_saida)<4:
                Mensagem.mensagem_erro(self,"Erro","cfop saida menor que permitido\n sao 4 digitos ")
                self.ui.cb_classificacao.setFocus()
                break
            if len(self.cst_saida)<4:
                Mensagem.mensagem_erro(self,"Erro","cst saida menor que permitido\n sao 4 digitos ")
                self.ui.cb_classificacao.setFocus()
                break
            if self.cst_saida=="":
                Mensagem.mensagem_erro(self,"Erro","CST de saída é dado obrigatório.")
                self.ui.tx_CstSaida.setFocus()
                break   
            if self.codigo_barra=="":
                Mensagem.mensagem_erro(self,"Erro","CODIGO DE BARRA VAZIO")
                self.ui.tx_codigoBarra.setFocus()
                break
            if self.ncm=="":
                Mensagem.mensagem_erro(self,"Erro","NCM é um dado obrigatório")
                self.ui.tx_ncm.setFocus()
                break
            if len(self.ncm)<8:
                Mensagem.mensagem_erro(self,"Erro","NCM tem que ter 8 digitos")
                self.ui.tx_ncm.setFocus()
                break
          
           
            else:
                db.adicionar(f"""INSERT INTO tb_estoque(codigo_barra,descricao,unidade,
                fonecedor,marca,quantidade,fracao,valor,maximo_prod,minimo_prod,ncm,preco_compra,preco_custo,
                lucro,codst,class_tributaria,cfop_saida,cst_saida,codgrupo,descricaogrupo,data_emissao,ativo)values('
                {self.codigo_barra}','{self.descricaoproduto}','{self.unidadeproduto}',
                '{self.fonecedorproduto}','{self.marcaProduto}','{self.quantidadeproduto}','{self.fracoproduto}',
                '{self.valorVendaProduto}','{self.maximu}','{self.minimo}','{self.ncm}',
                '{self.compra}','{self.custo}','{self.lucro}','{self.codst}',
                '{self.clasificacao}','{self.cfop_saida}','{self.cst_saida}','{self.codgrupo}','{self.descricaogrupo}','{self.Dataemissao}','{ativo}')""")
                Mensagem.mensagem(self,'Cadastro','Produto Cadastrado Com Sucesso')
                
                
                try:
                    bancofoto=db.pega_dados(""" select id FROM tb_estoque ORDER BY id DESC LIMIT 1""")
                    self.pixmap.save(f"confi/FotosEstoque/{bancofoto[0][0]}.png")
                except:KeyError
                self.close()
            break
  
    def Fun_BuscarTelaFornecedo(self,event):
        self.FormIncluirFornecedor=FormIncluirFornecedor()
        self.FormIncluirFornecedor.setModal(True)
        self.FormIncluirFornecedor.setWindowFlag(Qt.Drawer)
        self.FormIncluirFornecedor.setWindowModality(QtCore.Qt.ApplicationModal)
        def selecionarFoncedortable():
            try:
                selecionarFonecedoTab=self.FormIncluirFornecedor.ui.tab_Fornecedor.selectedItems()
                self.ui.tx_Fornecedor.setText(str(selecionarFonecedoTab[1].text()))
                self.FormIncluirFornecedor.close()
            except:
                error
        self.FormIncluirFornecedor.ui.tab_Fornecedor.doubleClicked.connect(selecionarFoncedortable)
        self.FormIncluirFornecedor.exec_()
    
    def Tributacao(self):
        descricao=self.ui.cb_classificacao.currentText()
        form = db.pega_dados(f'''SELECT * FROM tb_classtributaria where descricao ='{descricao}'  ''')
        try:
            self.ui.tx_codst.setText(str(form[0][1]))
            
            if form[0][1]=='f':
                self.ui.tx_cfopSaida.setText('5405')
                self.ui.tx_CstSaida.setText('0500')
                
            if form[0][1]=='t':
                self.ui.tx_cfopSaida.setText('5102')
                self.ui.tx_CstSaida.setText('0102')
            if form[0][1]=='i':
                self.ui.tx_cfopSaida.setText('5102')
                self.ui.tx_CstSaida.setText('0400')
        except:error