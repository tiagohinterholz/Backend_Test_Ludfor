# Faça um programa que leia a planilha de excel PLD.xlsx disponibilizada via e-mail e imprima o maior valor de cada submercado por ano.

import pandas as pd

file_path = 'PLD.xlsx' 
df = pd.read_excel(file_path, header=None)  # Carrega sem cabeçalho


df.columns = df.iloc[1]  # Segunda linha = cabeçalho
df = df.drop([0,1])  # Remove as duas primeiras linhas -> cabeçalho e dados desnecessários


df = df.drop([7, 8], axis=0, errors='ignore')  # Remover as linhas B8 e B9 -> Piso e teto do submercado
df_submercados = df.iloc[0:6]  # A partir da linha 1 até 6 estão os submercados

df.set_index('Submercados', inplace=True)
df.columns = pd.to_datetime(df.columns, errors='coerce')

df_transposed = df.T
df_transposed['year'] = df_transposed.index.year

df_grouped = df_transposed.groupby('year').max()

print("Maior valor por submercado por ano:")
for ano in df_grouped.index:
    print(f"\nAno: {ano}")
    for submercado in df_grouped.columns:
        print(f'O maior valor do submercado {submercado} em {ano} é: R$ {df_grouped.loc[ano, submercado]:.2f}')