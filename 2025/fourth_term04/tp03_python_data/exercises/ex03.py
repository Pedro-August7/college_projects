# importações 
import pandas as pd

# Carregando arquivo CSV / DataFrame
df_play20 = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_20.csv')

df_play21 = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_21.csv')

# Filtrando jogadores âncoras
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

rst = df_play20[df_play20['long_name'].isin(jogadores_acora)]
rst = df_play21[df_play21['long_name'].isin(jogadores_acora)]

# Exibindo tamanho final da tabela
print('\n=== Player 20 ===\n')
rst = df_play20[df_play20['long_name'].isin(jogadores_acora)]

print(rst)

print('\n=== Player 21 ===\n')
rst2 = df_play21[df_play21['long_name'].isin(jogadores_acora)]

print(rst2)

# Realizando merge nos campos
rst = pd.merge(df_play20, df_play21, on=['short_name', 'long_name'], how='inner')

rst = rst[['short_name', 'long_name']]

print(f"\n{'===' *10}\nMerger dos dois DataFrame\n{'===' *10}\n")

print(rst)

# Agregação
consolidando = df_play20.groupby('age')[['overall', 'potential']].mean().reset_index()
consolidando2 = df_play21.groupby('age')[['overall', 'potential']].mean().reset_index()

print(f"\n{'===' *10}\nConsolidando\n{'===' *10}")

strings = ['', 'Players 20', '', consolidando.to_string(), '', 'Players 21', '', consolidando2.to_string()]
out = "\n".join(strings)
print(out)
