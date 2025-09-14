import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('vehicles.csv')

# Mostrar as primeiras linhas do CSV
print(df.head())

# Mostrar os nomes das colunas
print("\nColunas disponíveis no CSV:")
print(df.columns)

