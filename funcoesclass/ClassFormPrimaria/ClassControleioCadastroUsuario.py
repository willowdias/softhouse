from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.databese.ClassQuery import*
#importa incluirClinetes
from funcoesclass.FormCode.FormControleioCadastroUsuario import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
#import baixa

class ForcontroleioCadastroUsuario(QDialog):#essa tela puxa os quarto
    def __init__(self,verificar=None):
        QWidget.__init__(self)
      
        self.ui = Ui_ForPermissaoUsuario()
        self.ui.setupUi(self)
       
        #QGraphicsOpacityEffect
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()
        #closeTela
        self.ui.widget_4.close()
        self.ui.bt_altera.close()
        '''#coluna table itens
        self.ui.tb_libera.setColumnWidth(0, 80)
        self.ui.tb_libera.setColumnWidth(1, 30)'''
        self.ui.widget_2.move(self.mapToGlobal(self.rect().center() - self.ui.widget_2.rect().center()))
        self.ui.widget_4.move(self.mapToGlobal(self.rect().center() - self.ui.widget_4.rect().center()))
        #fechar Sistema todo
        self.ui.bt_cancelar.clicked.connect(self.CloseSistema)
        #closee Form
        self.ui.bt_Voltar.clicked.connect(self.CloseForm)
        #novo add tela
        self.ui.bt_adicionar_usuario.clicked.connect(self.novoUser)
        #crrega permisoessuuario
        #seleciona usuario
        self.ui.Libera_acesso_User.clicked.connect(self.EditaLiberacao)
        #carrega usuario    
        self.FunCarregarusuario()
        #remove tab 
        self.ui.tabWCadastro.removeTab(1)
        #salvarliberaçao
        self.ui.bt_liberaUser.clicked.connect(self.SalvaLiberacao)
        #corrigi coluna
        self.ui.tableWidget.setColumnWidth(0, 220)#descriçao
        self.ui.tableWidget.setColumnWidth(2, 1)#codigo barra
        #retorna cadastro user
        self.ui.bt_ReturnCadastroUser.clicked.connect(self.ReturnaCadastroUSer)
        #cria novo usuario
        self.ui.bt_salvarUser.clicked.connect(self.FunAdicionaUsuario)
        #editaSeha
        self.ui.bt_edita_usuario.clicked.connect(self.editaUsuario)
        #editar usuario
        self.ui.bt_altera.clicked.connect(self.SalvaUserEditado)
        #mostraSenha oculta
        self.ui.ch_mostrSenha.toggled.connect(self.MostraSenha)
        #self.ui.printar.clicked.connect(self.botaoselecionacoluna),
        #selecion head cell
        self.ui.checkBox.toggled.connect(self.marcaTodapcao)
    def toggleCheckState(self, index):
        print('willow')
        if index == 3:
            pass
    def FunCarregarusuario(self):
        banco=db.pega_dados('''select * from usuario ''')
        
        self.ui.tb_CadastroUsuario.setRowCount(0)
        for linha,row in enumerate(banco):
            self.ui.tb_CadastroUsuario.insertRow(linha)
            self.ui.tb_CadastroUsuario.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tb_CadastroUsuario.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(row[1])))
    def CarregaLiberaçao(self,codigo=None,nome=None):
        self.ui.lb_codUSer.setText(str(codigo))
        self.ui.lb_Descuser.setText(str(nome))
        banco=db.pega_dados(f''' SELECT * FROM permissoes_usuario 
                            where codigo_usuario='{codigo}'and nome_usuario='{nome}' ''')
        headertitle = db.pega_dados(''' SELECT * FROM pragma_table_info('permissoes_usuario') ''')
        self.ui.tableWidget.setRowCount(0)
        
        for  linha,campos in enumerate (banco):
            for  linhainde,tabela in enumerate (headertitle):
                self.ui.tableWidget.insertRow(linhainde)
                
                tabelas = QTableWidgetItem(str(tabela[1]))
                tabelas.setForeground(QColor(255, 0, 0))
                tabelas.setFlags(Qt.NoItemFlags)   
                self.ui.tableWidget.setItem(linhainde,0, tabelas)
                
                acessos = QTableWidgetItem(str(campos[linhainde]))
                acessos.setFlags(Qt.NoItemFlags)  
                self.ui.tableWidget.setItem(linhainde,1,acessos)
                
                self.ui.tableWidget.item(linhainde,0).setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget.item(linhainde,1).setTextAlignment(Qt.AlignCenter)
                
                if campos[linhainde]=="S":
                    self.checkbox = QCheckBox()
                    self.checkbox.setCheckState(Qt.Checked) 
                    self.ui.tableWidget.setCellWidget(linhainde, 2, self.checkbox) 
                    self.checkbox.stateChanged.connect(self.SelecionaChecativo)
                else: 
                    self.checkbox = QCheckBox()
                    self.checkbox.setCheckState(Qt.Unchecked)
                    self.ui.tableWidget.setCellWidget(linhainde, 2, self.checkbox) 
                    self.checkbox.stateChanged.connect(self.SelecionaChecativo)
        for remove in range(3):                         
            self.ui.tableWidget.removeRow(0)         

       
    def marcaTodapcao(self):
        if self.ui.checkBox.isChecked():
            for i in range(self.ui.tableWidget.rowCount()):
                self.checkbox = QCheckBox()
                self.checkbox.setCheckState(Qt.Checked) 
                self.ui.tableWidget.setCellWidget(i, 2,self.checkbox)
                s = QtWidgets.QTableWidgetItem(str('S'))
                s.setForeground(QtGui.QColor('white'))
                s.setBackground(QtGui.QColor('green'))
                s.setFont(QFont("song", 18))
                self.ui.tableWidget.setItem(i,1,s )
                self.ui.tableWidget.item(i,1).setTextAlignment(Qt.AlignCenter)
                self.checkbox.stateChanged.connect(self.SelecionaChecativo)
        else: 
            for i in range(self.ui.tableWidget.rowCount()):
                n = QTableWidgetItem(str('N'))
                n.setFlags(Qt.NoItemFlags)     
                self.ui.tableWidget.setItem(i,1,n)
                self.ui.tableWidget.item(i,1).setTextAlignment(Qt.AlignCenter)
                self.checkbox = QCheckBox()
                self.checkbox.setCheckState(Qt.Unchecked)
                self.ui.tableWidget.setCellWidget(i, 2, self.checkbox) 
                self.checkbox.stateChanged.connect(self.SelecionaChecativo)      
    def SelecionaChecativo(self):
        linha=self.ui.tableWidget.currentRow()
        if self.ui.tableWidget.cellWidget(linha, 2).isChecked():
          
            s = QtWidgets.QTableWidgetItem(str('S'))
            s.setForeground(QtGui.QColor('white'))
            s.setBackground(QtGui.QColor('green'))
            s.setFont(QFont("song", 18))
            self.ui.tableWidget.setItem(linha,1,s )
            self.ui.tableWidget.item(linha,1).setTextAlignment(Qt.AlignCenter)
        else:
            n = QTableWidgetItem(str('N'))
            n.setFlags(Qt.NoItemFlags)     
            self.ui.tableWidget.setItem(linha,1,n)
            self.ui.tableWidget.item(linha,1).setTextAlignment(Qt.AlignCenter)    
    def EditaLiberacao(self):
        try:
            seleciona=self.ui.tb_CadastroUsuario.selectedItems()
            self.ui.tabWCadastro.removeTab(0)
            self.CarregaLiberaçao(str(seleciona[0].text()),str(seleciona[1].text()))
            self.ui.tabWCadastro.addTab(self.ui.liberausuario, ('LIBERA USUARIO'))
            self.ui.tabWCadastro.setCurrentWidget(self.ui.liberausuario)
        except:error
    def SalvaLiberacao(self):
        s=[]
        for i in range(self.ui.tableWidget.rowCount()):
            s.append(str(self.ui.tableWidget.item(i,1).text()).upper())
        self.confirma=Mensagem.confirmacao(self,'Deseja',f'Deseja Altera Liberaçao Do Usuario {self.ui.lb_Descuser.text()}')
        
        if self.confirma:
        
            while True:
              
                db.adicionar(f''' UPDATE permissoes_usuario set              
                            cadastro_clientes='{s[0]}'
                            ,cadastro_estoque='{s[1]}'
                            ,cadastro_funcionario='{s[2]}'
                            ,caixa='{s[3]}'
                            ,conta_receber='{s[4]}'
                            ,contas_apagar ='{s[5]}'
                            ,entrada_nota ='{s[6]}'  
                            ,analasievenda ='{s[7]}'
                            ,cadastro_menu='{s[8]}'
                            ,venda_menu='{s[9]}'
                            ,financeiro_menu='{s[10]}'
                            ,utilitario_menu='{s[11]}'
                            ,configuracao_menu='{s[12]}'
                            ,cadastro_left='{s[13]}'
                            ,fincanceiro_left='{s[14]}'
                            ,entrada_nota_left='{s[15]}' 
                            ,venda_left='{s[16]}' 
                            where codigo_usuario='{self.ui.lb_codUSer.text()}' ''') 
                time.sleep(1)
                break
           
            self.ui.tabWCadastro.removeTab(0)
            self.ui.tabWCadastro.addTab(self.ui.cadastrousuario, ('CADASTRO USUARIO'))
            self.ui.tabWCadastro.setCurrentWidget(self.ui.cadastrousuario) 
    def ReturnaCadastroUSer(self):
        self.ui.tabWCadastro.removeTab(0)
        self.ui.tabWCadastro.addTab(self.ui.cadastrousuario, ('CADASTRO USUARIO'))
        self.ui.tabWCadastro.setCurrentWidget(self.ui.cadastrousuario) 
    def CloseForm(self):
        self.confirma=Mensagem.confirmacao(self,'Sair','Sair DA tela')
        if self.confirma:
            self.LimparCampos()
            self.ui.widget_4.close()
            self.ui.widget_2.setDisabled(False)
    def CloseSistema(self):
        self.confirma=Mensagem.confirmacao(self,'Sair','Sair DA tela')
        if self.confirma:
            self.close()
    def LimparCampos(self):
        self.ui.tx_codigo_id.clear()
        self.ui.tx_usuario.clear()
        self.ui.tx_senha.clear()
        self.ui.tx_senha2.clear()
    def novoUser(self):
        self.ui.widget_2.setDisabled(True)
        self.ui.widget_4.show() 
        self.ui.tx_usuario.setFocus()   
    def FunAdicionaUsuario(self):
        self.ui.bt_salvarUser.show()
        usuario=self.ui.tx_usuario.text().lower()
        senha=self.ui.tx_senha.text().lower()
        confirmasenha=self.ui.tx_senha2.text().lower()
        while True:
            if usuario=='':
                Mensagem.mensagem(self,"Campo usuario","campos usuario Em branco")
                self.ui.tx_usuario.setFocus()
                break
            if senha=='':
                Mensagem.mensagem(self,"Campo senha","campos senha Em branco")
                self.ui.tx_senha.setFocus()
                break
            if confirmasenha=='':
                Mensagem.mensagem(self,"Campo confirma senha","campos confirma senha Em branco")
                self.ui.tx_senha2.setFocus()
                break
            else:
                self.adicionar=Mensagem.confirmacao(self,'Deseja Adicionar','Deseja Adicionar Usuario')
                if self.adicionar:
                    if (senha == confirmasenha):
                            banco=db.pega_dados(f""" select * FROM usuario where nome ='{usuario}'""")
                            if banco:
                                Mensagem.mensagem(self,'usuario','Cadastro Usuario ja existe')
                            else:
                                db.adicionar(f'''insert into usuario (nome,senha,senha2)values('{usuario}','{senha}','{confirmasenha}') ''')
                            
                                banco=db.pega_dados(f""" select id,nome FROM usuario ORDER BY id DESC LIMIT 1""")
                                db.adicionar(f''' insert into permissoes_usuario(
                                            codigo_usuario,
                                            nome_usuario,
                                            cadastro_clientes,
                                            cadastro_estoque,
                                            cadastro_funcionario,
                                            caixa,
                                            conta_receber,
                                            contas_apagar,
                                            entrada_nota,
                                            analasievenda,
                                            cadastro_menu,
                                            venda_menu,
                                            financeiro_menu,
                                            utilitario_menu,
                                            configuracao_menu,
                                            fincanceiro_left,
                                            entrada_nota_left,
                                            venda_left)values
                                            ('{banco[0][0]}','{banco[0][1]}','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N')''')
                                Mensagem.mensagem(self,"Adicionar","adicionador com sucesso")
                                self.ui.widget_4.close()
                                self.FunCarregarusuario()
                                self.LimparCampos()
                    else:
                        Mensagem.mensagem(self,"Senha erro","Senhas Nao compativel")
            break
    def editaUsuario(self):
        self.ui.widget_2.setDisabled(True)
        self.ui.bt_salvarUser.close()
        self.ui.bt_altera.show()
        try:
            selecionarid=self.ui.tb_CadastroUsuario.selectedItems()[0].text()
            self.ui.widget_4.show()
            banco=db.pega_dados(f""" select * FROM usuario where id ='{selecionarid}'""")
            self.ui.tx_codigo_id.setText(str(banco[0][0])) 
            self.ui.tx_usuario.setText(str(banco[0][1])) 
            self.ui.tx_senha.setText(str(banco[0][2])) 
            self.ui.tx_senha2.setText(str(banco[0][2]))
            self.ui.tx_usuario.setFocus()
            
        except:error
              
    def SalvaUserEditado(self):
        usuario=self.ui.tx_usuario.text().lower()
        senha=self.ui.tx_senha.text().lower()
        confirmasenha=self.ui.tx_senha2.text().lower()
        while True:
            if usuario=='':
                Mensagem.mensagem(self,"Campo usuario","campos usuario Em branco")
                self.ui.tx_usuario.setFocus()
                break
            if senha=='':
                Mensagem.mensagem(self,"Campo senha","campos senha Em branco")
                self.ui.tx_senha.setFocus()
                break
            if confirmasenha=='':
                Mensagem.mensagem(self,"Campo confirma senha","campos confirma senha Em branco")
                self.ui.tx_senha2.setFocus()
                break
            else:
                self.adicionar=Mensagem.confirmacao(self,'Deseja alterar','Deseja alterar Usuario')
                if self.adicionar:
                    if (senha == confirmasenha):
                        
                        db.adicionar(f'''update usuario set  nome='{usuario}' ,senha='{senha}',senha2='{confirmasenha}' where id='{self.ui.tx_codigo_id.text()}'  ''')
                        db.adicionar(f'''update permissoes_usuario set  nome_usuario='{usuario}' where codigo_usuario='{self.ui.tx_codigo_id.text()}'  ''')
                        
                        self.ui.widget_4.close()
                        self.FunCarregarusuario()
                        self.LimparCampos() 
                        self.ui.widget_2.setDisabled(False)     
                    else:
                        Mensagem.mensagem(self,"Senha erro","Senhas Nao compativel")
            break
    def MostraSenha(self,mostra):
        
        if self.ui.ch_mostrSenha.isChecked():
            self.ui.tx_senha2.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.tx_senha.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.tx_senha2.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.tx_senha.setEchoMode(QtWidgets.QLineEdit.Password)