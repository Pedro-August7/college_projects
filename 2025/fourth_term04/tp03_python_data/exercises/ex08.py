import pandas as pd

# Carregando arquivos CSv
df_20 = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_20.csv')
df_21 = pd.read_csv(r'C:\Users\Pedrox\OneDrive\Repositorios GitHub\college_projects\2025\fourth_term04\tp03_python_data\files\players_21.csv')

colunas_a_processar = ['overall', 'potential', 'age']

media_20 = df_20[colunas_a_processar].mean()
media_21 = df_21[colunas_a_processar].mean()

# Comparações anuais
df_comparacao_ano = pd.DataFrame({
    'Ano 2020': media_20,
    'Ano 2021': media_21
})

print(df_comparacao_ano)