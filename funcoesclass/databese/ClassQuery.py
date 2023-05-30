
from distutils.log import error
import sqlite3
import io  
import json
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#from SqliteCidade import*
class sqlite_db:
    def __init__(self,banco=None):
        self.conn =None
        self.curso = None
        
        if banco:
            self.open(banco)
        self.createtabelas()
    def open(self,banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            
        except:
           print("banco Off")     

    def adicionar(self,query):#acicionar item
        cur = self.cursor
        cur.execute(query)
        return self.conn.commit()
        
    def update(self,query):#upadte
        cur = self.cursor
        cur.execute(query)
        self.conn.commit() 
    def adicionafoto(self,id=None):
        banco = sqlite3.connect('bancodados/database.db')
        cur = banco.cursor()
        foto="config/logo/logo.png"
        with open(foto,'rb') as file:
                photo=file.read()

        cur.execute(f"update  param set logo_sistema=? where id=? ",(photo,id))
        banco.commit()
    
    def pega_dados(self,query): #selecionar item
        
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()
    
    def apaga(self,query):
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()
        
    def createtabelas(self):
        cur = self.cursor
        #creata table lembrete
        cur.execute('''CREATE TABLE IF NOT EXISTS tb_mesa(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero int,
            id_usuario int,
            nome_usuario varchar(200),
            id_cliente int,
            nome_cliente varchar(200),
            subtotal NUMERIC (18,4),
            total NUMERIC (18,4),
            hr_abertura varchar(200),
            hrfechadura varchar(200)
        
            
            );
           
       
        ''')
        #creata table item mesa
        cur.execute('''CREATE TABLE IF NOT EXISTS tb_item_mesa(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero int,
            cod_barra int,
            descricao char(200),
            quant int,
            vl_unid NUMERIC (18,4),
            vl_total NUMERIC (18,4),
            unidade char(20) 
            
            );
       
        ''')
        #create table
        cur.execute('''CREATE TABLE IF NOT EXISTS param(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_empresa varchar(250),
            cnpj int,
            inscricao int,
            regime_tributario varchar(250),
            razao_social varchar(250),
            nome_fantasia varchar(250),
            cep int,
            endereco varchar(250),
            numero int,
            complemento varchar(250),
            bairro varchar(200),
            cidade varchar(200),
            uf char(2),
            codigo_pais int,
            descpais varchar(250),
            email varchar(250),
            site varchar(250),
            celular_empresa int,
            nome_responsalve varchar(200),
            celular_responsavel varchar(200),
            versao_sistema varchar(50),
            ns_produto varchar(100),
            liberacao varchar(200),
            logo_sistema BLOB           
            );''')
        
        #creata table lembrete
        cur.execute('''CREATE TABLE IF NOT EXISTS lembrete(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text varchar(250),
            cores varchar(250)
            
            );''')
        
        #creata table usuario
        cur.execute('''CREATE TABLE IF NOT EXISTS usuario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome varchar(200) NOT NULL UNIQUE,
            senha varchar(200),
            senha2 varchar(200)
            );
        
        ''')
        
        #creata table tb_pais
        cur.execute('''CREATE TABLE IF NOT EXISTS  tb_pais(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo int,
            descricao varchar(250)
    
            );
        
        ''')
        #creata table usuario
        cur.execute('''CREATE TABLE IF NOT EXISTS tb_funcionario(
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nome varchar(200),
            sobronenome varchar(200),
            cpf int(11),
            cidade varchar(150),
            estado char(2),
            status char(2),
            data_aniversario varchar(200),
            data_cadastro varchar(200),
            codigo_usuario int,
            nome_usuario varchar(200)

            );
        ''')
        
        cur.execute(''' CREATE TABLE IF NOT EXISTS tb_clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome varchar(200),
            sobrenome char(200),
            cpf_cnpj INT,
            rg_inscricao INT,
            celular INT,
            telefone INT ,
            email char(200),
            obs char(500),
            cod_ibge INT,
            cep INT,          
            cidade char(200),
            estado char(2),
            endereco char(500),
            bairro char(120),
            numeroresidencia INT,
            data_emissao varchar(255),
            data_aniversario varchar(255),
            data_ultimaCompra VARCHAR (255),
            pai               VARCHAR (255),
            mae               VARCHAR (255),
            estado_civil      VARCHAR (255),
            situacao          CHAR (1),
            sexo              CHAR (1),
            tipo_cliente      CHAR (1) 


        );''')
        
        cur.execute(''' CREATE TABLE IF NOT EXISTS tb_estoque(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo_barra INT,
            descricao varchar(200),
            unidade varchar(2),
            fonecedor vachar(200),
            marca varchar(200),
            quantidade DOUBLE PRECISION,
            fracao INT,
            valor NUMERIC(18,4),
            obs char(500),
            maximo_prod int,
            minimo_prod int,
            ncm int,
            preco_compra NUMERIC (18,4),
            preco_custo NUMERIC (18,4),
            lucro real,
            codst char(1),
            class_tributaria varchar(100),
            cfop_saida int,
            cst_saida int,
            codgrupo int,
            descricaogrupo varchar(200),
            data_emissao varchar(255),
            ativo char(2)
            
        );''')
        cur.execute(''' CREATE TABLE IF NOT EXISTS grupos(
            codigogrupo INTEGER PRIMARY KEY AUTOINCREMENT,
            
            descricaogrupo varchar(200)
            
            
        );''')
        
        cur.execute(''' CREATE TABLE IF NOT EXISTS tb_fornecedor(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_fantasia char(200),
                    razao_social char(200),
                    cnpj int,
                    inscricao int,
                    telefone int,
                    email char (200),
                    obs char(500),
                    cep int,
                    endereco char(200),
                    numeroresidencia int,
                    bairro char(200),
                    cidade char(200),
                    estado char(2)


        );''')
        cur.execute(''' CREATE TABLE IF NOT EXISTS tb_venda(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nota int,
                    codigo int,
                    nome char(200),
                    quantidade_produto int,
                    forma_pagamento char(20),
                    tipo_documento int,
                    data int,
                    horario int,
                    valortotal NUMERIC (18,4)
                    
        );''')
        cur.execute(''' CREATE TABLE IF NOT EXISTS orcas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nota int,
                    descricao char(200),
                    valortotal NUMERIC (18,4),
                    data_emissao vachar(200),
                    data_final varchar(200),
                    Finalizar VARCHAR(1) 
                    
        );''')
        cur.execute(''' CREATE TABLE IF NOT EXISTS orca(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nota int,
                    cod_barra int,
                    descricao char(200),
                    quantidade int,
                    valor_unit NUMERIC (18,4),
                    valortotal NUMERIC (18,4),
                    data_emissao varchar(200),
                    hora varchar(200),
                    Finalizado char(1),
                    unidade char(20) 
                    
        );''')
      
            
        
        cur.execute(''' CREATE TABLE IF NOT EXISTS tb_planopagamento(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo int,
                    descricao char(200),
                    Quantidade_parcelas int,
                    dias int    );''')
        verifica=self.pega_dados(''' select * from tb_planopagamento''')
        if not verifica:
            self.adicionar(''' INSERT INTO tb_planopagamento (codigo,descricao,Quantidade_parcelas,dias)values ('1','AVISTA','1','1') ''')
        ####################################conta receber
        cur.execute(''' CREATE TABLE IF NOT EXISTS tb_receber(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nota int,
                    documento int,
                    nome char(200),
                    valortotal NUMERIC (18,4),
                    parcelas char(40),
                    data_emissao char(200),
                    data_vencimento char(200),
                    codcliente int
                    );''')
        ####################################conta receber
        cur.execute(''' CREATE TABLE IF NOT EXISTS tb_recebidos(
                    id ,
                    nota int,
                    documento int,
                    codcliente int,
                    nome char(200),
                    valornominal NUMERIC (18,4),
                    desconto NUMERIC (18,4),
                    valortotal NUMERIC (18,4),
                    parcelas char(40),
                    data_emissao char(200),
                    data_vencimento char(200)
                    
                    );''')
        ############################################### caixa
        cur.execute(''' CREATE TABLE IF NOT EXISTS tb_caixa(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nota int,
                    nome char(200),
                    valortotal NUMERIC (18,4),
                    tipodocumento char(40),
                    data_pagamento char(200),
                    cd_doc char(1)
                      );''')
        ####################PEMISSOES USUARIO
        cur.execute('''CREATE TABLE IF NOT EXISTS permissoes_usuario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo_usuario int,
            nome_usuario varchar(200),
            cadastro_clientes char(2),
            cadastro_estoque char(2),
            cadastro_funcionario char(2),
            caixa char(2),
            conta_receber char(2),
            contas_apagar char(2),
            entrada_nota char(2),
            analasievenda char(2),
            cadastro_menu char(2),
            venda_menu char(2),
            financeiro_menu char(2),
            utilitario_menu char(2),
            configuracao_menu char(2),
            cadastro_left char(2),
            fincanceiro_left char(2),
            entrada_nota_left char(2),
            venda_left char(2)
            );
       
        ''')
        #################### nota de compra
        cur.execute('''CREATE TABLE IF NOT EXISTS tb_compra(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_nota int,
            chave_nota int,
            razao_social vachar(200),
            cnpj int,
            serie_nota int,
            cfop_entrada int,
            modelo int,
            cod_pais int,
            pais varchar(200),
            cep int,
            bairro vachar(200),
            municipio vachar(200),
            endereco vachar (200),
            numero_imovel vachar(200),
            data_emissao vachar(150),
            data_entrada vachar(150)
            );
       
        ''')
        #################### nota de compra
        cur.execute('''CREATE TABLE IF NOT EXISTS tb_nfe_item(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_nota int,
            codigo_barra int,
            descricao_produto vachar(200),
            quantidade  NUMERIC (18,4),
            valor_custo NUMERIC (18,4),
            valor_total NUMERIC (18,4),
            tipo_unidade vachar(200),
            cfop_saida int,
            cst_saida int,
            ncm int
            
            );
       
        ''')
        ##############tb_tipodocumento
        cur.execute('''CREATE TABLE IF NOT EXISTS tb_tipodocumento(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo int,
            descricao varchar(200)
            );
       
        ''')
        #class tb_tipodocumento
        cur.execute('''CREATE TABLE IF NOT EXISTS tb_tipodocumento(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codst int,
            descricao_class vachar(200),
            aliquota_st varchar(50)
            
            );
       
        ''')
        
        #class tb_contasapagar
        cur.execute('''CREATE TABLE IF NOT EXISTS tb_contasapagar(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nota varchar(200),
            descricao varchar(200),
            valor  NUMERIC (18,4),
            data_inicial varchar(200),
            data_final varchar(200),
            codigo_fornecedor int,
            fornecedor varchar(200),
            cnpj int
            );
       
        ''')
        
        #class tb_contasapagar
        cur.execute('''CREATE TABLE IF NOT EXISTS tb_classtributaria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codst char(1),
            descricao varchar(200),
            icms varchar(10),
            reg varchar(10)
            );
       
        ''')
    def erro():
        with open("config/config.json", encoding='utf-8') as meu_json:
            dados = json.load(meu_json)  
        data_file_dict =  dados
        lista_ip=[data_file_dict.get('host')]
        caminho_da_pasta = f"{lista_ip[0]}"
        if os.path.isfile(caminho_da_pasta):
            return caminho_da_pasta
        else:
            pass


        


db=sqlite_db(sqlite_db.erro())
