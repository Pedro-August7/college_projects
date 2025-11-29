# Importações
import pandas as pd
import sqlite3

# Carregando CSV
df_20 = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_20.csv')
df_21 = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_21.csv')

# Jogadores âncoras
jogadores_acora = [
    "Cristiano Ronaldo",
    "Lionel Messi",
    "Neymar Jr",
    "Kylian Mbappé",
    "Kevin De Bruyne",
    "Mohamed Salah",
    "Robert Lewandowski",
    "Sergio Ramos",
    "Virgil van Dijk",
    "Luka Modric",
    "Toni Kroos",
    "Eden Hazard",
    "Luis Suárez",
    "Manuel Neuer",
    "Harry Kane",
    "Paulo Dybala",
    "Giorgio Chiellini",
    "Karim Benzema",
    "Antoine Griezmann",
    "Marc-André ter Stegen"
    ]

# Criando DataFrame consolidando informações

df_20_filter  = df_20[df_20['short_name'].isin(jogadores_acora)]
df_21_filter  = df_21[df_21['short_name'].isin(jogadores_acora)]

print('\n=== Filtrando Jogadores Âncora ===')

print(f'Jogadores em 2020: {len(df_20_filter)}')
print(f'Jogadores em 2020: {len(df_21_filter)}')

print('\n=== Renomeando e Selecionando Colunas ===')

df_20_final = df_20_filter[['short_name', 'overall', 'potential']].copy()
df_20_final.rename(columns={'overall': 'overall_20', 'potential': 'potential_20'}, inplace=True)
print('Colunas 2020 renomeadas.')

df_21_final = df_21_filter[['short_name', 'overall', 'potential']].copy()
df_21_final.rename(columns={'overall': 'overall_21','potential': 'potential_21'}, inplace=True)
print('Colunas 2021 renomeadas.')

df_consolidado = pd.merge(df_20_final, df_21_final, on='short_name', how='inner')
print(f'DataFrame Consolidado criado. Total de jogadores: {len(df_consolidado)}')

print('\n=== Resultado Final ===')

# Exibe o DataFrame consolidado
print(df_consolidado)