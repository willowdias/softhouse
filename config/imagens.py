import os
upload_img = f'{os.getcwd()}/FotosClientes'
def recupera_imagem(id):
    for nome_arquivo in os.listdir(upload_img):
        
        if f'{id}' in nome_arquivo:#verifica se img na pasta
            print(nome_arquivo)
                
                
   
    
