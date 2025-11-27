# Importações
import pandas as pd

# Carregando arquivo CSV e criando DataFrame
df = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\tp03_python_data\files\players_20.csv')

# Exibindo as 5 primeiras linhas
print(f'Exibindo as 5 primeiras linhas: {df.head(5)}')

# Exibindo as colunas disponíveis e total de registros
print(f'Colunas disponíveis: {df.columns}') # Exibi as colunas

print(f'Total de registros: {len(df)}') # Exibe total de registros