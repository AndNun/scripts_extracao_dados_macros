import pandas as pd
import requests
from bcb import Expectativas
expec = Expectativas()

# Criando função para consulta 
def consulta_bcb(codigo_bcb):
    
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo_bcb)
    df = pd.read_json(url)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    return df

# Criando função para capturar os dados referente as projeções

def exp_proj(tipo_exp = '', indicador = '', basecalculo = 0):

    ep = expec.get_endpoint(tipo_exp)
    
    df_ind = ep.query().filter(ep.Indicador == indicador).collect()
    
    df_ind_elegivel = df_ind.loc[(df_ind['baseCalculo'] == basecalculo)][['Data'
                                                                        , 'DataReferencia'
                                                                        , 'Media'
                                                                        , 'Mediana'
                                                                        , 'Minimo'
                                                                        , 'Maximo']].copy()
    return(df_ind_elegivel)