import urllib.request
import urllib.error
import os

def baixar_pagina_wiki():
    url_alvo = "https://en.wikipedia.org/wiki/List_of_most-played_mobile_games_by_player_count"
    
    caminho_pasta = r"C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\pedro_silva_dr4_at\file"
    nome_arquivo = "pagina_original.html"
    
    caminho_completo = os.path.join(caminho_pasta, nome_arquivo)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print(f"Iniciando download de: {url_alvo}")
    print(f"Salvando em: {caminho_pasta}")

    try:
        if not os.path.exists(caminho_pasta):
            print("A pasta não existia, criando diretório...")
            os.makedirs(caminho_pasta)

        requisicao = urllib.request.Request(url_alvo, headers=headers)
        
        with urllib.request.urlopen(requisicao) as resposta:
            conteudo_html = resposta.read()

        with open(caminho_completo, 'wb') as arquivo:
            arquivo.write(conteudo_html)

        print(f"\nSucesso! O arquivo foi salvo em: {caminho_completo}")

    except urllib.error.HTTPError as e:
        print(f"\nErro HTTP: O servidor recusou a conexão. Código: {e.code}")
    
    except urllib.error.URLError as e:
        print(f"\nErro de URL: Falha na conexão ou URL inválida. Motivo: {e.reason}")
    
    except OSError as e:
        print(f"\nErro de Sistema/Caminho: {e}")
    
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    baixar_pagina_wiki()