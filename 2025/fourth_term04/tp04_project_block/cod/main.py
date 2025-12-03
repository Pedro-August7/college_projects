import json
from sqlalchemy import Table, MetaData
from sqlalchemy.dialects.postgresql import insert
from connect import conexao_eng
import argparse

# Carregando os dados do JSON
with open(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp04_project_block\file\JSON\carga.json', 'r') as file:
    data = json.load(file)

with open(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp04_project_block\file\JSON\delete.json', 'r') as file:
    data02 = json.load(file)

# Criando o engine de conexão com o banco
engine = conexao_eng()

# Criando o metadata
metadata = MetaData()

# Refletindo a tabela 'clientes' do banco de dados - para adicionar / atualizar
clientes_add = Table('clientes', metadata, autoload_with=engine, schema='tp4_project_block')

# Verificando as colunas refletidas
print("Colunas refletidas:", clientes_add.columns.keys())

# Função para inserir ou atualizar os dados
def insert_dados():
    print('\n==== Atualizando ====')

    with engine.connect() as conn:
        for cliente in data:
            try:
                existing_email = conn.execute(
                    clientes_add.select().where(clientes_add.c.email == cliente['email'])
                ).fetchone()

                if existing_email:
                    print(f"\nEmail {cliente['email']} já existe, atualizando o cliente com id_cliente {existing_email[0]}")
                    instrucao_update = clientes_add.update().where(
                        clientes_add.c.id_cliente == existing_email[0]
                    ).values(
                        nome=cliente['nome'],
                        email=cliente['email']
                    )
                    conn.execute(instrucao_update)
                else:
                    instrucao_insert = insert(clientes_add).values(
                        nome=cliente['nome'],
                        email=cliente['email']
                    )
                    instrucao_insert = instrucao_insert.on_conflict_do_update(
                        index_elements=['id_cliente'],
                        set_={
                            'nome': cliente['nome'],
                            'email': cliente['email']
                        }
                    )
                    conn.execute(instrucao_insert)

            except Exception as e:
                print(f"\nErro ao processar o cliente {cliente['nome']}: {e}")
        
        conn.commit()
        print("\nTodos os clientes foram processados.\n")

# Função para remover os dados
def remove_dados():
    print('==== Removendo ====\n')

    erro_ocorrido = False  # Variável de controle

    with engine.connect() as conn:
        for cliente in data02:
            try:
                existing_cliente = conn.execute(
                    clientes_add.select().where(clientes_add.c.id_cliente == cliente['id_cliente'])
                ).fetchone()

                if existing_cliente:
                    print(f"\nid_cliente {cliente['id_cliente']} encontrado, removendo o cliente com email {existing_cliente[2]}")
                    instrucao_delete = clientes_add.delete().where(
                        clientes_add.c.id_cliente == cliente['id_cliente']  # Usando id_cliente como critério de exclusão
                    )
                    conn.execute(instrucao_delete)
                else:
                    erro_ocorrido = True
                    print(f"id_cliente {cliente['id_cliente']} não encontrado, nenhum dado foi removido.")

            except Exception as e:
                erro_ocorrido = True
                print(f"\nErro ao processar o cliente com id_cliente {cliente['id_cliente']}: {e}")
        
        conn.commit()

        if not erro_ocorrido:
            print("\nTodos os clientes foram removidos.")
        
        if erro_ocorrido:
            print('\nVerifique o arquivo JSON, pode estar com usuário duplicado.\n')

# Função para consultar registros
def consultar_clientes(engine):
    if engine is None:
        print("Não foi possível conectar ao banco de dados.")
        return
    
    # Criando o metadata
    metadata = MetaData()

    # Refletindo a tabela 'clientes' do banco de dados
    clientes = Table('clientes', metadata, autoload_with=engine, schema='tp4_project_block')

    # Consultando os registros da tabela 'clientes'
    with engine.connect() as conn:
        try:
            result = conn.execute(clientes.select()).fetchall()

            if result:
                print("\nRegistros encontrados:")
                for row in result:
                    print(row)
            else:
                 print("\nNenhum registro encontrado na tabela 'clientes'.")
        except Exception as e:
            print(f"\nErro ao consultar os clientes: {e}")

# Função para gerenciar os argumentos
def main_gere():
    parser = argparse.ArgumentParser(description='Escolha qual função executar: ')

    # Adicionando os argumentos
    parser.add_argument('funcao', choices=['inserir', 'remover', 'consultar'],
                        help="Escolha a função a ser executada: 'inserir', 'remover', 'consultar'")
    args = parser.parse_args()

    if args.funcao == 'inserir':
        insert_dados()  
    elif args.funcao == 'remover':
        remove_dados()
    elif args.funcao == 'consultar':
        consultar_clientes(engine)

if __name__ == '_main_':
    main_gere()