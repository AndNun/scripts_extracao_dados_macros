# %%
import pandas as pd
import sqlite3

import sys

sys.path.insert(0, "./src/lib")

import utils

# %%
# Carregando dados projeções ipca mensal
df_ipca_proj = utils.exp_proj('ExpectativaMercadoMensais'
         ,'IPCA'
         , 0)

df_ipca_proj.head()

df_ipca_proj['dt_inclusao'] = pd.to_datetime('today')

# Carregando dados reais ipca mensal
df_ipca_real = utils.consulta_bcb(433)

df_ipca_real.head()

df_ipca_real['dt_inclusao'] = pd.to_datetime('today')
# %%
# Conectando ao banco SQLite (ou criando se não existir)
conexao = sqlite3.connect('data/macroeconomico.db')

# Salvando o dataframe no banco de dados so SQLite
df_ipca_real.to_sql('ipca_mensal_real', conexao, if_exists = 'append', index = False)
df_ipca_proj.to_sql('ipca_mensal_projecao', conexao, if_exists = 'append', index = False)

# Fechando conexão
conexao.close()