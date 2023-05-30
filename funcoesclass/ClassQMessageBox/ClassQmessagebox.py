qmesagem="""QMessageBox{background-color: rgb(38, 50, 56);text-transform: uppercase;font: 11pt MS Shell Dlg 2;}
            QLabel{background-color: rgb(38, 50, 56);width:400px;color:white;}
            QPushButton{opacity: 5;background-color: rgb(103, 255, 128);font: 87 14pt Arial;}
            QPushButton:hover{background-color: rgb(0, 0, 255);}
            QPushButton:checked{background-color:red;}
            QMessageBox {border-radius: 1px;opacity: 100;background-color: rgb(38, 50, 56);border: 1px solid black;border-bottom-color :white;}'"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.FormCode.FormMessagemWidget import*
from funcoesclass.databese.ClassQuery import*
import time
class Mensagem(QDialog):
    def __init__(self):
        QWidget.__init__(self)

        self.ui = Ui_FormMessagemWidget()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.ui.pushButton.clicked.connect(self.CloseTelas)
  
        
    def CloseTelas(self):
        self.hide()

    def confirmacao(self,titulo,mensagem):
        q = QMessageBox()
        q.setWindowTitle(f"<center>{titulo}</center>")
        q.setText(mensagem)
        q.setStyleSheet(qmesagem)
        q.setIcon(QMessageBox.Question)
        q.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        q.setModal(True)
        q.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        #q.move(self.mapToGlobal(self.rect().center() - q.rect().center()))
        x = q.exec_()
        if x == 1024:
                return True
        else:
                return False

    def mensagem(self, titulo, msg):
        q = QMessageBox()
        q.setWindowTitle(f"<center>{titulo}</center>")
        q.setText(msg)
        q.setStyleSheet(qmesagem)
        q.setIcon(QMessageBox.Information)
        q.setStandardButtons(QMessageBox.Ok)
        q.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        q.setModal(True)
        #q.move(self.mapToGlobal(self.rect().center() - q.rect().center()))#centralizar widget
        q.exec()


    def mensagem_erro(self, titulo, msg):

        q = QMessageBox()
        q.setWindowTitle(f"<center>{titulo}</center>")
        q.setText(msg)
        q.setStyleSheet(qmesagem)
        q.setIcon(QMessageBox.Critical)
        q.setStandardButtons(QMessageBox.Ok)
        q.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        q.setModal(True)
        #q.move(self.mapToGlobal(self.rect().center() - q.rect().center()))
        
        q.exec()
    
    def messagem_personalizada(self,item,nome,total,data,Numeronota=None):
        box= QMessageBox ()
        self.Numeronota=Numeronota
        box.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        box.setStyleSheet('''QMessageBox {background-color: #333333;text-align:center;width:200px;}
        QMessageBox QLabel {font: 14pt MS Shell Dlg 2;color: white;text-align:center;width:300px;}
        QMessageBox QPushButton{width:200; height:50;text-align:center;color:#fff;border:0px;font-size:15px;cursor: pointer;background-color:#538fff;
        padding:1px 0px;}QMessageBox QPushButton:hover{background-color:#3668ff;}''')
        salvarorca=box.addButton("SALVAR ORÇAMENTO", QMessageBox.AcceptRole)
        fechartela=box.addButton("FECHAR TELA", QMessageBox.AcceptRole)
        box.exec()
        if(box.clickedButton() == salvarorca):    
                
                self.Nomecliente=nome
                self.valor=total
                self.data=data
                bancoorca=db.pega_dados(""" select NOTA FROM orcas ORDER BY NOTA DESC LIMIT 1""")
                self.nota=1
                for orca in bancoorca:
                    if orca[0]<1:
                        self.nota=orca[0]
                    else:
                        self.nota=orca[0]+1
                resultado = db.pega_dados(f'''SELECT nota FROM orcas WHERE nota ='{self.Numeronota.text()}' ''')
           
                if len(resultado):  #Verifica se o retorno contém alguma linha
                    db.apaga(f'''delete from orca where nota='{self.Numeronota.text()}' ''')
                    
                    db.adicionar(f''' update orcas set Finalizar='N' , descricao='{self.Nomecliente}',valortotal='{self.valor}',
                                 data_final={self.data}
                                 where nota='{self.Numeronota.text()}' ''')
                    item(self.Numeronota.text())
                else:
                    if nome=='':
                        db.adicionar(f''' insert into orcas (nota,descricao,valortotal,data_emissao,data_final,Finalizar)values
                        ('{self.nota}','{'consumidor final'}','{self.valor}','{self.data}','{self.data}','N')  ''')   

                    else:
                        db.adicionar(f''' insert into orcas (nota,descricao,valortotal,data_emissao,data_final,Finalizar)values
                        ('{self.nota}','{self.Nomecliente}','{self.valor}','{self.data}','{self.data}','N')  ''')   
                        
                    item(self.nota)
                
        if(box.clickedButton() == fechartela):    
                self.close()
       

        