import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re

def extracao_html_clear(url_passada=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    if url_passada:
        url_visitada = url_passada
    else:
        url_visitada = input("Qual página deseja visitar: ")

    print(f'\n=== Tentando acesso na página: {url_visitada} ====\n')

    try:
        order = urllib.request.Request(url_visitada, headers=headers)
        response = urllib.request.urlopen(order)

        # Lendo o HTML
        html = response.read().decode('utf-8')

        # Parsing - Processando Dados
        soup_dados = BeautifulSoup(html, 'html.parser')

        # Encontrando a cidade
        tag_city = soup_dados.find('h1', attrs={'class': '-bold -font-18 -dark-blue _margin-r-10'})

        # Encontrando dados
        tag_temperature_min = soup_dados.find('span', attrs={'id': 'min-temp-1'})
        tag_temperature_max = soup_dados.find('span', attrs={'id': 'max-temp-1'})
        tag_chuva = soup_dados.find('span', attrs={'class': '_margin-l-5'})
        tag_vento = soup_dados.find('span', attrs={'class': 'arrow _margin-r-10'})

        lista_umidade = soup_dados.find_all('span', attrs={'class': '-gray-light'})

        if tag_city and tag_temperature_min and len(lista_umidade) >= 5:
            
            tag_umidade_min = lista_umidade[2].get_text().strip()
            tag_umidade_max = lista_umidade[3].get_text().strip()
            tag_arco_iris = re.sub(r'\s+', ' ', lista_umidade[4].get_text().strip())
            
            spans_gerais = soup_dados.find_all('span')
            nascer_por_sol = "N/A"
            if len(spans_gerais) > 41:
                nascer_por_sol = re.sub(r'\s+', ' ', spans_gerais[41].get_text().strip())

            result = {
                'url': url_visitada,
                'city': tag_city.text,
                'temp_min': tag_temperature_min.text,
                'temp_max': tag_temperature_max.text,
                'chuva': tag_chuva.text,
                'vento': tag_vento.text,
                'umidade_min': tag_umidade_min,
                'umidade_max': tag_umidade_max,
                'arco_iris': tag_arco_iris,
                'sol': nascer_por_sol
            }
            return result
        else:
            return None 

    except Exception as e:
        print(f"Erro interno na extração: {e}")
        raise e