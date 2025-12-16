import json
import os
from bs4 import BeautifulSoup

def exportar_e_ler_json():
    caminho_pasta = r"C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\pedro_silva_dr4_at\file"
    nome_arquivo_html = "pagina_original.html"
    nome_arquivo_json = "dados_scraping.json"
    
    caminho_html = os.path.join(caminho_pasta, nome_arquivo_html)
    caminho_json = os.path.join(caminho_pasta, nome_arquivo_json)

    print("--- Etapa 1: Preparando os dados ---")
    lista_dados = []

    try:
        if not os.path.exists(caminho_html):
            raise FileNotFoundError("HTML base não encontrado.")
        
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
                lista_dados.append(dict(zip(headers, valores)))
        
        print(f"Dados prontos na memória: {len(lista_dados)} registros.")

    except Exception as e:
        print(f"Erro na preparação: {e}")
        return

    print("\n--- Etapa 2: Salvando em JSON ---")

    try:
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(lista_dados, f, indent=4, ensure_ascii=False)
        
        print(f"Sucesso! Arquivo JSON criado em: {caminho_json}")

    except IOError as e:
        print(f"Erro de permissão ou disco ao salvar JSON: {e}")
    except Exception as e:
        print(f"Erro genérico ao salvar JSON: {e}")

    print("\n--- Etapa 3: Lendo o arquivo JSON gerado ---")

    try:
        with open(caminho_json, 'r', encoding='utf-8') as f:
            conteudo_lido = json.load(f)

        print("Leitura realizada com sucesso! Exibindo o primeiro registro encontrado no arquivo:")
        if conteudo_lido:
            print(conteudo_lido[0])
        else:
            print("O arquivo JSON está vazio.")

    except json.JSONDecodeError as e:
        print(f"O arquivo existe, mas o JSON está corrompido: {e}")
    except Exception as e:
        print(f"Erro ao ler o arquivo JSON: {e}")

if __name__ == "__main__":
    exportar_e_ler_json()