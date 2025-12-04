from main import extracao_html_clear
from conexoes import conexao_eng
from datetime import datetime
from sqlalchemy import create_engine, text

if __name__ == '__main__':
    
    # Lista de URLs para visitar
    lista_urls = [
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/3348/itabirito-mg',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp',
        'https://www.site-errado-teste.com/nao-existe', 
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/107/belohorizonte-mg',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/403/avare-sp',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/1445/tubarao-sc',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/4195/jardimalegre-pr',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/80/serra-es',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/9647/tromso-no',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/4371/caraa-rs',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/508/perus-sp',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/7447/pereira-co',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/3351/perola-pr',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/7241/perth-aa',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/3644/carai-mg',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/3182/carmo-rj',
        'https://www.climatempo.com.br/previsao-do-tempo/cidade/3442/carira-se'
    ]

    engine = conexao_eng()

    if engine:
        with engine.connect() as conn:
            
            for url_atual in lista_urls:
                
                print(f"=== Processando: {url_atual} ===")
                
                try:
                    sql_pai = text("""
                        INSERT INTO pedro_silva_pb_tp05.pag_visitadas(url, data_visita)
                        VALUES(:url, :data)
                        RETURNING id_paginas;
                    """)
                    
                    resultado = conn.execute(sql_pai, {'url': url_atual, 'data': datetime.now()})
                    id_pai_gerado = resultado.fetchone()[0]
                    conn.commit()
                    
                except Exception as e:
                    print(f"Erro crítico ao salvar página visitada (Pai): {e}")
                    continue

                try:
                    
                    dados = extracao_html_clear(url_atual)

                    if dados:
                        sql_filho = text("""
                            INSERT INTO pedro_silva_pb_tp05.dados_coletados 
                            (xid_paginas, cidade, temp_min, temp_max, chuva, vento, umidade_min, umidade_max, arco_iris, sol)
                            VALUES (:id_pai, :cidade, :temp_min, :temp_max, :chuva, :vento, :umidade_min, :umidade_max, :arco_iris, :sol);
                        """)

                        parametros_filho = {    
                            "id_pai": id_pai_gerado,
                            "cidade": dados['city'], 
                            "temp_min": dados['temp_min'],
                            "temp_max": dados['temp_max'], 
                            "chuva": dados['chuva'],
                            "vento": dados['vento'],
                            "umidade_min": dados['umidade_min'],
                            "umidade_max": dados['umidade_max'],
                            "arco_iris": dados['arco_iris'],
                            "sol": dados['sol']
                        }
                        
                        conn.execute(sql_filho, parametros_filho)
                        conn.commit()
                        print("-> SUCESSO: Dados coletados e salvos!")
                    
                    else:
                        raise Exception("A estrutura do site mudou ou a extração falhou (retornou None).")

                except Exception as e:
                    conn.rollback()
                    print(f"-> FALHA: Salvando na tabela de Logs... Erro: {e}")
                    
                    sql_log = text("""
                        INSERT INTO pedro_silva_pb_tp05.logs_excecoes (descricao, data, origem_url)
                        VALUES (:desc, :data, :url)
                    """)
                    
                    conn.execute(sql_log, {
                        "desc": str(e),
                        "data": datetime.now(),
                        "url": url_atual
                    })
                    conn.commit()

            print("\n=== Fim do Processamento de todas as URLs ===")