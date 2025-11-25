# conexao.py
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from dotenv import load_dotenv

import os

load_dotenv(dotenv_path=r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_work\tp4_project_block\conexoes\.env')

db_user = os.getenv('userenv')
db_password = os.getenv('passwordenv')
db_host = os.getenv('hostenv')
db_door = os.getenv('doorenv')
db_name_db = os.getenv('name_dbenv')


# Função para criar o engine de conexão com o banco de dados
def conexao_eng():
    # Dados DB
    user = db_user
    password = db_password
    host = db_host
    door = db_door
    name_db = db_name_db

    connection_string = f'postgresql+psycopg2://{user}:{password}@{host}:{door}/{name_db}'

    try:
        # Criando o engine de conexão
        engine = create_engine(
            connection_string,
            connect_args={"options": "-c client_encoding=utf8"})
        
        # Teste de conexão
        with engine.connect() as conn:
            result = conn.execute(text('SELECT 1')).fetchone()
            print("\nConexão bem-sucedida! Resultado do SELECT 1:")
        
        return engine
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None