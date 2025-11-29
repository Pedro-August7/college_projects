import pandas as pd
import sqlite3

# DataFrame
df = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_20.csv ')

# Conexão com o banco em memória
conn = sqlite3.connect(':memory:')

# DataFrame no banco
df.to_sql('jogadores_20', conn, if_exists='replace', index=False)

# Jogadores âncoras
jogadores_ancora = [
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

# Consulta
query = f"""

SELECT
    short_name, pace, shooting, defending 
FROM
    jogadores_20
WHERE 
    short_name IN ({', '.join([f"'{jogador}'" for jogador in jogadores_ancora])})

"""
# Consultando dados
df_result = pd.read_sql_query(query, conn)

# Printando o DataFrame
print(df_result)