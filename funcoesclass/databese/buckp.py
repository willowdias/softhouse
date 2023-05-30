import shutil
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from ClassQMessageBox.ClassQmessagebox import *#IMPORA MENSAGEM BOX
#from databese.ClassQuery import*
from funcoesclass.FormCode.Formbuckp import*
from datetime import datetime
import os
import subprocess

import pymysql
class statbuckp(QDialog):
    def __init__(self):
        QWidget.__init__(self)

        self.ui = Ui_Formbuckp()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        #self.setWindowFlags(Qt.Tool)
        self.showFullScreen()
        
        self.ui.bt_origem.clicked.connect(self.selecionacaminhoorigem)
        #salva
        self.ui.bt_start.clicked.connect(self.starbuckp)
        #sair sistema
        self.ui.lb_link.mouseDoubleClickEvent=self.abrirpasta
        #seleciona buckp mysql
        self.ui.rd_mysql.toggled.connect(lambda:self.show_mysql_widget('s'))
            
        self.ui.bt_voltaincial.clicked.connect(lambda:self.show_mysql_widget('n'))
        #seelciona banco muysq
        self.ui.com_origem.clicked.connect(self.selecionbancomysql)
        self.ui.comdestino.clicked.connect(self.selecionacaminhosalvamysql)
        #salva banco mmysql
        self.ui.bt_starmysql.clicked.connect(self.buckpmysq)
        #fecha
        self.ui.bt_cancelar.clicked.connect(self.closeEventsistema)
    def closeEventsistema(self):
        confirma=self.confirmacao('Fechar','Deseja fechar Sistema?')
        if confirma:
            self.close()
    def show_mysql_widget(self,sim):
        if sim=="s":
            self.ui.stackedWidget.setCurrentWidget(self.ui.mysql)
            self.ui.rd_mysql.setCheckable(False)
        else:
            self.ui.rd_mysql.setCheckable(True)
            self.ui.stackedWidget.setCurrentWidget(self.ui.inicial)
    def selecionbancomysql(self):
        
        fileName, _ = QFileDialog.getOpenFileName(None, "Selecionar banco", "", "banco dados  (*.exe *)")
        if fileName:
            caminhobanco=(str(fileName).replace('.exe','').replace('C:/','C:\ '))
            self.ui.mysqcaminhoorigem.setText(caminhobanco.replace(" ",''))
    def selecionacaminhosalvamysql(self):
        fileName= QFileDialog.getExistingDirectory(None, 'Selecione uma pasta buckp')
        if fileName:
           self.ui.mysqcaminhodestino.setText(f'{str(fileName)}/db_mysql.sql')
    def buckpmysq(self):
        db_host = self.ui.db_host.text()
        db_user = self.ui.db_user.text()
        db_password = self.ui.db_password.text()
        db_name = self.ui.db_name.text()
        caminhoorigem=self.ui.mysqcaminhoorigem.text()
        backup_file_path = self.ui.mysqcaminhodestino.text()
        if db_host=='' or db_user==''or db_password=='' or db_name=='' or backup_file_path=='' or caminhoorigem=='':
            pass
        else:
            conn = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)

            subprocess.run([f'{caminhoorigem}', '-u', db_user, '-p'+db_password, db_name, '--result-file=' + backup_file_path])
            #C:\wamp64/bin/mysql/mysql5.7.31/bin/mysqldump
            conn.close()

    def selecionacaminhoorigem(self):
        if self.ui.rd_naocomprimir.isChecked() or self.ui.rd_compactar.isChecked():
            fileName, _ = QFileDialog.getOpenFileName(None, "Selecionar banco", "", "banco dados  (*.sqlite *.db *.FDB)")
            if fileName: 
                self.ui.tx_origem.setText(str(fileName))
                nome_pasta = datetime.now().strftime("%H%M%S")
            
                if not os.path.exists(nome_pasta):
                    c=str(fileName+nome_pasta).replace('.','')
                    os.makedirs(f'{c}')
                    self.ui.tx_destino.setText(f'{c}')
                    self.ui.lb_link.setText(str(f'{c}'))
                
            self.ui.bt_start.setDisabled(False) 
    def confirmacao(self,titulo,mensagem):
        q = QMessageBox()
        q.setWindowTitle(f"<center>{titulo}</center>")
        q.setText(mensagem)
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
    def mensagem_erro(self, titulo, msg):
        q = QMessageBox()
        q.setWindowTitle(f"<center>{titulo}</center>")
        q.setText(msg)
        q.setIcon(QMessageBox.Critical)
        q.setStandardButtons(QMessageBox.Ok)
        q.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        q.setModal(True)
        #q.move(self.mapToGlobal(self.rect().center() - q.rect().center()))
        
        q.exec()
    def starbuckp(self):
        caminho=self.ui.tx_origem.text()
        destino=self.ui.tx_destino.text()
        self.confirma=self.confirmacao('buckp','Deseja Fazer buckp')
        if self.confirma:
            if caminho=='' or destino=='':
                self.mensagem_erro('Erro','campo caminho em branco')
            else:
                if self.ui.rd_naocomprimir.isChecked():
                    thread = CopyThread(caminho,destino)
                    thread.start()
                    thread.join() 
                    self.limparcampo() 
                if self.ui.rd_compactar.isChecked():
             
                   
                    nome_pasta = datetime.now().strftime("%H%M%S")
                    nome_arquivo_saida = f"buckp{nome_pasta}.rar"
                    # Define o comando a ser executado no sistema operacional
                    comando = f'"C:/Program Files/WinRAR/WinRAR.exe" a -ep1 -r "{destino}/{nome_arquivo_saida}" "{caminho}"'

                    subprocess.run(comando, shell=True)
                    thread = CopyThread(None,None)
                    thread.start()
                    thread.join()
                    self.limparcampo() 
    def abrirpasta(self,event):
        caminho_pasta = self.ui.lb_link.text()
        os.startfile(caminho_pasta) 
    def limparcampo(self):
        self.ui.bt_start.setDisabled(True) 
        self.ui.tx_origem.clear()
        self.ui.tx_destino.clear()         
class CopyThread(threading.Thread):
    def __init__(self, src_path=None, dst_path=None):
        
        threading.Thread.__init__(self)
        
        self.src_path = src_path
        self.dst_path = dst_path
        
    def run(self):
        try:
            shutil.copy(self.src_path, self.dst_path)
        except:KeyError
 

'''db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'banco'
backup_file_path = 'E:\PRogramaçao Python\CodeSoft\dsi.sql'

conn = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)

subprocess.run(['C:\wamp64/bin/mysql/mysql5.7.31/bin/mysqldump', '-u', db_user, '-p'+db_password, db_name, '--result-file=' + backup_file_path])

conn.close()'''

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = statbuckp()
    # Verifica se a aplicação está ativa
    ui.exec_()
    sys.exit(app.exec_())

