from main import extracao_html_clear
from conexoes import conexao_eng
import psycopg2
from datetime import datetime
from sqlalchemy import create_engine, text

# Criando conexão
engine = conexao_eng()

# Só roda se for o arquivo main
if __name__ == '__main__':
    dados_site = extracao_html_clear()

    if dados_site:
        result = dados_site # Desempacotano

        with engine.connect() as conn:
            try:
                print('Conexão aberta!')

                conn.connection(text("INSERT INTO "))
                
                conn.commit()
                print('Dados Salvos!')
            
            except Exception as e:
                print(f'Erro ao salvar: {e}')

