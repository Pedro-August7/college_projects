from bs4 import BeautifulSoup
import os

def extrair_tabela_jogos():
    caminho_pasta = r"C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\pedro_silva_dr4_at\file"
    nome_arquivo = "pagina_original.html"
    caminho_completo = os.path.join(caminho_pasta, nome_arquivo)

    print(f"Lendo arquivo em: {caminho_completo}\n")

    try:
        if not os.path.exists(caminho_completo):
            raise FileNotFoundError("O arquivo pagina_original.html não foi encontrado. Execute o exercício 1 primeiro.")

        with open(caminho_completo, 'r', encoding='utf-8') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        tabela = soup.find('table', class_='wikitable')
        
        if not tabela:
            tabela = soup.find('table')

        if not tabela:
            raise Exception("Não foi possível encontrar nenhuma tabela estruturada na página.")

        lista_dados = []
        
        linhas = tabela.find_all('tr')
        
        headers = [th.get_text(strip=True) for th in linhas[0].find_all('th')]

        for linha in linhas[1:]:
            colunas = linha.find_all(['td', 'th'])
            
            valores = [col.get_text(strip=True) for col in colunas]

            if len(valores) == len(headers):
                dicionario_linha = dict(zip(headers, valores))
                lista_dados.append(dicionario_linha)

        print(f"Total de registros extraídos: {len(lista_dados)}")
        print("=== Primeiros 5 Registros ===\n")
        
        for i, item in enumerate(lista_dados[:5], 1):
            print(f"Registro {i}: {item}")

    except FileNotFoundError as e:
        print(f"Erro de Arquivo: {e}")
    except Exception as e:
        print(f"Erro durante o processamento: {e}")

if __name__ == "__main__":
    extrair_tabela_jogos()