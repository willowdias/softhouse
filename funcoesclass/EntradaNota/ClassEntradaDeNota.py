from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from funcoesclass.FormCode.FormEntradaDenota import*

from funcoesclass.ClassQMessageBox.ClassQmessagebox import *#IMPORA MENSAGEM BOX
from funcoesclass.databese.ClassQuery import*
from xml.dom import minidom
from datetime import datetime
import datetime
from decimal import Decimal
from datetime import timedelta
from datetime import datetime
import datetime
from funcoesclass.EntradaNota.ClasseditaItem import*
from funcoesclass.EntradaNota.ClassVisualizarnotas import*
class FormEntradaDenotasFiscal(QDialog):
    def __init__(self,nota=None,FunçaoBusca=None):
        QWidget.__init__(self)
        self.ui = Ui_FormEntradaDenota()
        self.ui.setupUi(self)
        #action
        
       
        self.ui.dt_dataCompra.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        self.ui.dt_dataEntrada.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        self.ui.dt_PArcelamento.setDateTime(QtCore.QDateTime.currentDateTime())#puxa data Hoje
        self.ui.bt_EntraXml.clicked.connect(self.FunBuscarXml)
        #EDITA COLUNA
        self.ui.tab_EntradaNota.setColumnWidth(0, 80)#id
        self.ui.tab_EntradaNota.setColumnWidth(1, 140)#codigo barra
        self.ui.tab_EntradaNota.setColumnWidth(2, 350)#descriçao
        self.ui.tab_EntradaNota.setColumnWidth(3, 120)#quantidadede
        self.ui.tab_EntradaNota.setColumnWidth(4, 120)#valor venda
        #buscar nota fiscal
        self.ui.bt_Notas.clicked.connect(self.funBuscanotaFiscal)
        #addacitotable

        self.ui.actionedita_item.triggered.connect(self.FunEditarITemNota)
        self.ui.tab_EntradaNota.doubleClicked.connect(self.FunEditarITemNota)
      
        #processa pagamento
        self.ui.bt_proceSPagamento.clicked.connect(self.FunCacularPagamento)
        form = db.pega_dados(f'''SELECT descricao FROM tb_tipodocumento  ''')
        formapagamento = [item[0] for item in form]
        self.ui.cb_formaPagamento.addItems(formapagamento)

        
  
    def FunCacularPagamento(self):
        
            valorTotalVenda=self.ui.db_valortotal.value()
            parcela=int(self.ui.db_parcelas.value())
            final=(valorTotalVenda/parcela)
            self.ui.tb_Parcelamento.setRowCount(0)
            run=0
            dados=datetime.datetime.strptime(f"{self.ui.dt_PArcelamento.text()}","%d/%m/%Y")
          
          
            for i in range(0,parcela):#fracionar datas
                run+=1
                dados=dados + timedelta(days=30) 
                datafinal=dados.strftime("%d/%m/%Y")
                
                self.ui.tb_Parcelamento.insertRow(i)
                self.ui.tb_Parcelamento.setItem(i, 0, QTableWidgetItem(str(datafinal)))#parcelas
                self.ui.tb_Parcelamento.setItem(i, 1, QTableWidgetItem(str(f'{run}/{run}')))#parcelas
                self.ui.tb_Parcelamento.setItem(i, 2, QTableWidgetItem(str(final)))#parcelas
                self.ui.tb_Parcelamento.setItem(i, 3, QTableWidgetItem(str(self.ui.cb_formaPagamento.currentText())))#parcelas
                
            for i in range(0,parcela):
                for linha in range(0,4):
                    self.ui.tb_Parcelamento.item(i,linha).setTextAlignment(Qt.AlignCenter)
       
    @QtCore.pyqtSlot()
    def FunBuscarXml(self):
    
       
            fileName, _ = QFileDialog.getOpenFileName(None, "Selecionar arquivo XML", "", "Arquivos  XML  (*.xml)")
            if fileName: 
                with open(f"{fileName}",'r',encoding='utf-8')as f:
                    xml= minidom.parse(f)
                    self.FumLimparCampo()
                    Razaosocial=xml.getElementsByTagName("xNome")
                    NumeroNota=xml.getElementsByTagName("nNF")
                    cnpj=xml.getElementsByTagName("CNPJ")
                    Chavenota=xml.getElementsByTagName("chNFe")
                    modelo_nota=xml.getElementsByTagName("mod")
                    cfop_entrada=xml.getElementsByTagName("CFOP")
                    serienota=xml.getElementsByTagName("serie")
                    cod_pais=xml.getElementsByTagName("cPais")
                    nomepais=xml.getElementsByTagName("xPais")
                    bairro=xml.getElementsByTagName("xBairro")
                    municipio=xml.getElementsByTagName("xMun")
                    endereco=xml.getElementsByTagName("xLgr")
                    cep=xml.getElementsByTagName("CEP")
                    numero_imovel=xml.getElementsByTagName("nro")
                    data_emissao=self.ui.dt_dataEntrada.text()
                    data_entrada=self.ui.dt_dataCompra.text()
                
                    numerochave=str(Chavenota[0].firstChild.data)
                    verificanota=db.pega_dados(f'''select id_nota from tb_compra where id_nota='{NumeroNota[0].firstChild.data}' ''')
                    if len(verificanota):
                        Mensagem.mensagem_erro(self,"numero de nota cadastro","numero de nota cadastro")  
                    else:
                        db.adicionar(f''' insert into  tb_compra (id_nota,chave_nota,razao_social,cnpj,serie_nota,cfop_entrada,modelo,cod_pais,pais,
                                    bairro,municipio,endereco,cep,numero_imovel,data_emissao,data_entrada) values('{NumeroNota[0].firstChild.data}','{numerochave}',
                                    '{Razaosocial[0].firstChild.data}','{cnpj[0].firstChild.data}',
                                    '{serienota[0].firstChild.data}','{cfop_entrada[0].firstChild.data}','{modelo_nota[0].firstChild.data}',
                                    '{cod_pais[0].firstChild.data}','{nomepais[0].firstChild.data}','{bairro[0].firstChild.data}',
                                    '{municipio[0].firstChild.data}','{endereco[0].firstChild.data}','{cep[0].firstChild.data}',
                                    '{numero_imovel[0].firstChild.data}','{data_emissao}','{data_entrada}')''')
                        self.FunEntraProdutos(fileName,NumeroNota[0].firstChild.data)
        
    def FunEntraProdutos(self,chavenota,id_nota):
        with open(f"{chavenota}",'r',encoding='utf-8')as f:
            xml= minidom.parse(f)
            codigoBarra=xml.getElementsByTagName("cProd")
            nome=xml.getElementsByTagName("xProd")
            Quantidaitem=xml.getElementsByTagName("det")
            quantidade=xml.getElementsByTagName("qCom")
            valorcusto=xml.getElementsByTagName("vUnCom")
            valortotal=xml.getElementsByTagName("vProd")
            tipo_unidade=xml.getElementsByTagName("uCom")
            cfop_saida=xml.getElementsByTagName("CFOP")
            cst_saida=xml.getElementsByTagName("CSOSN")
            ncm=xml.getElementsByTagName("NCM")
            for i in range(0, len(codigoBarra)):              
                db.adicionar(f''' insert into tb_nfe_item(id_nota,codigo_barra,descricao_produto,quantidade,
                            valor_custo,valor_total,tipo_unidade,cfop_saida,cst_saida,ncm )values
                         ('{id_nota}','{codigoBarra[i].firstChild.data}','{nome[i].firstChild.data}',
                         '{quantidade[i].firstChild.data}','{float(valorcusto[i].firstChild.data)}','{valortotal[i].firstChild.data}'
                         ,'{tipo_unidade[i].firstChild.data}','{cfop_saida[i].firstChild.data}','{cst_saida[i].firstChild.data}','{ncm[i].firstChild.data}')''')   
            self.FunCarregaItemTablewidegt(id_nota)
    @QtCore.pyqtSlot()
    def FunCarregaItemTablewidegt(self,idnota=None):
        self.FumLimparCampo()
        self.cabecarioNota(idnota)
        
        item_nota=db.pega_dados(f'''select * from tb_nfe_item where id_nota='{idnota}'   ''')
        self.ui.tab_EntradaNota.setRowCount(0)
        for linha,row in enumerate(item_nota):
            self.ui.tab_EntradaNota.insertRow(linha)
            self.ui.tab_EntradaNota.setItem(linha, 0, QTableWidgetItem(str(row[0])))
            self.ui.tab_EntradaNota.setItem(linha, 1, QTableWidgetItem(str(row[2])))#codigo barra
            self.ui.tab_EntradaNota.setItem(linha, 2, QTableWidgetItem(str(row[3])))#descricao
            self.ui.tab_EntradaNota.setItem(linha, 3, QTableWidgetItem(str(row[4])))#quantidade
            self.ui.tab_EntradaNota.setItem(linha, 4, QTableWidgetItem(str("R$ {:.2f}".format(row[5]))))#valor cursto
            self.ui.tab_EntradaNota.setItem(linha, 5, QTableWidgetItem(str("R$ {:.2f}".format(row[6]))))#valototal
            self.ui.tab_EntradaNota.setItem(linha, 6, QTableWidgetItem(str(row[7])))#tipounid
            self.ui.tab_EntradaNota.setItem(linha, 7, QTableWidgetItem(str(row[8])))#cfopsaida
            self.ui.tab_EntradaNota.setItem(linha, 8, QTableWidgetItem(str(row[9])))#cst_entrada
            self.ui.tab_EntradaNota.setItem(linha, 9, QTableWidgetItem(str(row[10])))#ncm
        for linha in range(0, len(item_nota)):#ajuda tamanho
            for linh2 in range(0,9):
                self.ui.tab_EntradaNota.item(linha,linh2).setTextAlignment(Qt.AlignCenter)  
    def cabecarioNota(self,numero):
        ###carregarcabeçario
        try:
            cabecario=db.pega_dados(f'''select * from tb_compra where id_nota='{numero}'   ''')
            
            self.ui.tx_numeroNota.setText(str(cabecario[0][1]))
            self.ui.tx_ChaveNota.setText(str(cabecario[0][2]))
            self.ui.tx_razaoSocial.setText(str(cabecario[0][3]))
            self.ui.tx_cnpj.setText(str(cabecario[0][4]))
            self.ui.tx_numeSerie.setText(str(cabecario[0][5]))
            self.ui.tx_cfop.setText(str(cabecario[0][6]))
            self.ui.tx_ModeloNota.setText(str(cabecario[0][7]))
            for i in cabecario:    
                datacompra=datetime.datetime.strptime(f"{i[15]}","%d/%m/%Y")
                dataentrada=datetime.datetime.strptime(f"{i[16]}","%d/%m/%Y")
                self.ui.dt_dataCompra.setDate(datacompra)
                self.ui.dt_dataEntrada.setDate(dataentrada)
        except:"Erro"
        ####
 
    def funBuscanotaFiscal(self):
        self.ForVisualiNotaEntrada=ForVisualiNotaEntrada()
        def carregaNota():
            try:
                selecionanota=self.ForVisualiNotaEntrada.ui.tb_WidegNotas.selectedItems()[1].text()
                self.FunCarregaItemTablewidegt(selecionanota)
                self.ForVisualiNotaEntrada.close()
            except:error
        self.ForVisualiNotaEntrada.ui.tb_WidegNotas.doubleClicked.connect(carregaNota)    
        self.ForVisualiNotaEntrada.exec_()
        
    
    #edita item nota
    def FunEditarITemNota(self):
        try:
            selecionaid=self.ui.tab_EntradaNota.selectedItems()[0].text()
            selecionumeronota=self.ui.tab_EntradaNota.selectedItems()[0].text()
            item_nota=db.pega_dados(f'''select * from tb_nfe_item where id='{selecionumeronota}'   ''')
            self.ForEditaItem=ForEditaItem(str(selecionaid),str(item_nota[0][1]),self.FunCarregaItemTablewidegt)
            self.ForEditaItem.exec_()
        except:"erro"
  
           
    def FumLimparCampo(self):
        self.ui.tx_razaoSocial.clear()
        self.ui.tx_cnpj.clear()
        self.ui.tx_ChaveNota.clear()
        self.ui.tx_ModeloNota.clear()
        self.ui.tx_cfop.clear()
        self.ui.tx_numeSerie.clear()
        self.ui.tx_numeroNota.clear()
        self.ui.tx_cnpj.clear()