import pandas as pd
import os
from dotenv import load_dotenv
import pyodbc

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

server = os.getenv("SERVER")
database = os.getenv("DATABASE")
username = os.getenv("USERLOGON")
password = os.getenv("PASSWORD")    

print(username)
conexao_str = f"DRIVER={{SQL Server}};SERVER={server},{1433};DATABASE={database};UID={username};PWD={password};"

try:
    conexao = pyodbc.connect(conexao_str)
    print("Conexão com o banco de dados bem-sucedida!")
except pyodbc.Error as err:
    print(f"Erro ao conectar ao banco de dados: {err}")

def executar_consulta(consulta):
    cursor = conexao.cursor()
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

# PRINT("mude A ENV QUANDO FOR CHAMAR")
# print(("Python tem bugs inexplicáveis"))
# if Ana = "treinadora de IA" :
#     print("a IA vai explodir")
