# Importações
import pandas as pd

# Carregando arquivo CSV e criando DataFrame
df_anchor_20 = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\tp03_python_data\files\players_20.csv')

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

rst = df_anchor_20[df_anchor_20['long_name'].isin(jogadores_acora)]

#print(rst)

# Exibindo tamanho final da tabela
print(f'Linhas: {df_anchor_20.shape[0]}', f' Colunas: {df_anchor_20.shape[1]}')