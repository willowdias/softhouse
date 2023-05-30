
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from funcoesclass.databese.ClassQuery import*
class FichaCadastro:
    def __init__(self,id): 
        
        self.id=id
        banco=db.pega_dados(f'''select *from tb_clientes where id='{self.id}' ''')

        for i in banco:
            self.carregar(i[1])
       
    def carregar(self,nome=None,cpf=None,rg=None,Endereco=None,numero=None,cidade=None,cep=None,data=None):
        from reportlab.pdfgen import canvas   
      
            
        canvas = canvas.Canvas(f"config/pdf/FichaCadastro.pdf")
        run=0
        for i in range(1):
                
            run+=1#aferi parcela
            canvas.drawString(10, 12, f"{data}")#
                ###########################
                #textual
            textLines = [
            f'Seja Bem Vindo {(nome)}  ',
                'Ao Nosso Cadastro.', 
                    ]
            text = canvas.beginText(50, 800)
            text.setFont("Courier", 18)
            text.setFillColor(colors.red)
            for line in textLines:
                text.textLine(line)
            canvas.drawText(text)
                #############################
                #coloca linha no texto
            canvas.line(5,830,5,8)#linha lateral esquerda
            canvas.line(592,10,5,10) #linha inferior
            canvas.line(592,830,5,830) #linha superio
            canvas.line(592,830,590,8)#linha lateral esquerda
                
                #cabeçario
            canvas.setFillColor(colors.black)
            canvas.drawString(180, 700, f"Ficha Cadastro")
            canvas.drawString(10, 695,f"_"*53)
                #fonte
            canvas.setFont("Courier", 12)
            canvas.setFillColorRGB(0, 0, 0)
            canvas.drawString(10, 670, f"Nome: {(nome)}  ")#nome cliente
            canvas.setFillColor(colors.red)#color fonte
            canvas.drawString(300, 670, f"CPF/CNPJ:{cpf}")#CPF
            canvas.drawString(450, 670, f"RG/IE:{rg}")#rg
            canvas.setFillColor(colors.black)#color fonte
            canvas.drawString(10, 650, f"Endereço: {Endereco}")#Endereco
            canvas.drawString(420, 650, f"Numero: {numero}")#numero casa
                
            canvas.setFont("Courier", 11)
            canvas.drawString(10, 630, f"Cidade: {cidade}")#Nome cidades
            canvas.drawString(260, 630, f"CEP:{cep}")#CEP
                
            canvas.setFont("Courier", 18)
            canvas.setFillColor(colors.black)
            canvas.drawString(10, 600, f"_"*53)#linha separamento
                #essa funçao deixa coloca fundo pdf
            canvas.setFillColorRGB(60, 0, 0 ,alpha=0.5)
            canvas.rect(10,545,574,50, fill=True, stroke=False)
                
            canvas.setFillColor(colors.white)#color fonte
            canvas.setFont("Helvetica", 14)
            canvas.drawString(10, 580, f"Pai: Eliasa *******")#nome do pai
            canvas.drawString(200, 580, f"Mae: REGINA *****************")#nome do pai
            canvas.drawString(420, 580, f"Estado: Civil:Solteiro")#nome da mae
            canvas.drawString(10, 560, f"Sexo: Masculino")#sexo
            canvas.drawString(200, 560, f"Data Nascimento: 05/06/1998")#nascimento
            canvas.drawString(420, 560, f"Data Cadastro:05/06/1998")#data cadastro
                
            canvas.line(195,550,195,596)#linha esquerda
            canvas.line(417,550,417,596)#linha lateral esquerda meio tamanho
            canvas.setFont("Courier", 18)
            canvas.setFillColor(colors.black)
            canvas.drawString(10, 548, f"_"*53)#linha separamento
            canvas.setFont("Courier", 11)


                #ASSINATURA CLIENTE()
            canvas.setFont('Helvetica', 11)
            canvas.drawString(120, 80, f"__________"*5)#CEP
            canvas.drawString(120, 65, f"Assinatura Do Senhor : {(nome)}")#CEP
            canvas.showPage()
            
        canvas.save()        
                                    
            

#FichaCadastro('lucas lucas')