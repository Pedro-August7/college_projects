# Importações
import pandas as pd
import sqlite3

# Carregando CSV
df_20 = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_20.csv')
df_21 = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_21.csv')

# Criando db
conn= sqlite3.connect(':memory:')

df_20.to_sql('jogadores_20', conn, if_exists='replace', index=False)
df_21.to_sql('jogadores_21', conn, if_exists='replace', index=False)

# Consultando
query= """

SELECT
    j20.*
FROM
    jogadores_20 j20
INNER JOIN jogadores_21 j21 ON j20.sofifa_id = j21.sofifa_id
LIMIT 100

"""

# Executando
result = pd.read_sql(query, conn)

# Printando
print(result)