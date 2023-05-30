

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QLabel, QDialog
from PyQt5 import QtWidgets, QtCore, QtPrintSupport, QtGui
#import icone

from funcoesclass.FormCode.inicial import*
#importa Cadastro Cliente
from funcoesclass.ClassFormPrimaria.ClassFormControleioClientes import*
#import estoque
from funcoesclass.classestoque.ClassFormControleioEstoque import*
#importa Tela PDv
from funcoesclass.ClassPdv.Pdv import*
#importa PArcelas Clientes
from funcoesclass.ClassFormPrimaria.ClassFormIncluirPArcelas import*
#import Conta Receber
from funcoesclass.classcontasreceber.ClassFormContaReceber import*
#import Caixa
from funcoesclass.ClassFormPrimaria.ClassFormCaixa import*
#ControleioFuncionario
from funcoesclass.ClassFormPrimaria.ClassFormControelioFuncionario import*
#class permisao de usuario
from funcoesclass.ClassLiberauser.Classpermissoesusuario import*
# cadastro de usuario
from funcoesclass.ClassFormPrimaria.ClassControleioCadastroUsuario import*
#Entrada DEnota Fiscal
from funcoesclass.EntradaNota.ClassEntradaDeNota import*
#incluir tipo documento
from funcoesclass.ClassFormPrimaria.ClassIncluirTipoDocumento import*
#incluir Contas apagar
from funcoesclass.ClassFormPrimaria.ClassContasApagar import*
#fonecedor
#class analise venda
from funcoesclass.ClassFormPrimaria.ClassFormAnalisevenda import*
#from classcadastrotributos
from funcoesclass.ClassFormPrimaria.ClassCadastroTributos import*

#visualisar Grupo Produtos Ui_FormProdutosGrupo
from funcoesclass.ClassFormPrimaria.ClassRestaurante import*
#cadastro grupos 
from funcoesclass.ClassFormSegundaria.ClassGrupoDeProdutos import*#imorta grupo
#lembrete
from funcoesclass.ClassFormPrimaria.ClassLembrete import*
#controleio interno venda
from funcoesclass.classcontroleiointerno.ClassControleiointerno import*
#import config empresa
from funcoesclass.ClassFormPrimaria.ConfigEmpresa import*
#sistema backp
from funcoesclass.databese.buckp import*
import barcode
from barcode.writer import ImageWriter
import cryptocode
import datetime
class telaincial(QMainWindow):
    def __init__(self,Inicial=None,login=None):
        QMainWindow.__init__(self)
        self.ui = Ui_Inicial()
        self.ui.setupUi(self)
        self.showMaximized()
        #verificaliberaçao
        self.lista=[]
        self.objetolista=[]
        self.botoeslateral=[]
        login=str("willow").lower()
        permissoes.logar(self,login)
        #oBJESTOS INICIAL MENU TOP
        self.ui.lb_topico.setText(str(f'Soft House'))
        #menu vendas
        self.ui.tb_vendas.addAction(self.ui.actionpdv_restaurante)
        #action vendas
        self.ui.actionpdv_restaurante.triggered.connect(lambda:Restaurante().exec_())
        #menu cadastro
        self.ui.tollcadastro.addAction(self.ui.actionIncluir_Parcelas)
        self.ui.tollcadastro.addAction(self.ui.actionCadastro_Funcionario)
        self.ui.tollcadastro.addAction(self.ui.actionincluir_tipo_documento)
        self.ui.tollcadastro.addAction(self.ui.actioncadastro_fornecedor)
        self.ui.tollcadastro.addAction(self.ui.actioncadastro_grupo)
        self.ui.tollcadastro.addAction(self.ui.actioncadastro_clientes)
        self.ui.tollcadastro.addAction(self.ui.actioncadastro_estoque)
        self.ui.tollcadastro.addAction(self.ui.actioncadastro_de_tributo)
        #finananceiro tool
        self.ui.toolfinanceiro.addAction(self.ui.actionconta_receber)
        self.ui.actionconta_receber.triggered.connect(self.VerificarEAbriPAginaTab)
        #menu utilitarios
        self.ui.tollutitilitarios.addAction(self.ui.actionCADASTRO_DE_USUARIO)
        self.ui.tollutitilitarios.addAction(self.ui.actionbuckp_sistema)
        
        self.ui.actionbuckp_sistema.triggered.connect(lambda:statbuckp().exec_())
        #menu config
        self.ui.tolconfiguracao.addAction(self.ui.actionConfig)
        
        self.ui.actionConfig.triggered.connect(lambda:FormConfigParam().exec_())
        ###############
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        
        #chama bakcp
        #self.ui.actionbuckp_sistema.triggered.connect(lambda:statbuckp().exec_())
        
        #self.setWindowFlags(Qt.WindowSystemMenuHint|Qt.FramelessWindowHint)
        #parcelas
        self.ui.actionIncluir_Parcelas.triggered.connect(lambda:FormIncluirParcelas().exec_())
        #####################################################################################
        #CADASTRO DE USUARIO
        self.ui.actionCADASTRO_DE_USUARIO.triggered.connect(lambda:ForcontroleioCadastroUsuario().exec_())
        #incluir tipo documento
        self.ui.actionincluir_tipo_documento.triggered.connect(lambda:FormTipoDocumento().exec_())
    
        #fornecdor
        self.ui.actioncadastro_fornecedor.triggered.connect(lambda:FormIncluirFornecedor().exec_())

        #cadastrodegruposvisualisar
        self.ui.actioncadastro_grupo.triggered.connect(lambda:grupodeProdutos().exec_())
        #cadastro tributos
        self.ui.actioncadastro_de_tributo.triggered.connect(lambda:ForCadastroTributos().exec_())
        #acttion incluir estoque 
        self.ui.actioncadastro_estoque.triggered.connect(lambda:FormIncluirEstoque('N','None').exec_())
        self.ui.actioncadastro_clientes.triggered.connect(lambda:FormIncluirClientes().exec_())       

        self.ui.actionDeslogar.triggered.connect(self.Deslogar)
        self.login=Inicial#retorna login
        #mmenu bar###############################
        self.SOBRE=QPushButton('SOBRE SISTEMA !')
        self.SOBRE.setStyleSheet("font: 12pt MS Shell Dlg 2;color: white;border:none ;padding:5px 45px;background-color: rgb(38, 50, 56);")
        self.loginUSer=QLabel()
        self.loginUSer.setText(str(login).upper())
        self.loginUSer.setStyleSheet("background-color: rgb(38, 50, 56);font: 12pt MS Shell Dlg 2;color: white; padding:5px 45px;")
        self.SOBRE.clicked.connect( lambda:Mensagem.mensagem(self,'','''SISTEMA COMERCIAL\n
                contato : (69)99270-2408 willow dias\nemail : willow@gmail.com\n''')   )
        
        self.statusBar().addPermanentWidget(self.loginUSer)
        self.statusBar().addPermanentWidget(self.SOBRE)
        self.statusBar().showMessage("SEJA BEM VINDO")
        #pega tamanho do objeto
   
        self.ui.tabWidget.tabCloseRequested.connect(self.removeTab)#fecha click
        self.ui.tabWidget.currentChanged.connect(self.qtabwidget_currentchanged)
        #clicar
        self.ui.bt_maislembrete.clicked.connect(self.adicionaLembrete)
        self.ui.bt_atulembrete.clicked.connect(lambda:self.carregarlembrete())
        
        self.ui.bt_clientes.clicked.connect(self.VerificarEAbriPAginaTab)
        self.ui.bt_estoqque.clicked.connect(self.VerificarEAbriPAginaTab)
        self.ui.bt_funcionario.clicked.connect(self.VerificarEAbriPAginaTab)
        self.ui.tb_receber.clicked.connect(self.VerificarEAbriPAginaTab)
        self.ui.tb_pagarConta.clicked.connect(self.VerificarEAbriPAginaTab)
        self.ui.tb_caixa.clicked.connect(self.VerificarEAbriPAginaTab)
        self.ui.tb_entradanota.clicked.connect(self.VerificarEAbriPAginaTab)
        self.ui.tb_analasivenda.clicked.connect(self.VerificarEAbriPAginaTab)


        self.timeMovimentaLAbel = QtCore.QTimer(self, interval=10000)
        self.timeMovimentaLAbel.timeout.connect(self.MovimentaLAbel) 
        self.timeMovimentaLAbel.start()
        #menu
        #self.ui.bt_Menu.clicked.connect(lambda:self.menu(0,True))
   
        #dasbhoar
        self.dasbhoar = QtCore.QTimer(self, interval=2000)
        self.dasbhoar.timeout.connect(self.Dashboard) 
        self.dasbhoar.start()
        #dataDashborad
        self.ui.dataRelatorio.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        self.ui.dataRelatorio.dateChanged.connect(self.Dashboardata)#editar data
        self.Dashboardata()
        #visualisar DAdos diario
        self.ui.clientes.clicked.connect( self.VerDados)
        self.ui.bt_verestoque.clicked.connect( self.VerDados)
        self.ui.bt_vervenda.clicked.connect( self.VerDados)
        self.ui.bt_caixa.clicked.connect( self.VerDados)
        self.listaobjetosbotao=[self.ui.clientes.clicked,self.ui.bt_verestoque,
                                self.ui.bt_vervenda,self.ui.bt_caixa]
   
        #menu objeto modern
        self.ui.bt_Cadastros.clicked.connect(self.menuObjetos)
        self.ui.BtFinanceiros.clicked.connect(self.menuObjetos)
        self.ui.bt_entradasnotas.clicked.connect(self.menuObjetos)
        self.ui.Bt_vendas.clicked.connect(self.menuObjetos)
        #move tela entre tab
        self.ui.bt_seguir.clicked.connect(lambda:self.moverTab("seguir"))
        self.ui.bt_voltar.clicked.connect(lambda:self.moverTab("voltar"))
        #menu lateral
        self.ui.bt_Menu.enterEvent=lambda event:self.closetlateral()
        self.ui.frame_LT.leaveEvent=lambda event: self.closetlateral()#fecha js
        #fecha tela sistema
        self.ui.bt_closer.clicked.connect(self.CloseTela)
        #verifica da
        self.timerdata = QtCore.QTimer(self, interval=200)
        self.timerdata.timeout.connect(self.verififcaData) 
        self.timerdata.start()
        
    def verififcaData(self):
        try:
            datagerada_vecimento=db.pega_dados(""" select liberacao FROM param""")
            decoded = cryptocode.decrypt(datagerada_vecimento[0][0], "willow")#essa funçao descripta a data    
            data_vencimento = datetime.datetime.strptime(f"{decoded}","%d/%m/%Y").date()
            dias_restantes = (data_vencimento - data_vencimento.today()).days
           
            if dias_restantes==0:
                
                Mensagem.mensagem(self,"Vencimento",
                                  f"""  sua liberaçao expiro   {decoded} entre contado com  Central : (69)9.99270-2408""")
                self.close()
            elif dias_restantes <= 5:
                Mensagem.mensagem(self,"Vencimento",
                                  f"""Faltam {dias_restantes} dias para licença expirar \nvencimento {decoded}\nentre contado com  Central : (69)9.99270-2408""") 
            self.timerdata.stop()    
        except:error
    def adicionaLembrete(self):#coloca lembrete
        Formlembrete(self.carregarlembrete).exec_()
    def alteraLembrete(self):#coloca lembrete
        lembrete=self.sender()
        idconfig=str(lembrete.text()).lower()
        banco=db.pega_dados(f'''select id from lembrete where id='{idconfig}' ''')
        Formlembrete(self.carregarlembrete,banco[0][0]).exec_()          
    def carregarlembrete(self):
        self.lembretelista=db.pega_dados('select * from lembrete')
        while self.ui.lembrete.count():
            item = self.ui.lembrete.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        for a,b in enumerate (self.lembretelista):
            text=QTextBrowser(self) 
            text.setMaximumHeight(150)#coloca tamanho
            text.setPlainText(str(b[1]))
            if b[2]=='#000000' or b[2]=='#0000FF' or b[2]=='#ff0000':#essa funçao coloca cores no text
                text.setStyleSheet(f"background-color:{b[2]} ; color:white;padding:25px; font: 900 9pt Arial Black;line-height: 1.5;")  
            else:
                text.setStyleSheet(f"background-color:{b[2]} ; color:black ; padding:25px;font: 900 9pt Arial Black;line-height: 1.5;")
            botao=QPushButton(text)#ess botao fica objeto criado pra lembrete
            botao.setIcon(QtGui.QIcon(":/telainicial/telainicial/cancelar.png"))
            botao.setStyleSheet('border:none;padding:0px;background-color:none;font: 6pt "Segoe UI";color:transparent;')
            botao.setText(f'{b[0]}')
            botao.clicked.connect(self.deleteLembrete)
            
            botaoedita=QPushButton(text)#ess botao fica objeto criado pra lembrete
            botaoedita.setIcon(QtGui.QIcon(":/telainicial/telainicial/edita.png"))
            botaoedita.setGeometry(205,0,100,25)
            botaoedita.setStyleSheet('border:none;padding:0px;background-color:none;font: 6pt "Segoe UI"; color:transparent;')
            botaoedita.setLayoutDirection(Qt.RightToLeft)
            botaoedita.setText(f'{b[0]}')
            botaoedita.clicked.connect(self.alteraLembrete)
        
            self.ui.lembrete.addWidget(text)  
            
     
    def deleteLembrete(self):#apaga lembrete
        lembrete=self.sender()
        delete=str(lembrete.text()).lower()
        confirma=Mensagem.confirmacao(self,'Excluir',f'Deseja excluir lembrete {delete}')
        
        #widget = self.ui.lembrete.widget(b)
        if confirma:
            db.apaga(f'''delete from lembrete where id ='{delete}'  ''') 
            self.carregarlembrete()    
       

    def closetlateral(self):
      
        abrir=self.ui.frame_LT.width()
        if abrir==0:
            
            self.ui.bt_Menu.setIcon(QtGui.QIcon(":/novo/telainicial/menuopen.png"))
            self.animation = QtCore.QPropertyAnimation(self.ui.frame_LT, b"maximumWidth")
            self.animation.setStartValue(abrir)
            self.animation.setEndValue(150)
            self.animation.setDuration(400)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuint)
            self.animation.start() 
            
        
        else:
            self.ui.bt_Menu.setIcon(QtGui.QIcon(":/novo/telainicial/menuaberto.png"))     
            self.animation = QtCore.QPropertyAnimation(self.ui.frame_LT, b"maximumWidth")
            self.animation.setStartValue(abrir)
            self.animation.setEndValue(0)
            self.animation.setDuration(400)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuint)
            self.animation.start()
            
    

    def CloseTela(self):
        self.confirma=Mensagem.confirmacao(self,'deseja Fecha','Fecha Tela Sistema')
        if self.confirma:
            self.close()
    def MovimentaLAbel(self):
        self.animation = QPropertyAnimation(self.ui.label, b"geometry")
        self.animation.setDuration(10000)  # in milliseconds
        self.animation.setLoopCount(-1)  # infinite loop
        self.animation.setStartValue(QRect(self.ui.frame_move.width(), 0, 450, 50))
        self.animation.setEndValue(QRect(0, 0, 450, 50))
        self.animation.start()
        QApplication.processEvents()
    def menuObjetos(self):
        clickedButton = self.sender()
        selecionar = str(clickedButton.text()).lower()
        objetostab=[self.ui.widgetCadastro,self.ui.frameFinanceiro,
                    self.ui.frameentradanota,self.ui.FrameVenda]
        objetobotao=[self.ui.bt_Cadastros,self.ui.BtFinanceiros,
                     self.ui.bt_entradasnotas,self.ui.Bt_vendas]
        if selecionar=="cadastro":
            i=objetostab[0]
            objbotao=objetobotao[0]
        if selecionar=="financeiro":
            i=objetostab[1] 
            objbotao=objetobotao[1]
           
        if selecionar=="entrada de nota":
            i=objetostab[2]
            objbotao=objetobotao[2]
        if selecionar=="vendas":
            i=objetostab[3]   
            objbotao=objetobotao[3]      
        if selecionar not in self.botoeslateral: 
            self.animation = QtCore.QPropertyAnimation(i, b"maximumHeight")
            self.animation.setEndValue(400)
            self.animation.setDuration(1)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InQuad)
            self.animation.start()
            self.botoeslateral.append(selecionar)
            objbotao.setIcon(QtGui.QIcon(":/telainicial/telainicial/setapracima.png"))
        else:
            objbotao.setIcon(QtGui.QIcon(":/telainicial/telainicial/setabaixo.png"))
            self.animation = QtCore.QPropertyAnimation(i, b"maximumHeight")
            self.animation.setEndValue(0)
            self.animation.setDuration(1)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InQuad)
            self.animation.start()
            self.botoeslateral.clear()   
        
    def Dashboard(self):
     
        cliente=db.pega_dados('''select id from tb_clientes''')
        estoque=db.pega_dados('''select id from tb_estoque''')
        vendas=db.pega_dados('''select id from orcas''')
        caixa=db.pega_dados('''SELECT SUM(valortotal) FROM tb_caixa where cd_doc='c' ''')
        
        self.ui.lb_quantClientes.setText(f' {str(len(cliente))}')
        self.ui.lb_quantEstoque.setText(f' {str(len(estoque))}')
        self.ui.lb_Vendas.setText(f' {str(len(vendas))}')
        self.ui.db_CaixaValor.setValue(caixa[0][0])

    def Dashboardata(self):
        self.data=self.ui.dataRelatorio.text()
        self.ui.db_CaixaValordiario.setValue(0)
        self.ui.lb_quantEstoquediario.setText("0")
        vendas=db.pega_dados(f'''select *from orcas where data_emissao ='{self.data}' ''')
        self.ui.lb_Vendasdiario.setText(f' {str(len(vendas))}')
        clientes=db.pega_dados(f'''select * from tb_clientes where data_emissao='{self.data}' ''')
        self.ui.lb_QuantClienteDiario.setText(f' {str(len(clientes))}')
        try:
            caixa=db.pega_dados(f'''select sum(valortotal)from tb_caixa where data_emissao like'%{self.data}%' and cd_doc='c' ''')
            self.ui.db_CaixaValordiario.setValue(caixa[0][0])
        except:error
        estoque=db.pega_dados(f'''select id from tb_estoque where data_emissao='{self.data}' ''')
        run=0
        for i in estoque:
            run+=int(len(i))
            self.ui.lb_quantEstoquediario.setText(str(run))     
             
    def VerDados(self):#menu
        clickedButton = self.sender()
        selecionar = str(clickedButton.text()).lower()
        fecha=[self.ui.tableWidget,self.ui.tableWidget_2,self.ui.tableWidget_3,self.ui.tableWidget_4]
        if selecionar=='clientes':
            i=(fecha[0])
            numeroBanco=[0,1]
            nomeTabela="tb_clientes"
        if selecionar=='estoque': 
            i=(fecha[1])     
            numeroBanco=[1,2]
            nomeTabela="tb_estoque"
        if selecionar=='vendas':  
            i=(fecha[2]) 
            numeroBanco=[1,2]
            nomeTabela="orcas"     
        if selecionar=='caixa':
            i=(fecha[3])
            numeroBanco=[2,3]
            nomeTabela="tb_caixa"
             
        if selecionar not in self.objetolista: 
            self.animation = QtCore.QPropertyAnimation(i, b"maximumHeight")
            self.animation.setStartValue(0)
            self.animation.setEndValue(300)
            self.animation.setDuration(2000)
            self.animation.setEasingCurve(QtCore.QEasingCurve.OutBack)#Linear ,OutCirc ,OutBounce
            self.animation.start()
            self.objetolista.append(selecionar)
            self.data=self.ui.dataRelatorio.text()
            estoque=db.pega_dados(f'''select * from '{nomeTabela}' where data_emissao='{self.data}' ''') 
            i.setRowCount(0)    
            for linha, row_data in enumerate (estoque): 
                i.insertRow(linha)
                i.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(row_data[numeroBanco[0]])))
                i.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(row_data[numeroBanco[1]]))) 
                
        else:
            self.objetolista.clear()
            self.animation = QtCore.QPropertyAnimation(i, b"maximumHeight")
            self.animation.setStartValue(0)
            self.animation.setEndValue(0)
            self.animation.setDuration(2000)
            self.animation.setEasingCurve(QtCore.QEasingCurve.OutElastic)
            self.animation.start()
    def menu(self,maxWidth,enable):#menu
        self.ui.bt_Menu.setIcon(QtGui.QIcon(":/novo/telainicial/menuopen.png"))
        if enable:
            
            abrir=self.ui.frame_LT.width()

            maxExtend = maxWidth    
            normal = 270
            if abrir==270: 
       
                extender = maxExtend 
             
                self.ui.bt_Menu.setIcon(QtGui.QIcon(":/novo/telainicial/menuaberto.png"))                          
            else:
                
                extender = normal   
            self.animation = QtCore.QPropertyAnimation(self.ui.frame_LT, b"maximumWidth")
            self.animation.setStartValue(abrir)
            self.animation.setEndValue(extender)
            self.animation.setDuration(400)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuint)
            self.animation.start()
            
    
    def moverTab(self,item):#ess funçao move objeto como aba
        if item=='seguir':
            index=self.ui.tabWidget.currentIndex()+1
            self.ui.tabWidget.setCurrentIndex(index)
        else:
            index=self.ui.tabWidget.currentIndex()-1
            self.ui.tabWidget.setCurrentIndex(index)         
            
    @QtCore.pyqtSlot(int)
    def qtabwidget_currentchanged(self, index):
        current_tab_text =self.ui.tabWidget.tabText(index)
       
    
        #self.ui.tabWidget.setTabEnabled(index+1, False)
    @QtCore.pyqtSlot(int)    
    def removeTab(self, index):#remove table widget
        current_tab_text =self.ui.tabWidget.tabText(index)
        
        confirma=Mensagem.confirmacao(self,'Deseja',f'Deseja Fechar {current_tab_text}')
        if confirma:
            if index==0:
                pass
            else:
                
                widget = self.ui.tabWidget.widget(index)
                if widget is not None:
                    self.lista.remove(self.ui.tabWidget.tabText(index))
                    widget.deleteLater()
                    self.ui.tabWidget.removeTab(index)
                
   
    def VerificarEAbriPAginaTab(self,item):

        clickedButton = self.sender()
        selecionar = str(clickedButton.text()).lower()
        self.wid=int(self.ui.tabWidget.width()) 
        self.hei=int(self.ui.inicialpage.height())
        mob=''
        if selecionar=='clientes':
            mob=FormCadastroClientes()
            nome=selecionar
            icon=QtGui.QIcon(":/telainicial/telainicial/cadastro clientes.png")
            objetoFocus=mob.ui.tx_BuscaClientes
        if selecionar=='cadastro funcionario':
            mob=FormControleioFuncio()
            nome=selecionar
            icon=QtGui.QIcon(":/telainicial/telainicial/funcionario.png")
            objetoFocus=mob.ui.tx_BuscaFuncionario
        if selecionar=='estoque':
            mob=FormControleioEstoque()
            nome=selecionar
            icon=QtGui.QIcon(":/telainicial/telainicial/estoque.png")
            objetoFocus=mob.ui.tx_BuscarEstoque
            #direciona numero      
        if selecionar=='entrada de nota':
            mob=FormEntradaDenotasFiscal()
            nome=selecionar
            icon=QtGui.QIcon(":/telainicial/telainicial/entradanota.png")
            objetoFocus=mob.ui.tx_ChaveNota
        if selecionar=='caixa':
            
            mob=Formcaixa(self.wid,self.hei)
           
            nome=selecionar
            icon= QtGui.QIcon(":/telainicial/telainicial/caixa.png")
            #self.ui.tabWidget.removeTab(self.ui.tabWidget.count()-1) 
            objetoFocus=mob.ui.data_emisao   
        if selecionar=='receber':
            x=(self.ui.tabWidget.width())
            mob=FormContasReceber(x)
            nome=selecionar
            icon=QtGui.QIcon(":/telainicial/telainicial/receber.png")
            objetoFocus=mob.ui.tx_buscarCliente
        if selecionar=='contas apagar':
            x=(self.ui.tabWidget.width())
            mob=FormContasApagar(x)
            nome=selecionar
            icon= QtGui.QIcon(":/telainicial/telainicial/parcelas.png")
            objetoFocus=mob.ui.tx_buscaNota
        if selecionar=='analise vendas':
            #analise de veda
          
            mob=Formaanalisevenda(self.wid,self.hei)
            nome=selecionar
            icon=QtGui.QIcon(":/telainicial/telainicial/analytics.png")
            objetoFocus=mob.ui.db_total
        if selecionar=="venda":
            mob=ControleioVendas()
            nome='venda'
            icon=QtGui.QIcon(":/novo/telainicial/combinado.png")
            objetoFocus=mob.ui.tx_BuscaItem_2
        
        #index = self.ui.tabWidget.indexOf(f"{mob}")
        current_tab_text = self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex())
       
        if current_tab_text != selecionar:
            if selecionar not in self.lista: 
                objeto=self.ui.tabWidget.addTab(mob, f"{nome}")
                objetoFocus.setFocus()
                self.ui.tabWidget.setTabIcon(objeto, icon)
                self.ui.tabWidget.setCurrentWidget(mob)
                self.lista.append(selecionar)
            else:
                for a, b in zip(range(1,self.ui.tabWidget.count()),self.lista):
                    if b==selecionar:
                        self.ui.tabWidget.setCurrentIndex(a)
            
   
    def FunChamarClass(self,classe):
        
        self.ui.mdiArea.closeAllSubWindows()
        c= classe
        md=self.ui.mdiArea.addSubWindow(c)
        md.setWindowFlags(Qt.FramelessWindowHint)
        md.setMinimumHeight(800)
        md.setMinimumWidth(1500)
       
       # md.showMaximized() 
        c.show()
        center = self.ui.mdiArea.viewport().rect().center()
        geo = md.geometry()
        geo.moveCenter(center)
        md.setGeometry(geo)
        
    

    def Deslogar(self):
        form=self.login('relogar')
        form.exec_()  
   

        

