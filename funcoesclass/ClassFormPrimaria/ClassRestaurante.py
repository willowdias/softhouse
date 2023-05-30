from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.databese.ClassQuery import*
from datetime import timedelta
from datetime import datetime
import datetime
from funcoesclass.FormCode.FormRestaurante import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import*
import os
from PyQt5.QtGui import QPalette, QColor
from funcoesclass.ClassFormSegundaria.ClassQuantidaVenda import*
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QWidget, QLabel
import time
from PyQt5.QtCore import Qt, QThread, QTimer, pyqtSignal


 
        
class Restaurante(QDialog):#analise venda
    def __init__(self,):
        QWidget.__init__(self)
      
        self.ui = Ui_Formrestaurante()
        self.ui.setupUi(self)
        
        self.update_thread = UpdateLabelThread()
        self.update_thread.update_signal.connect(self.chamaMEsa)
        self.update_thread.start()
        #delete 
        self.ui.bt_delete.clicked.connect(self.Removeitemvenda)
        #inseir venda banco dados
        self.ui.bt_finalizaVenda.clicked.connect(self.inseriprodutobanco)
        #ok
        self.ui.spin_quantidade.editingFinished.connect(lambda:self.ui.tx_descriproduto.setFocus())
        #inseir produto tabela
        self.ui.bt_adicionarproduto.clicked.connect(self.inserirprodutomesa)
        #corrig
        self.ui.tb_vendaGrupo.setColumnWidth(0, 160)#codigo barra
        self.ui.tb_vendaGrupo.setColumnWidth(2, 80)#qtd
        self.ui.tb_vendaGrupo.setColumnWidth(3, 80)#vl_un
        self.ui.tb_vendaGrupo.setColumnWidth(4, 80)#VLW
    
        self.ui.bt_criamesa.clicked.connect(self.criamesa)
        self.showMaximized()

    def criamesa(self):
        self.ui.spin_mesa.setDisabled(False)
        self.ui.spin_mesa.setValue(0)
        def inserirmesa():
            self.ui.tx_descriproduto.setFocus()
            mesa=self.ui.spin_mesa.value()
            if int(mesa)<=0:
                self.ui.spin_mesa.setValue(1)
            else:
                verifica=db.pega_dados(f''' select * from tb_mesa where numero='{mesa}' ''')
                if verifica:
                    Mensagem.mensagem(self,'mesa',' mesa ja esta em uso')
                    self.ui.spin_mesa.setValue(0)
                    self.ui.spin_mesa.setDisabled(True)
                else:
                    db.adicionar(f''' insert into tb_mesa(numero,total)values('{mesa}','0') ''')
                    self.ui.spin_mesa.setDisabled(True)
                    self.update_thread.start()
                    
                    
        self.ui.spin_mesa.editingFinished.connect(inserirmesa)
    
    def inserirprodutomesa(self):
        nome=self.ui.tx_descriproduto.text()
        dados =db.pega_dados(f"SELECT *FROM tb_estoque where codigo_barra ='{nome}' ")

        if not dados:
            pass
        elif self.ui.spin_mesa.value()<1:
            pass
        else:
            linha = self.ui.tb_vendaGrupo.rowCount()
            self.ui.tb_vendaGrupo.insertRow(linha)
            self.ui.tb_vendaGrupo.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(dados[0][1])))#codigo
            self.ui.tb_vendaGrupo.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(dados[0][2])))#nome
            self.ui.tb_vendaGrupo.setItem(linha, 2, QtWidgets.QTableWidgetItem(f'{str(self.ui.spin_quantidade.value())}'))#quantidade
            self.ui.tb_vendaGrupo.setItem(linha, 3, QtWidgets.QTableWidgetItem(str(("R$ {:.2f}".format(dados[0][8])))))#valor
            banco=(self.ui.spin_quantidade.value()*float(dados[0][8]))
            self.ui.tb_vendaGrupo.setItem(linha, 4, QtWidgets.QTableWidgetItem(str(("R$ {:.2f}".format(banco)))))#valor
            self.ui.tb_vendaGrupo.selectRow(self.ui.tb_vendaGrupo.rowCount()-1)
            self.SomarColunaTabe()
    def Removeitemvenda(self):
        linha = self.ui.tb_vendaGrupo.currentRow()

        self.ui.tb_vendaGrupo.removeRow(linha)
        self.ui.tb_vendaGrupo.selectRow(self.ui.tb_vendaGrupo.rowCount()-1)
        self.SomarColunaTabe()
    def SomarColunaTabe(self):
        venda=[]
        quantidade=[]
        for i in range(self.ui.tb_vendaGrupo.rowCount()):
           
            venda.append(str(self.ui.tb_vendaGrupo.item(i, 4).text()).replace('R','').replace('$',''))
            quantidade.append(str(self.ui.tb_vendaGrupo.item(i, 2).text()).replace('R','').replace('$',''))
          
        valor=0
        for vendas in venda:
            valor += float(vendas) 
            self.ui.db_vendas.setValue(valor)
        qnt=0
        for quant in quantidade:
     
            qnt += float(quant)
            self.ui.tx_Quantidade.setText(str(qnt)) 
           
        linha=(self.ui.tb_vendaGrupo.rowCount())
        if linha==0:#remove coluna
            self.ui.db_vendas.setValue(0)
            self.ui.tx_Quantidade.setText(str('0,00'))            
        
        
    def inseriprodutobanco(self):
        db.apaga(f'''delete from tb_item_mesa where numero='{self.ui.spin_mesa.value()}' ''')
        if int(self.ui.spin_mesa.value())>0:
            for i in range(self.ui.tb_vendaGrupo.rowCount()):        
                codigobara=(self.ui.tb_vendaGrupo.item(i, 0).text())
                descricao=(self.ui.tb_vendaGrupo.item(i, 1).text())
                qnt=(self.ui.tb_vendaGrupo.item(i, 2).text())  
                vl_unid=str(self.ui.tb_vendaGrupo.item(i, 3).text().replace('R','').replace('$',''))   
                vl_total=str(self.ui.tb_vendaGrupo.item(i, 4).text().replace('R','').replace('$',''))   
                
                db.adicionar(f'''insert into tb_item_mesa (numero,cod_barra,descricao,quant,vl_unid,vl_total)
                             values ('{self.ui.spin_mesa.value()}','{codigobara}','{descricao}','{qnt}','{vl_unid}','{vl_total}')''')

                db.update(f''' update tb_mesa set total='{self.ui.db_vendas.value()}' where numero='{self.ui.spin_mesa.value()}'  ''')
                
            self.ui.spin_mesa.setValue(0)
            self.ui.spin_garcon.setValue(0)
            self.ui.db_vendas.setValue(0)
            self.ui.spin_quantidade.setValue(1)
            self.ui.tx_Quantidade.setText('0,00')
            self.ui.tx_descriproduto.clear()
            self.ui.tb_vendaGrupo.setRowCount(0)
                    
    def chamaMEsa(self,text):
        run=0   
        dados =db.pega_dados(f"SELECT *FROM tb_mesa  ")
        self.ui.listGrupoProdutos.clear()     
        for index, name in enumerate(dados):
            item_widget = QWidget()
            item_layout = QVBoxLayout(item_widget)
            
            
            item_botao = QPushButton(f'00{name[1]}')
        
            labelnome = QLabel('consumidor final')
            labelnome.setScaledContents(True)
            labelnome.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
         
            frame = QFrame()
            frame.setFrameShape(QFrame.Box)  
            frame.setMidLineWidth(1)  
            pixmap = QPixmap(':/telainicial/telainicial/timebreve.png')
            labeliconetime=QLabel()
            labeliconetime.setPixmap(pixmap)
            labeliconetime.setScaledContents(True)
            labeliconetime.setMaximumWidth(20)
            labeliconetime.setMaximumHeight(20)
            tempo = QLabel(f"{str(text)}")
                
            valor=QDoubleSpinBox()
            valor.setButtonSymbols(QDoubleSpinBox.NoButtons) 
            valor.setGroupSeparatorShown(True)
            valor.setPrefix("R$ ")  
            valor.setRange(0, 1500000)  
            valor.setValue(name[7]) 
                
            frame_layout = QHBoxLayout()
            frame_layout.addWidget(labeliconetime)
            frame_layout.addWidget(tempo)
            frame_layout.addWidget(valor)
            frame.setLayout(frame_layout)

            layout = QVBoxLayout()
            layout.addWidget(frame)
            
            item_layout.addWidget(item_botao)
            item_layout.addWidget(labelnome)
            item_layout.addWidget(frame)
                
            list_item = QListWidgetItem()
            list_item.setSizeHint(QSize(350,180))
            self.ui.listGrupoProdutos.addItem(list_item)
            self.ui.listGrupoProdutos.setItemWidget(list_item, item_widget)
            item_botao.clicked.connect(self.selecionamesa) 
            #self.update_thread.join()
            QApplication.processEvents()

           

    def selecionamesa(self):
        item=self.sender()
        mesa=str(item.text()).lower()
        self.ui.spin_mesa.setValue(int(mesa))
        
        dados =db.pega_dados(f"SELECT *FROM tb_item_mesa where numero ='{int(mesa)}' ")
        self.ui.tb_vendaGrupo.setRowCount(0)
        for linha, name in enumerate(dados):
            self.ui.tb_vendaGrupo.insertRow(linha)
            self.ui.tb_vendaGrupo.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(name[2])))#codigo
            self.ui.tb_vendaGrupo.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(name[3])))#nome
            self.ui.tb_vendaGrupo.setItem(linha, 2, QtWidgets.QTableWidgetItem(f'{str(name[4])}'))#quantidade
            self.ui.tb_vendaGrupo.setItem(linha, 3, QtWidgets.QTableWidgetItem(str(("R$ {:.2f}".format(name[5])))))#valor
            self.ui.tb_vendaGrupo.setItem(linha, 4, QtWidgets.QTableWidgetItem(str(("R$ {:.2f}".format(name[6])))))#valor
            self.ui.tb_vendaGrupo.selectRow(self.ui.tb_vendaGrupo.rowCount()-1)
        self.SomarColunaTabe()

class UpdateLabelThread(QThread):
    update_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
    def run(self):
        run=0
        while True:
            run+=1
            self.update_signal.emit(str(run))
            time.sleep(1.9)
