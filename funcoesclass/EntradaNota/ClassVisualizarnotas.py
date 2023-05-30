from PyQt5.QtWidgets import *
from funcoesclass.FormCode.FormVisualisarNotasEntrada import*
from funcoesclass.databese.ClassQuery import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *#IMPORA MENSAGEM BOX
class ForVisualiNotaEntrada(QDialog):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_FormNotasEntrada()
        self.ui.setupUi(self)
        self.showFullScreen()
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        self.ui.tb_WidegNotas.setColumnWidth(0, 80)#id
        self.ui.tb_WidegNotas.setColumnWidth(1, 140)#numeronota
        self.ui.tb_WidegNotas.setColumnWidth(2, 350)#razao social
        self.ui.tb_WidegNotas.setColumnWidth(3, 120)#cnpj
        self.ui.tb_WidegNotas.addAction(self.ui.actionAPAGAR_NOTA)
        self.ui.tb_WidegNotas.addAction(self.ui.actionEDITA_NOTA)
        self.ui.bt_BuscarNota.clicked.connect(self.FunbusCarnotaFisca)
        self.ui.tb_WidegNotas.itemSelectionChanged.connect(self.FuVisualiQuantidadeITem)
        
    def FunbusCarnotaFisca(self):
        numero=self.ui.tx_BuscarNota.text()
        numeronota=db.pega_dados(f'''select * from tb_compra where  id_nota like'%{numero}%' or razao_social like '%{numero}%' ''')
        self.ui.tb_WidegNotas.setRowCount(0)
        for linha,row in enumerate(numeronota):
            self.ui.tb_WidegNotas.insertRow(linha)
            self.ui.tb_WidegNotas.setItem(linha, 0, QTableWidgetItem(str(row[0])))#id
            self.ui.tb_WidegNotas.setItem(linha, 1, QTableWidgetItem(str(row[1])))#numero
            self.ui.tb_WidegNotas.setItem(linha, 2, QTableWidgetItem(str(row[3])))#razao social
            self.ui.tb_WidegNotas.setItem(linha, 3, QTableWidgetItem(str(row[4])))#cnpj
    def FuVisualiQuantidadeITem(self):
        try:
            visualisar=self.ui.tb_WidegNotas.selectedItems()[1].text()
            banco=db.pega_dados(f'''select * from tb_nfe_item where id_nota='{visualisar}'   ''')

            self.ui.lb_VisualisaQuantidadeitem.setText(f'{str(len(banco))}')
            self.ui.tab_ProdutoVisualisar.setRowCount(0)
            for linha,row in enumerate(banco):
                self.ui.tab_ProdutoVisualisar.insertRow(linha)
                self.ui.tab_ProdutoVisualisar.setItem(linha, 0, QTableWidgetItem(str(row[0])))#id
                self.ui.tab_ProdutoVisualisar.setItem(linha, 1, QTableWidgetItem(str(row[2])))#id
                self.ui.tab_ProdutoVisualisar.setItem(linha, 2, QTableWidgetItem(str(row[3])))#id
        except:error