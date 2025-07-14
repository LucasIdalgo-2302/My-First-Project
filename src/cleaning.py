import pandas as pd
import numpy as np

# Lê o arquivo CSV do projeto
df = pd.read_csv("data/processed/alunos_limpos.csv")

print("\n Dataset original:")
print(df.head())

# 1 Identificar valores ausentes
print("\nValores ausentes por coluna:")
print(df.isnull().sum())

# 2 Tratar valores ausentes:
# Substituir NaN em 'nota' pela média das notas
if 'nota' in df.columns:
    nota_media = df['nota'].mean()
    df['nota'] = df['nota'].fillna(nota_media)

# Substituir NaN em 'idade' pela mediana das idades
if 'idade' in df.columns:
    idade_mediana = df['idade'].median()
    df['idade'] = df['idade'].fillna(idade_mediana)

# 3 Ajustar tipos de dados (exemplo: garantir que 'nota' e 'idade' sejam numéricos)
df['nota'] = pd.to_numeric(df['nota'], errors='coerce')
df['idade'] = pd.to_numeric(df['idade'], errors='coerce')

print("\n Dataset após tratamento de valores ausentes e tipos ajustados:")
print(df.head())

# 4 Remover duplicatas
df = df.drop_duplicates()

print("\n Dataset sem duplicatas:")
print(df.head())

# 5 Exemplo: padronizar valores incosistentes na coluna 'sexo'
if 'sexo' in df.columns:
    df['sexo'] = df['sexo'].replace({'feminino': 'F', 'Masculino': 'M', 'female': 'F', 'male': 'M'})

print("\n Dataset final tratado:")
print(df.head())

#Opcional: Salvar arquivo limpo novamente
df.to_csv("data/processed/alunos_tratados.csv", index=False)
print("\n Dataset tratado salvo como 'alunos_tratados.csv'")

