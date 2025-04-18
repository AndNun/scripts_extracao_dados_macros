
# %%
# Importando pacotes
import pandas as pd
import sqlite3
import sys

sys.path.insert(0, "./lib")

import utils

# %%

# Carregando dados variação do ipca mensam
df_ipca_real = utils.consulta_bcb(433)

df_ipca_real.head()

df_ipca_real['dt_inclusao'] = pd.to_datetime('today')
# %%
# Conectando ao banco SQLite (ou criando se não existir)
conexao = sqlite3.connect('macroeconomico.db')

# Salvando o dataframe no banco de dados so SQLite
df_ipca_real.to_sql('ipca_mensal_real', conexao, if_exists = 'append', index = False)

conexao.close()