from datetime import date
import mysql.connector
import os

db_connection = mysql.connector.connect(host="localhost", user="root", passwd="toor", database="anlix")
cursor = db_connection.cursor()
query = "SHOW TABLES LIKE 'pacientes'; "
cursor.execute(query)


dir_dados='./dados'
for diretorio, subpastas, arquivos in os.walk(dir_dados):
    for arquivo in arquivos:
        tabela=diretorio.replace(dir_dados+'\\' , "")   

        #print(os.path.join(diretorio,arquivo))
        data,ext = os.path.splitext(arquivo)
        if ext == '':
            file=open(os.path.join(diretorio,arquivo),encoding="utf8")
            file = file.read()
            linhas = file.split('\n')
            linhas[0]=linhas[0].strip()
            print(linhas[0])
            for linha in linhas:
                linha = linha.split(' ')
                if len(linha) == 3:
                    query= 'INSERT INTO '+tabela+' (CPF,EPOC,ind_pulm,data) VALUES("'+linha[0]+'",'+linha[1]+','+linha[2]+r', STR_TO_DATE("'+arquivo+'", "%d%m%Y"));'
                    
                  
 
                
