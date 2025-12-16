import csv
import os
from bs4 import BeautifulSoup

def exportar_para_csv():
    caminho_pasta = r"C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\pedro_silva_dr4_at\file"
    nome_arquivo_html = "pagina_original.html"
    nome_arquivo_csv = "dados_scraping.csv"
    
    caminho_html = os.path.join(caminho_pasta, nome_arquivo_html)
    caminho_csv = os.path.join(caminho_pasta, nome_arquivo_csv)

    print("--- Etapa 1: Carregando dados do HTML ---")

    lista_final_dados = [] 

    try:
        if not os.path.exists(caminho_html):
            raise FileNotFoundError("Execute o Exercício 1 para baixar o HTML primeiro.")

        with open(caminho_html, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        tabela = soup.find('table', class_='wikitable')
        if not tabela: tabela = soup.find('table')

        linhas = tabela.find_all('tr')
        headers = [th.get_text(strip=True) for th in linhas[0].find_all('th')]

        for linha in linhas[1:]:
            colunas = linha.find_all(['td', 'th'])
            valores = [col.get_text(strip=True) for col in colunas]
            
            if len(valores) == len(headers):
                lista_final_dados.append(dict(zip(headers, valores)))
        
        print(f"Dados carregados. Registros prontos para escrita: {len(lista_final_dados)}")

    except Exception as e:
        print(f"Erro na preparação dos dados: {e}")
        return
    print("\n--- Etapa 2: Exportando para CSV ---")

    try:
        if not lista_final_dados:
            raise ValueError("A lista de dados está vazia. Nada para salvar.")

        with open(caminho_csv, mode='w', newline='', encoding='utf-8') as arquivo_csv:

            campos = lista_final_dados[0].keys()

            escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

            escritor.writeheader()

            escritor.writerows(lista_final_dados)

        print(f"Sucesso! Arquivo salvo em: {caminho_csv}")

    except IOError as e:
        print(f"Erro de Permissão ou Disco: Não foi possível salvar o arquivo. Detalhes: {e}")
    except Exception as e:
        print(f"Erro inesperado ao criar o CSV: {e}")

if __name__ == "__main__":
    exportar_para_csv()