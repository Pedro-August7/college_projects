import pandas as pd
import os

def leitura_eficiente_csv():
    caminho_pasta = r"C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\pedro_silva_dr4_at\file"
    nome_arquivo_csv = "dados_scraping.csv"
    caminho_completo = os.path.join(caminho_pasta, nome_arquivo_csv)

    print(f"Lendo arquivo: {caminho_completo}")

    try:
        if not os.path.exists(caminho_completo):
            raise FileNotFoundError("O arquivo CSV não foi encontrado. Execute o Exercício 4 primeiro.")

        colunas_para_ler = ["Game", "Release date"]

        print(f"\n--- Carregando apenas as colunas: {colunas_para_ler} ---")
        df = pd.read_csv(caminho_completo, usecols=colunas_para_ler)

        print("\n--- Primeiras 5 linhas (Dados Brutos) ---")
        print(df.head())

        coluna_ordenacao = "Game"
        print(f"\n--- Ordenando pelo campo '{coluna_ordenacao}' ---")
        
        df_ordenado = df.sort_values(by=coluna_ordenacao, ascending=True)

        print(df_ordenado)

        print("\n--- Informações do DataFrame ---")
        df.info()

    except ValueError as e:
        print(f"\nErro de Coluna: {e}")
        print("Dica: Verifique se os nomes das colunas no código batem EXATAMENTE com o cabeçalho do seu CSV.")
    except FileNotFoundError as e:
        print(f"\nErro de Arquivo: {e}")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

if __name__ == "__main__":
    leitura_eficiente_csv()