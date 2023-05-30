from fpdf import FPDF
from funcoesclass.databese.ClassQuery import*



class relatorioitem:
    def __init__(self,Tablewo=None,valortotal=None,dataHora=None): 
        numero = '123456'
        data_emissao = f'{str(dataHora)}'
        # Criação do objeto FPDF
        pdf = FPDF()
        #pdf = FPDF('P', 'mm', (100, 150))#coloca tamanho
        pdf.add_page()
        # Configuração da fonte
        pdf.set_font('Arial', 'B', 10)
       
        # Cabeçalho
        pdf.cell(0, 10, 'NFC-e número {}'.format(numero), 0, 1)
        pdf.cell(0, 10, 'Emissão: {}'.format(data_emissao), 0, 1)

        # Tabela com os dados da NFC-e
        pdf.ln(10)
        pdf.cell(100, 10, 'Descrição', 1)
        pdf.cell(25, 10, 'Quantidade', 1)
        pdf.cell(25, 10, 'Valor Unitário', 1)
        pdf.cell(25, 10, 'Valor Total', 1)
        pdf.ln()
      
        for i in range(Tablewo.rowCount()):
            descriçao=(Tablewo.item(i, 1).text())
            qnt=(Tablewo.item(i, 2).text())    
            valorunid=(Tablewo.item(i, 3).text()).replace('R','').replace('$','')
            valort=(Tablewo.item(i, 4).text()).replace('R','').replace('$','')
            pdf.cell(100, 10, f'{descriçao}', 1)
            pdf.cell(25, 10, f'{qnt}', 1)#quantidade
            pdf.cell(25, 10, f'R${valorunid} ', 1)#valor
            pdf.cell(25, 10, f'{valort}', 1)
            pdf.ln()
        
        
      
        pdf.cell(100, 10, 'ok', 1)
        pdf.cell(25, 10, f'Quant 15', 1)
        pdf.cell(25, 10, f'R$ {str(valortotal)}', 1)
        pdf.cell(25, 10, f'R$ {str(valortotal)}', 1)
        pdf.ln()

        # Salvando o PDF
        pdf.output('config/relatoriopdv/itemvenda.pdf', 'F')

