import pandas as pd
import io
from sqlalchemy import create_engine, text

def pipeline_completo_corrigido():
    csv_dados = """id,valor,categoria,descricao
1,250,credito,Deposito realizado no app
2,-100,debito,Pagamento de boleto
3,480,credito,Recebimento TED
4,-50,debito,Compra online
5,1020,credito,Salario mensal
6,-200,debito,Supermercado
"""
    
    df = None 
    conn = None

    print("--- ETAPA 1: Carregamento do CSV ---")
    try:
        arquivo_simulado = io.StringIO(csv_dados)
        df = pd.read_csv(arquivo_simulado)
        print("Arquivo carregado com sucesso!")
        
    except Exception as e:
        print(f"Erro fatal ao ler o CSV: {e}")

    print("\n--- ETAPA 2: Cálculos de Métricas ---")
    if df is not None:
        try:
            media_valor = df["valor"].mean()
        except KeyError:
            print("Erro: Coluna 'valor' não encontrada.")
        else:
            print(f"Média calculada: {media_valor:.2f}")

        try:
            df["origem"].value_counts()
        except KeyError:
            print("Aviso: A coluna 'origem' não existe. Ignorando...")
            pass
    else:
        print("Pulei a Etapa 2 porque o DataFrame está vazio.")

    print("\n--- ETAPA 3: Integração SQL ---")

    try:

        engine = create_engine("sqlite:///meubanco.db")
        conn = engine.connect()
        print("Conexão com o banco estabelecida.")

        try:
            if df is None:
                raise ValueError("Não há dados para salvar (DataFrame nulo).")
            
            df.to_sql("tabela_dados", conn, if_exists="replace", index=False)
        
        except ValueError as ve:
            print(f"Erro de validação: {ve}")
        except Exception as e:
            print(f"Erro ao gravar no banco: {e}")
        else:
            print("Tabela gravada com sucesso!")

            try:
                sql_query = text("SELECT * FROM tabela_dados;")
                consulta = conn.execute(sql_query)
                
                print("\n--- Resultado da Consulta SQL ---")
                for linha in consulta:
                    print(linha)
                    
            except Exception as e:
                print(f"Erro ao executar a consulta SQL: {e}")

    except Exception as e:
        print(f"Erro crítico na conexão com o banco: {e}")
    
    finally:
        if conn:
            conn.close()
            print("\nConexão com o banco encerrada.")

    print("\nPipeline corrigido e executado com sucesso!")

if __name__ == "__main__":
    pipeline_completo_corrigido()