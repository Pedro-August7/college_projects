# Importações
import pandas as pd
import sqlite3

# Jogadores âncora
jogadores_acora = [
    "Cristiano Ronaldo",
    "L. Messi",
    "Neymar Jr",
    "K. Mbappé",
    "Kevin De Bruyne",
    "Mohamed Salah",
    "Robert Lewandowski",
    "Sergio Ramos",
    "Virgil van Dijk",
    "Luka Modric",
    "Toni Kroos",
    "Eden Hazard",
    "Luis Suárez",
    "Manuel Neuer",
    "Harry Kane",
    "Paulo Dybala",
    "Giorgio Chiellini",
    "Karim Benzema",
    "Antoine Griezmann",
    "Marc-André ter Stegen"
    ]

# Carregando arquivos
caminho_base = r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files'
anos = [15, 16, 17, 18, 19, 20, 21]

dfs_processados = []

print('=== Processando tabelas ===\n')
for ano in anos:
    index = + 1
    print(f'Ano processado: 20{ano}')

    # Caminho do arquivo dinamico
    arquivo = f'{caminho_base}\\players_{ano}.csv'

    # Carregando arquivo
    df_temp = pd.read_csv(arquivo)

    # Filtrando arquicos
    df_temp = df_temp[df_temp['short_name'].isin(jogadores_acora)]

    # Renomeando arquivo
    df_temp = df_temp.rename(columns={
    'overall': f'overall_{ano}',
    'potential': f'potential_{ano}'
    })

    # Colunas que serão exibidas
    cols_manter = ['short_name', f'overall_{ano}', f'potential_{ano}']
    df_temp = df_temp[cols_manter]

    # Guardar
    dfs_processados.append(df_temp)

print('Todos os arquivos foram processados.')

print('\n=== Iniciando Consolidação ===\n')

# Definindo DataFrame base
df_consolidado = dfs_processados[0]

# Processando os demais DataFrame
for df_ano in dfs_processados[1:]:
    df_consolidado = pd.merge(df_consolidado, df_ano, on='short_name', how='inner')

# Visualização
print(f"Merge concluído! Tamanho final: {df_consolidado.shape}")
print(df_consolidado.head())

# Calculando evolução
# Criando colunas no DataFrame
df_consolidado['evolucao_overall'] = df_consolidado['overall_21'] - df_consolidado['overall_15']
df_consolidado['evolucao_potential'] = df_consolidado['potential_21'] - df_consolidado['potential_15']

# Funcção para ratings
def classificar_tendencia(evolution):
    if evolution > 1:
        return 'Subiu'
    
    elif evolution < -1:
        return 'Caiu'
    else:
        return 'Estavel'
    
    # Aplicando a função na coluna "evolucao_overall"

df_consolidado['tendencia_overall'] = df_consolidado['evolucao_overall'].apply(classificar_tendencia)

# Salvando reports
print('\n=== Salvando relatório final ===\n')

nome_arquivo = 'relatorio_fifa_15_21_sj90.csv'
caminho_salvar_reports = r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\saved_reports'
caminho_saida = f"{caminho_salvar_reports}\\{nome_arquivo}"

df_consolidado.to_csv(caminho_saida, index=False)
print('Arquivo salvo com sucesso!')

colunas_visualizacao = ['short_name', 'overall_15', 'overall_21', 'evolucao_overall', 'tendencia_overall']
print(df_consolidado[colunas_visualizacao])