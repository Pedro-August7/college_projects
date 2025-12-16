import pandas as pd
import os

def gerar_relatorio_excel():

    caminho_pasta = r"C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\pedro_silva_dr4_at\file"
    nome_arquivo_json = "dados_scraping.json"
    nome_arquivo_excel = "relatorio_final.xlsx"
    
    caminho_json = os.path.join(caminho_pasta, nome_arquivo_json)
    caminho_excel = os.path.join(caminho_pasta, nome_arquivo_excel)

    print("--- Preparando dados para o Relatório Excel ---")

    try:

        if not os.path.exists(caminho_json):
            raise FileNotFoundError("JSON de origem não encontrado. Execute o Exercício 5.")

        df = pd.read_json(caminho_json)

        df.rename(columns={
            "Game": "Nome do Jogo",
            "Publisher(s)": "Empresa",
            "Release date": "Lançamento",
            "Player count": "Total de Jogadores",
            "Rank": "Posição"
        }, inplace=True)

        print(f"Dados carregados: {len(df)} registros.")

        df.to_excel(caminho_excel, index=False, engine='openpyxl')

        print(f"\nSucesso! Relatório salvo em: {caminho_excel}")

    except ImportError as e:
        print("\nERRO DE BIBLIOTECA:")
    except PermissionError:
        print("\nERRO DE PERMISSÃO:")
        print("O arquivo Excel parece estar aberto. Feche o Excel e tente novamente.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

if __name__ == "__main__":
    gerar_relatorio_excel()