# %%
import pandas as pd
import sqlite3

import sys

sys.path.insert(0, "C:/Users/AndsonSilva/Desktop/Estudos/repositorios_git/extracao_dados_macroeconomicos/lib")

import utils

# %%
# Criando um dataframe contendo as projeções mensais do ipca
   
df_ipca_proj = utils.exp_proj('ExpectativaMercadoMensais'
         ,'IPCA'
         , 0)

df_ipca_proj.head()

# %%
# Conectando ao banco SQLite (ou criando se não existir)
conexao = sqlite3.connect('db.db')

# Criando um cursor para executar comandos SQL
cursor = conexao.cursor()
print("Conexão estabelecida com sucesso!")

# Criando tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS ipca_projecao_mensal (
    dt_inclusao TEXT,
    Data TEXT,
    DataReferencia TEXT,
    Media TEXT,
    Mediana TEXT,
    Minimo TEXT,
    Maximo TEXT
);
''')

df_ipca_proj['dt_inclusao'] = pd.to_datetime('today')

# Subindo tabela no banco de dados 
df_ipca_proj.to_sql('ipca_projecao_mensal', conexao, if_exists='append', index=False)






