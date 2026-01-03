import pandas as pd

CAMINHO_EXCEL = "data/entrada/dados_exemplo.xlsx"
CAMINHO_SAIDA = "data/saida/dados_consolidados.csv"

def ler_e_unificar_abas(caminho_excel):
    abas = pd.read_excel(caminho_excel, sheet_name=None)
    lista_dfs = []

    for nome_aba, df in abas.items():
        df["aba_origem"] = nome_aba
        lista_dfs.append(df)

    return pd.concat(lista_dfs, ignore_index=True)

def normalizar_colunas(df):
    #padronizar nomes das colunas
    df.columns = (
        df.columns.str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )
    return df

def tratar_dados(df):
    #tratamento basico para remover linhas vazias
    df = df.dropna(how="all")
    df["cidade"] = df["cidade"].fillna("Não informado")
    return df

def main():
    print("Iniciando tratamento de dados...")
    df = ler_e_unificar_abas(CAMINHO_EXCEL)
    print("Abas unificadas!")
    df = normalizar_colunas(df)
    print("Colunas normalizadas!")
    df = tratar_dados(df)
    print("Dados tratados!")
    df.to_csv(CAMINHO_SAIDA, index=False, encoding="utf-8-sig")
    print("CSV gerado com sucesso!")

if __name__ == "__main__":
    main()
