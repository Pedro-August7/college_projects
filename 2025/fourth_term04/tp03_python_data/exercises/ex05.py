import pandas as pd
import sqlite3

# DataFrame
df = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_20.csv ')

# Conexão com o banco em memória
conn = sqlite3.connect(':memory:')

# DataFrame no banco
df.to_sql('jogadores_20', conn, if_exists='replace', index=False)

jogadores_acora = ['Cristiano Ronaldo', 'Harry Kane', 'Karim Benzema', 'Eden Hazard', 'Neymar Jr']

# Consultando
query = "SELECT * FROM jogadores_20 WHERE " + " OR ".join([f"short_name LIKE '{jogador}'" for jogador in jogadores_acora])

# Consultar dados
cursor = conn.cursor()
cursor.execute(query)

# Pegar todos os resultados da consulta
jogadores_encontrados = cursor.fetchall()

# Verificando se algum jogador foi encontrado
if jogadores_encontrados:

    # Printando os dados dos jogadores encontrados
    for player in jogadores_encontrados:
        sofifa_id = player[0]
        short_name = player[3]
        age = player[4]
        nationality = player[9]
        
        print(f"ID: {sofifa_id}")
        print(f"Nome Completo: {short_name}")
        print(f"Idade: {age}")
        print(f"Nacionalidade: {nationality}\n")
else:
    print("Nenhum jogador encontrado.")

# Fechando conexão
conn.close()
