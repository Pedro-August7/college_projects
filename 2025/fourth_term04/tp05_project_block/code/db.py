from main import extracao_html_clear
from conexoes import conexao_eng
from datetime import datetime
from sqlalchemy import create_engine, text


def db_extracao_dados():

    dados_clima = extracao_html_clear()
    
    if dados_clima:
        result = dados_clima

        # Criando conexão
        engine = conexao_eng()
        
        if engine:
            with engine.connect() as conn:
                try:
                    print('Iniciando transação no banco...')

                    sql_pai = text(
                        """
                        INSERT INTO pedro_silva_pb_tp05.pag_visitadas(url, data_visita)
                        VALUES(:url, :data)
                        RETURNING id_paginas;                        
                        """
                        )
                    
                    resultado_query = conn.execute(sql_pai, {'url': url_visitada, 'data': datetime.now()})
                    id_gerado = resultado_query.fetchone()[0]

                    print(f"Visita registrada! ID gerado: {id_gerado}")

                    sql_filho = text(
                        """
                        INSERT INTO pedro_silva_pb_tp05.dados_coletados (xid_paginas, cidade, umidade_min, chuva, vento, temp_min, arco_iris, sol, temp_max, umidade_max)
                        VALUES (:id_pai, :cidade, :umidade_min, :chuva, :vento, :temp_min, :arco_iris, :sol, :temp_max, :umidade_max);
                        """
                    )

                    parametros_filho = {    
                    "id_pai": id_gerado,
                    "cidade": result['city'], 
                    "temp_min": result['temp_min'],
                    "temp_max": result['temp_max'], 
                    "chuva": result['chuva'],
                    "vento": result['vento'],
                    "umidade_min": result['umidade_min'],
                    "umidade_max": result['umidade_max'],
                    "arco_iris": result['arco_iris'],
                    "sol": result['sol']
                    }

                    conn.execute(sql_filho, parametros_filho)

                    conn.commit()
                    print("Transação concluída com sucesso!")

                except Exception as e:
                    print(f"Erro na transação: {e}")
                    conn.rollback()
    else:
        print("O robô não conseguiu extrair dados, então nada será salvo no banco.")


if __name__ == '__main__':
    db_extracao_dados()