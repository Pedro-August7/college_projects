import pandas as pd
import io

def carregar_e_tratar_csv():

    csv_dados = """id,valor,categoria,descricao
1,250,credito,Deposito realizado no app
2,-100,debito,Pagamento de boleto
3,480,credito,Recebimento TED
4,-50,debito,Compra online
5,1020,credito,Salario mensal
6,-200,debito,Supermercado
"""
    df = None

    print("--- ETAPA 1: Carregamento do CSV ---")
    try:

        arquivo_simulado = io.StringIO(csv_dados)
        df = pd.read_csv(arquivo_simulado)
        
        print("Arquivo carregado com sucesso!")
        print("\n--- Visualização Inicial ---")
        print(df.head())
        
    except Exception as e:
        print(f"Erro fatal ao ler o CSV: {e}")
        return

    print("\n--- ETAPA 2: Cálculos de Métricas ---")


    try:

        media_valor = df["valor"].mean()
    except KeyError:

        print("Erro: A coluna 'valor' não foi encontrada no DataFrame.")
    else:

        print(f"Média calculada (Coluna 'valor'): {media_valor:.2f}")

    try:

        media_categoria = df["origem"].value_counts()
        print("Contagem 'origem':", media_categoria)
    except KeyError:

        print("Aviso: A coluna 'origem' não existe. Ignorando esta etapa...")
        pass

if __name__ == "__main__":
    carregar_e_tratar_csv()