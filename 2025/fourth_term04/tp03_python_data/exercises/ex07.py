import pandas as pd
import sqlite3

# Carregando o CSV
df = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_20.csv')

# Agrupando
cl_player_positions = df["player_positions"]

# Printando 20 resultados
print(f'Exibindo os 10 primeiros resultados:\n{cl_player_positions.head(10)}\n')

# Calculando a média
media_overall = round(df['overall'].mean(), 2)

media_potential = round(df['potential'].mean(), 2)

media_age = round(df['age'].mean(), 2)

print('\n=== MÉDIAS ===')
print(f'A média de overall é: {media_overall}')
print(f'A média de potential é: {media_potential}')
print(f'A média de age é: {media_age}')

# Ordenando pelo overall
df_sorted = df.sort_values(by='overall', ascending=False)

print('\n=== JOGADORES ORDENAÇÃO POR OVERALL ===')
print(df_sorted[['short_name', 'overall']].head(10))