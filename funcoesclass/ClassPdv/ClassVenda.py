from  funcoesclass.databese.ClassQuery import*
from  funcoesclass.ClassQMessageBox.ClassQmessagebox import *

class sis:
    def __init__(self):
        pass
    def FunVerificaOrca(self):#essa funçao cria numero nota
        bancoorca=db.pega_dados(""" select nota FROM numeroorca ORDER BY nota DESC LIMIT 1""")    
        b=int(1)
        for i in bancoorca:
            c=i[0]
            c+=b
            db.adicionar(f''' INSERT INTO numeroorca (nota)values ('{c}') ''')
            pega=db.pega_dados(""" select nota FROM numeroorca ORDER BY nota DESC LIMIT 1""")   
            return pega[0][0]
    
    def FunVerificaQuantidadeTable(self):#essa funçao busca dentro da tabela orca quantos item tem mesma nota
        try:
            banco=db.pega_dados(f''' SELECT * FROM orca where nota='{self.ui.tx_Cod_2.text()}' ''')
            
        except:
            Mensagem.mensagem(self,"Erro","Erro leitura ITem")
        return len(banco)
    def tipdocumento(self):#puxa tipo de documentos
        #pega tipo documento
        documento=db.pega_dados(''' select descricao from tb_tipodocumento ''')
        documetos = [item[0] for item in documento]
        self.ui.cb_tipoDocumento.addItems(documetos)
        
        form = db.pega_dados(f'''SELECT descricao FROM tb_planopagamento  ''')
        formapagamento = [item[0] for item in form]
        self.ui.cb_FormaPagamento.addItems(formapagamento)
        
    def FunVerificaValorTotalVenda(self):#essa funçao somar valor orca 
        try:
            banco=db.pega_dados(f'''SELECT SUM(valortotal*quantidade) FROM ORCA where nota='{self.ui.tx_Cod_2.text()}' ''')
            a_float = int(banco[0][0])
            valortotalfinal=f'{a_float:.2f}'
         
        except:
            self.ui.tx_valoTotalVenda.clear()#somar coluar venda
        return valortotalfinal


    def BaixaEstoque(self):
        self.descricao=str(self.ui.tx_BuscaItem_2.text())
        self.quantidadeItem=str(self.ui.tx_QUANTIDADE_3.text())
        valor=int(float(self.quantidadeItem))
        banco=db.adicionar(f'''UPDATE tb_estoque SET quantidade =quantidade -'{valor}' where codigo_barra='{self.descricao}' or descricao='{self.descricao}' ''')
      
        return banco