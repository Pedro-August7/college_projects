# Importações
import pandas as pd

# Carregando arquivo CSV / DataFrame
df_play20 = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_20.csv')

df_play21 = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_21.csv')

nome_01 = df_play20['long_name'].tolist()
nome_02 = df_play21['long_name'].tolist()

# Conjuntos com o nome dos jogadores
conjunto01 = set(nome_01)
conjunto02 = set(nome_02)

# Encontrando a inteseção
jogadores_comum = pd.merge(df_play20, df_play21, on='long_name')

# Exibindo os 10 primeiros nomes comuns
for i, player in enumerate(jogadores_comum['long_name'][:10]):
    if i == 0:
        print('Lista dos 10 primeiros nomes comuns: ')
    print(player)