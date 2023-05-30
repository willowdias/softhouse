from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from funcoesclass.databese.ClassQuery import*
class permissoes:
    def __init__(self):
        pass
    
    def logar(self,login):
     
        banco=db.pega_dados(f''' select * from permissoes_usuario where nome_usuario='{login}' ''')
  
        self.listaobjetoboteos=[
        self.ui.bt_clientes,#0
        self.ui.bt_estoqque,#1
        self.ui.bt_funcionario,#2
        self.ui.tb_receber,#3
        self.ui.tb_caixa,#4
        self.ui.tb_pagarConta,#5
        self.ui.tb_entradanota,#6
        self.ui.tb_analasivenda,#7
        self.ui.tollcadastro,#8
        self.ui.tb_vendas,#9
        self.ui.toolfinanceiro,#10
        self.ui.tollutitilitarios,#11
        self.ui.tolconfiguracao,#12
        self.ui.bt_Cadastros,#13
        self.ui.BtFinanceiros,#14
        self.ui.bt_entradasnotas,#15
        self.ui.Bt_vendas] 
        for i in range(0,len(self.listaobjetoboteos)):
            self.listaobjetoboteos[i].close()     
        else:
            try:
                if banco[0][3]=="S":
                    self.listaobjetoboteos[0].show()
                if banco[0][4]=="S":
                    self.listaobjetoboteos[1].show()
                if banco[0][5]=="S":
                    self.listaobjetoboteos[2].show()
                if banco[0][7]=="S":
                    self.listaobjetoboteos[3].show()
                if banco[0][6]=="S":
                    self.listaobjetoboteos[4].show()
                if banco[0][8]=="S":
                    self.listaobjetoboteos[5].show()
                if banco[0][9]=="S":
                    self.listaobjetoboteos[6].show()
                if banco[0][10]=="S":
                    self.listaobjetoboteos[7].show()
                if banco[0][11]=="S":
                    self.listaobjetoboteos[8].show()
                if banco[0][12]=="S":
                    self.listaobjetoboteos[9].show()
                if banco[0][13]=="S":
                    self.listaobjetoboteos[10].show()
                if banco[0][14]=="S":
                    self.listaobjetoboteos[11].show()
                if banco[0][15]=="S":
                    self.listaobjetoboteos[12].show()
                if banco[0][16]=="S":
                    self.listaobjetoboteos[13].show()
                if banco[0][17]=="S":
                    self.listaobjetoboteos[14].show()
                if banco[0][18]=="S":
                    self.listaobjetoboteos[15].show()
                if banco[0][19]=="S":
                    self.listaobjetoboteos[16].show()
            except:error   
        
        
    def selecionaFuncionario(self,login):
        funcionario=db.pega_dados(f''' select codigo_usuario,nome_usuario from tb_funcionario where nome_usuario='{login}' ''')
        #,funcionario[0][1]
        return funcionario[0][0],funcionario[0][1]
        
        