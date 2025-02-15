import pandas as pd
from app.notafiscal import NotaFiscal

def prever_nota(nota: NotaFiscal, modelo):
    # Converter a entrada para DataFrame
    df_nota = pd.DataFrame([nota.dict()])
    df_nota['iss_retention'] = df_nota['iss_retention'].astype(int)
    df_nota['opting_for_simples_nacional'] = df_nota['opting_for_simples_nacional'].astype(int)
    # Fazer a predição
    predicao = modelo.predict(df_nota)[0]

    return "valid" if predicao == 1 else "not valid"

