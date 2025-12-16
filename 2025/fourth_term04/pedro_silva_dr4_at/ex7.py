import pandas as pd
import os

def manipular_json_pandas():

    caminho_pasta = r"C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\pedro_silva_dr4_at\file"
    nome_arquivo_json = "dados_scraping.json"
    caminho_completo = os.path.join(caminho_pasta, nome_arquivo_json)

    print(f"Carregando JSON de: {caminho_completo}")

    try:
        if not os.path.exists(caminho_completo):
            raise FileNotFoundError("O arquivo JSON não foi encontrado. Execute o Exercício 5 primeiro.")

        df = pd.read_json(caminho_completo)

        print("\n--- Colunas Originais ---")
        print(df.columns.tolist())

        mapa_de_colunas = {
            "Game": "Nome do Jogo",
            "Publisher(s)": "Empresa",
            "Release date": "Lançamento",
            "Player count": "Jogadores",
            "Rank": "Posição"
        }

        df.rename(columns=mapa_de_colunas, inplace=True)

        print("\n--- Colunas Renomeadas ---")
        print(df.columns.tolist())

        termo_filtro = "Tencent"

        if "Empresa" in df.columns:
            filtro = df['Empresa'].str.contains(termo_filtro, case=False, na=False)
            df_filtrado = df[filtro]

            print(f"\n--- Resultado do Filtro: Jogos da '{termo_filtro}' ---")
            
            if not df_filtrado.empty:
                print(df_filtrado[["Nome do Jogo", "Empresa"]])
            else:
                print(f"Nenhum jogo encontrado para a empresa: {termo_filtro}")
        else:
            print("A coluna 'Empresa' não foi encontrada. Verifique os nomes originais.")

    except ValueError as e:
        print(f"\nErro de Valor/JSON: {e}")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

if __name__ == "__main__":
    manipular_json_pandas()