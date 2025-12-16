from bs4 import BeautifulSoup
import os

def processar_dados_jogos():
    caminho_pasta = r"C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\pedro_silva_dr4_at\file"
    nome_arquivo = "pagina_original.html"
    caminho_completo = os.path.join(caminho_pasta, nome_arquivo)

    print(f"Processando arquivo: {caminho_completo}\n")

    try:
        if not os.path.exists(caminho_completo):
            raise FileNotFoundError("Arquivo HTML não encontrado.")

        with open(caminho_completo, 'r', encoding='utf-8') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        
        tabela = soup.find('table', class_='wikitable')
        if not tabela:
            tabela = soup.find('table')
            
        if not tabela:
            raise Exception("Tabela não encontrada.")

        lista_dados = []
        linhas = tabela.find_all('tr')
        headers = [th.get_text(strip=True) for th in linhas[0].find_all('th')]

        for linha in linhas[1:]:
            colunas = linha.find_all(['td', 'th'])
            valores = [col.get_text(strip=True) for col in colunas]
            
            if len(valores) == len(headers):
                dicionario_linha = dict(zip(headers, valores))
                lista_dados.append(dicionario_linha)

        coluna_chave = "Game" 

        if coluna_chave not in headers:
            coluna_chave = headers[0]
            print(f"Aviso: Coluna 'Game' não encontrada. Usando '{coluna_chave}' como chave.\n")

        dicionario_indexado = {}
        conjunto_valores_unicos = set()
        lista_duplicatas = []

        for item in lista_dados:
            valor_chave = item.get(coluna_chave)

            dicionario_indexado[valor_chave] = item

            if valor_chave in conjunto_valores_unicos:
                lista_duplicatas.append(valor_chave)
            else:
                conjunto_valores_unicos.add(valor_chave)

        total_registros = len(lista_dados)
        total_unicos = len(conjunto_valores_unicos)

        print("=== Relatório de Processamento ===")
        print(f"Total de registros: {total_registros}")
        print(f"Total de valores únicos: {total_unicos}")
        print(f"Duplicatas encontradas: {lista_duplicatas}")

        if total_unicos > 0:
            exemplo_chave = list(dicionario_indexado.keys())[0]
            print(f"\nExemplo de consulta rápida por chave ['{exemplo_chave}']: ")
            print(dicionario_indexado[exemplo_chave])

    except Exception as e:
        print(f"Erro durante o processamento: {e}")

if __name__ == "__main__":
    processar_dados_jogos()