import pandas as pd
import sqlite3

# Carregando CSV
df_21 = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_21.csv')

# Criando e gravando no banco em memória
conn = sqlite3.connect(':memory:')

df_21.to_sql('jogadores_21', conn, if_exists='replace', index=False)

# Consultando
query = """

SELECT
    short_name, overall
FROM 
    jogadores_21
WHERE overall > 88;

"""

cursor = conn.cursor()
cursor.execute(query)

result = cursor.fetchall()

# Printando
clm = [description[0] for description in cursor.description]
df_result = pd.DataFrame(result, columns=clm)

format_text = [f"({name}, {overall})" for name, overall in result]

print("\n".join(format_text))

cursor.close()
conn.close()