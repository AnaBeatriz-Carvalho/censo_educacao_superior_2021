import pandas as pd
import os
from dotenv import load_dotenv
import pyodbc
import conexao

consulta = "SELECT * FROM dbo.MICRODADOS_CADASTRO_CURSOS"

resultados = conexao.executar_consulta(consulta)

resultado = pd.read_sql_query(resultados)

print("10 primeiras linhas do DataFrame", resultado.head(10), "\n")
print("10 últimas linhas do DataFrame", resultado.tail(10), "\n")