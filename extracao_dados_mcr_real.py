
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

#%%
# Conectando ao banco SQLite (ou criando se não existir)
conexao = sqlite3.connect('db.db')

# Criando um cursor para executar comandos SQL
cursor = conexao.cursor()
print("Conexão estabelecida com sucesso!")

#%%
# Criando tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS ipca_mensal_real (
    data TEXT,
    valor TEXT,
    dt_inclusao TEXT

);
''')

df_ipca_real['dt_inclusao'] = pd.to_datetime('today')
# Inserindo o DataFrame no banco
df_ipca_real.to_sql('ipca_mensal_real', conexao, if_exists='append', index=False)


