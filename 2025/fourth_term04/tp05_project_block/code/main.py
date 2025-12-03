import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re

def extracao_html_clear():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    req = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/3348/itabirito-mg'

    print('\n=== Tentando acesso na página ====\n')

    try:

        order = urllib.request.Request(req, headers=headers)

        response = urllib.request.urlopen(order)

        print('Sucesso! O site respondeu!')

        # Lendo o HTML
        html = response.read().decode('utf-8')

        # Parsing - Processando Dados

        # Transformando texto em objeto
        soup_dados = BeautifulSoup(html, 'html.parser')

        # encontrando a cidade
        tag_city = soup_dados.find('h1', attrs={'class': '-bold -font-18 -dark-blue _margin-r-10'})

        # Encontrando a temperatura
        tag_temperature_min = soup_dados.find('span', attrs={'id': 'min-temp-1'})
        tag_temperature_max = soup_dados.find('span', attrs={'id': 'max-temp-1'})
        tag_chuva = soup_dados.find('span', attrs={'class': '_margin-l-5'})
        tag_vento = soup_dados.find('span', attrs={'class': 'arrow _margin-r-10'})
        tag_umidade_min = soup_dados.find_all('span', attrs={'class': '-gray-light'})[2].get_text().strip()
        tag_umidade_max = soup_dados.find_all('span', attrs={'class': '-gray-light'})[3].get_text().strip()
        tag_arco_iris = re.sub(r'\s+', ' ', soup_dados.find_all('span', class_='-gray-light')[4].get_text().strip())
        nascer_por_sol = re.sub(r'\s+', ' ', soup_dados.find_all('span')[41].get_text().strip())
        
        # Extraindo os textos da TAG
        if tag_city and tag_temperature_min:

            city_text = tag_city.text
            temp_text_min = tag_temperature_min.text
            temp_text_max = tag_temperature_max.text
            chuva_text = tag_chuva.text
            vento_text = tag_vento.text

            result = {
            'city': city_text,
            'temp_min': temp_text_min,
            'temp_max': temp_text_max,
            'chuva': chuva_text,
            'vento': vento_text,
            'umidade_min': tag_umidade_min,
            'umidade_max': tag_umidade_max,
            'arco_iris': tag_arco_iris,
            'sol': nascer_por_sol
            }

            return result

        else:
            print(f'Não foi possível encontrar as TAG específicadas.')

            print('Sucesso!')

    except urllib.error.URLError as e:
        # Erro como 403, 404, 500
        print(f'O servidor recusou a conexão: {e.code}')

    except urllib.error.HTTPError as e:
        # Erro como sem internet, DNS
        print(f'Falah de conexão. Motivo: {e.reason}')

    except Exception as e:
        print(f'Erro genérico: {e}')


    print('\n=== Tratando os dados ====\n')

    


