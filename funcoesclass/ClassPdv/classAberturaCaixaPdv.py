from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *#IMPORA MENSAGEM BOX

from  funcoesclass.databese.ClassQuery import*
import json
from datetime import datetime
import time
data=datetime.today().strftime("%d/%m/%Y").capitalize()
from  funcoesclass.FormCode.FormAberturaCaixaPdv import*
class FormAberturaCaixa(QDialog):
    def __init__(self,Time=None,labelOcupado=None,frame_3=None):
        QWidget.__init__(self)
        self.ui = Ui_FormAberturaCaixaPdv()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        #puxa tipo documento
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(99)
        self.shadow.setColor(QtGui.QColor(99,255,255))
        self.shadow.setOffset(4)
        self.setGraphicsEffect(self.shadow)
        #show caixa
        self.visualisarCaixa()
        form = db.pega_dados(f'''SELECT descricao FROM tb_tipodocumento  ''')
        formapagamento = [item[0] for item in form]
        
        self.ui.cb_incluirTipodocumento.addItems(formapagamento)
        self.ui.dt_incluirdata.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        
        self.time=Time
        self.labelOcupada=labelOcupado
        self.frame_3=frame_3
        #verifica se caixa ta aberto
        with open("config/caixa.json", encoding='utf-8') as meu_json:
            dados = json.load(meu_json)
        obs=[dados.get('caixa')]#aqui abrer aqurivo

        if obs[0]=='fechado':
            self.ui.LB_abertura.setText("caixa Fechado")
            self.ui.bt_confirma.clicked.connect(self.abricaixa)
        elif obs[0]=='aberto':
            self.ui.LB_abertura.setText("caixa aberto")
            self.ui.bt_confirma.clicked.connect(self.fecharcaixa)
        ###################################
        
    def fecharcaixa(self):
        descricao=self.ui.tx_Descricaixa.text()
        valor=self.ui.db_valorCaixa.value()
        tipodoc=self.ui.cb_incluirTipodocumento.currentText()
        data=self.ui.dt_incluirdata.text()
        dictionary ={
            "caixa":"fechado",   
            } 
        json_object = json.dumps(dictionary, indent = 1) 
        with open("config/caixa.json", "w") as outfile: #se for aberto mudara json
            outfile.write(json_object)
        self.confirma=Mensagem.confirmacao(self,"Entra",'deseja fechar Caixa')
        if self.confirma:
            
            db.adicionar(f''' insert into tb_caixa (nota,nome,valortotal,tipodocumento,data_emissao,cd_doc)values
                         ('AberturaCaixa','{descricao}','{valor}','{tipodoc}','{data}','d')''')
        
            self.time.stop()
            self.labelOcupada.setText("Caixa fechado")
            self.frame_3.setDisabled(True)
            self.hide()
    def abricaixa(self):
        descricao=self.ui.tx_Descricaixa.text()
        valor=self.ui.db_valorCaixa.value()
        tipodoc=self.ui.cb_incluirTipodocumento.currentText()
        data=self.ui.dt_incluirdata.text()
        dictionary ={
            "caixa":"aberto",   
            } 
        json_object = json.dumps(dictionary, indent = 1) 
        with open("config/caixa.json", "w") as outfile: #se for aberto mudara json
            outfile.write(json_object)
        
        self.confirma=Mensagem.confirmacao(self,"Entra",'deseja  Abrir CAixa')
        if self.confirma:
            
            db.adicionar(f''' insert into tb_caixa (nota,nome,valortotal,tipodocumento,data_emissao,cd_doc)values
                         ('AberturaCaixa','{descricao}','{valor}','{tipodoc}','{data}','c')''')
            self.hide()
            self.time.start()
            self.labelOcupada.setText("Caixa ABERTO")
            self.frame_3.setDisabled(False)
    def visualisarCaixa(self):
    
        
        tipo=db.pega_dados(''' select * from tb_tipodocumento ''')
        self.data=datetime.today().strftime("%d/%m/%Y")
        for i,dados in enumerate(tipo):
            self.ui.tab_caixa.insertRow(i)
            item=QTableWidgetItem(str(dados[1]))
            item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
            self.ui.tab_caixa.setItem(i,0,item)

            valortotal=db.pega_dados(f'''select SUM(valortotal)  from tb_caixa where tipodocumento='{dados[2]}' and data_emissao='{self.data}' ''')
            if valortotal==None:
                item=QTableWidgetItem(f'R$ 0,00')
                item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
                self.ui.tab_caixa.setItem(i,1,item)
            else:
                item=QTableWidgetItem(f'R$ {str(valortotal[0][0])}')
                item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
                self.ui.tab_caixa.setItem(i,1,item)