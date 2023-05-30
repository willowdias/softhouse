from PyQt5.QtWidgets import *
from funcoesclass.databese.ClassQuery import*
from funcoesclass.ClassQMessageBox.ClassQmessagebox import *#IMPORA MENSAGEM BOX
from funcoesclass.FormCode.FormEditItemNotaFiscal import*
class ForEditaItem(QDialog):
    def __init__(self,idProduto=None,item_nota=None,ChamTabw=None):
        QWidget.__init__(self)
        self.ui = Ui_FormEditItemNotaFiscal()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Drawer)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()
        self.Idproduto=idProduto
        self.numeronota=item_nota
        self.ChamITemTab=ChamTabw
        self.ui.TX_IDpRODUTO.setText(str(self.Idproduto))
        self.ui.bt_salva.clicked.connect(self.FunEditaProduto)
        #chama descriçao edita
        self.FunChamaDescriaoproduto(self.Idproduto)
        #fecha tela
        self.ui.bt_sair.clicked.connect(self.CloseTela)
    def CloseTela(self):
        self.confirmaFecha=Mensagem.confirmacao(self,'Deseja fecha','Deseja Fechar TEla')
        if self.confirmaFecha:
            self.close()
    def FunChamaDescriaoproduto(self,id):
        banco=db.pega_dados(f'''select * from tb_nfe_item where id='{id}'   ''')
        #self.ui.TX_IDpRODUTO.setText(str(banco[0][1]))
        self.ui.tx_codigoBarra.setText(str(banco[0][2]))
        self.ui.tx_DescricaoProduto.setText(str(banco[0][3]))
        self.ui.tx_QuantidadeProduto.setValue(banco[0][4])
        self.ui.db_compra.setValue(banco[0][5])
        self.ui.tx_valorVenda.setValue(banco[0][6])
        self.ui.tx_tipoDeUnidade.setText(str(banco[0][7]))
        self.ui.tx_cfopSaida.setText(str(banco[0][8]))
        self.ui.tx_CstSaida.setText(str(banco[0][9]))
        self.ui.tx_ncm.setText(str(banco[0][10]))
     
    def FunEditaProduto(self):
        codigobarra=self.ui.tx_codigoBarra.text()
        descricaoproduto=self.ui.tx_DescricaoProduto.text().upper()
        quantidade=self.ui.tx_quantidade.value()
        valorcusto=self.ui.tx_valoCusto.value()
        valortotal=self.ui.tx_valortotal.value()
        tipo_unidade=self.ui.tx_unidade.text()
        cfop_saida=self.ui.tx_cfopSaida.text()
        cst_saida=self.ui.tx_CstSaida.text()
        ncm=self.ui.tx_ncm.text()
        self.confirma=Mensagem.confirmacao(self,'Altera ITem','deseja altera item nota')
        if self.confirma:
            db.adicionar(f'''update tb_nfe_item set codigo_barra='{codigobarra}',
            descricao_produto='{descricaoproduto}',quantidade='{quantidade}',valor_custo='{valorcusto}',
            valor_total='{valortotal}',tipo_unidade='{tipo_unidade}',cfop_saida='{cfop_saida}',
            cst_saida='{cst_saida}',ncm='{ncm}' where id='{self.Idproduto}' ''')
            self.ChamITemTab(self.numeronota)
            self.close()