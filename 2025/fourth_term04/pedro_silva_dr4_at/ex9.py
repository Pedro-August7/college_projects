import pandas as pd
from sqlalchemy import create_engine, text
import os

def integrar_sql_memoria():
    caminho_pasta = r"C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\pedro_silva_dr4_at\file"
    nome_arquivo_csv = "dados_scraping.csv"
    caminho_completo = os.path.join(caminho_pasta, nome_arquivo_csv)

    print("--- Iniciando Integração SQL ---")

    try:
        engine = create_engine('sqlite:///:memory:')
        print("Engine SQLite criada com sucesso (em memória).")

        if not os.path.exists(caminho_completo):
            raise FileNotFoundError("CSV não encontrado. Execute o Exercício 4.")
            
        df = pd.read_csv(caminho_completo)
        print(f"CSV carregado: {len(df)} registros.")

        df.to_sql('tabela_scraping', engine, index=False, if_exists='replace')
        print("Tabela SQL 'tabela_scraping' criada e populada.")

        coluna_ordenacao = df.columns[0] 
        query = f'SELECT * FROM tabela_scraping ORDER BY "{coluna_ordenacao}" LIMIT 3'
        
        print(f"\n--- Executando Query: {query} ---")

        df_resultado = pd.read_sql_query(query, engine)

        print(df_resultado)

    except ImportError:
        print("Erro: A biblioteca 'sqlalchemy' não está instalada.")
        print("Execute: pip install sqlalchemy")
    except Exception as e:
        print(f"Erro no processo SQL: {e}")

if __name__ == "__main__":
    integrar_sql_memoria()