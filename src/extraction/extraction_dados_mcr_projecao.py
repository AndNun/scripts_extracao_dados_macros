# %%
import pandas as pd
import sqlite3

import sys

sys.path.insert(0, "./lib")

import utils

# %%
# Criando um dataframe contendo as projeções mensais do ipca
   
df_ipca_proj = utils.exp_proj('ExpectativaMercadoMensais'
         ,'IPCA'
         , 0)

df_ipca_proj.head()

df_ipca_proj['dt_inclusao'] = pd.to_datetime('today')

# %%
# Conectando ao banco SQLite (ou criando se não existir)
conexao = sqlite3.connect('macroeconomico.db')

# Salvando o dataframe no banco de dados so SQLite
df_ipca_proj.to_sql('ipca_mensal_projecao', conexao, if_exists = 'append', index = False)

conexao.close()

