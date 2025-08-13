# Importar pandas
import pandas as pd

# Ler csv
df = pd.read_csv("vendas.csv")  

# Explorarando dados
print("Primeiras 5 linhas:")
print(df.head())

print("\nInformações do dataset:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())

# # ---------- 3. Limpeza simples ----------
# df.dropna(inplace=True)  # remove linhas com valores nulos

# # Exemplo de correção de tipo, se necessário
# # df['Quantidade'] = df['Quantidade'].astype(int)
# # df['PrecoUnitario'] = df['PrecoUnitario'].astype(float)

# # ---------- 4. Criar novas colunas e métricas ----------
# df['Receita'] = df['Quantidade'] * df['PrecoUnitario']
# # Se tiver coluna de custo, pode criar lucro
# # df['Lucro'] = df['Receita'] - df['Custo']

# # ---------- 5. Agrupar por categoria ----------
# vendas_por_categoria = df.groupby('Categoria').agg({
#     'Receita': ['sum', 'mean'],   # Total e média de receita
#     'Quantidade': 'sum'           # Total de quantidade vendida
# }).reset_index()

# # Ajustar nomes das colunas
# vendas_por_categoria.columns = ['Categoria', 'Receita_Total', 'Receita_Media', 'Quantidade_Total']

# print("\nVendas por categoria:")
# print(vendas_por_categoria)

# # ---------- 6. Exportar resultado ----------
# vendas_por_categoria.to_csv("vendas_por_categoria_preparado.csv", index=False)
# print("\nArquivo 'vendas_por_categoria_preparado.csv' gerado com sucesso!")
