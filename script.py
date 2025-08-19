# %% [markdown]
# ## Importando bibliotecas e lendo arquivo

# %%
# Importar pandas
import pandas as pd

# %% [markdown]
# Dataset utilizado
# https://caelum-online-public.s3.amazonaws.com/2030-entendendo-formulas-dax/01/Preparando-o-ambiente.zip

# %%
# Ler arquivo Excel
itens_notas = pd.read_excel("Data/dataset-vendas.xlsx", "Itens Notas")
notas = pd.read_excel("Data/dataset-vendas.xlsx", "Notas")
produtos = pd.read_excel("Data/dataset-vendas.xlsx", "Produtos")
vendedores = pd.read_excel("Data/dataset-vendas.xlsx", "Vendedores")

# %% [markdown]
# ## Explorando dados

# %% [markdown]
# ### Head

# %%
# Primeiras linhas itens notas
print(itens_notas.head())

# %%
# Primeiras linhas notas
print(notas.head())

# %%
# Primeiras linhas produtos
print(produtos.head())

# %%
# Primeiras linhas vendedores
print(vendedores.head())

# %% [markdown]
# ### Info

# %%
# Informações do Dataset itens notas
print(itens_notas.info())

# %%
# Informações do Dataset notas
print(notas.info())

# %%
# Informações do Dataset produtos
print(produtos.info())

# %%
# Informações do Dataset vendedores
print(vendedores.info())

# %% [markdown]
# ### Describe

# %%
# Estatisticas descritivas itens notas
print(itens_notas.describe())

# %%
# Estatisticas descritivas notas
print(notas.describe())

# %%
# Estatisticas descritivas produtos
print(produtos.describe())

# %%
# Estatisticas descritivas vendedore
print(vendedores.describe())

# %% [markdown]
# ### Contar valores nulos por coluna

# %%
print("--------Itens Notas---------")
print(itens_notas.isnull().sum())

print("\n----------Notas-----------")
print(notas.isnull().sum())

print("\n---------Produtos---------")
print(produtos.isnull().sum())

print("\n--------Vendedores--------")
print(vendedores.isnull().sum())

# %% [markdown]
# ## Limpeza e tratamento dos dados

# %% [markdown]
# A fazer:
#  - Remover colunas vazias
#  - Renomear colunas para padrão do banco de dados
#  - Ajustar tipos das colunas para padrão do banco de dados

# %% [markdown]
# ### Remover colunas vazias

# %%
# Remover colunas Unnamed: 3  Unnamed: 4  Unnamed: 5  Unnamed: 6

itens_notas = itens_notas.drop(columns=['Unnamed: 3', 'Unnamed: 4','Unnamed: 5', 'Unnamed: 6'])


# %% [markdown]
# ### Renomar colunas

# %%
# Itens Nota
itens_notas = itens_notas.rename(columns={
    'Numero': 'numero_nota',
    'Codigo do produto': 'codigo_produto',
    'Quantidade': 'quantidade'
})

# %%
# Notas

notas = notas.rename(columns={
    'Matricula': 'matricula_vendedor',
    'Data': 'data_venda',
    'Numero': 'numero_nota',
    'Imposto': 'imposto'
})

# %%
produtos = produtos.rename(columns={
    'Codigo do produto': 'codigo_produto',
    'Nome do produto': 'nome',
    'Tipo': 'tipo',
    'Preço': 'valor'
})

# %%
vendedores = vendedores.rename(columns={
    'Matricula': 'matricula',
    'Nome': 'nome',
    'Percentual Comissao': 'percentual_comissao',
    'Imagem': 'url_imagem'
})

# %% [markdown]
# ### Criando novas colunas

# %%
# Colocando coluna 'valor' de produtos em itens_notas
itens_notas = itens_notas.merge(produtos[['codigo_produto', 'valor']],
                                on='codigo_produto',
                                how='left')

# Renomear coluna
itens_notas = itens_notas.rename(columns={'valor': 'valor_unitario'})

# Criar nova coluna calculada
itens_notas['valor_venda'] = itens_notas['quantidade'] * itens_notas['valor_unitario']

print(itens_notas.head())


# %% [markdown]
# ### Tipos das colunas

# %%
# Itens Notas
itens_notas['numero_nota'] = itens_notas['numero_nota'].astype(int)
itens_notas['codigo_produto'] = itens_notas['codigo_produto'].astype(int)
itens_notas['quantidade'] = itens_notas['quantidade'].astype(int)
itens_notas['valor_unitario'] = itens_notas['valor_unitario'].astype(float)
itens_notas['valor_venda'] = itens_notas['valor_venda'].astype(float)

# %%
# Notas
notas['numero_nota'] = notas['numero_nota'].astype(int)
notas['matricula_vendedor'] = notas['matricula_vendedor'].astype(int)
notas['imposto'] = notas['imposto'].astype(float)
notas['data_venda'] = pd.to_datetime(notas['data_venda'])

# %%
# Produtos
produtos['codigo_produto'] = produtos['codigo_produto'].astype(int)
produtos['valor'] = produtos['valor'].astype(float)
produtos['nome'] = produtos['nome'].astype('string')
produtos['tipo'] = produtos['tipo'].astype('string')

# %%
# Vendedores
vendedores['matricula'] = vendedores['matricula'].astype(int)
vendedores['percentual_comissao'] = vendedores['percentual_comissao'].astype(float)
vendedores['nome'] = vendedores['nome'].astype('string')
vendedores['url_imagem'] = vendedores['url_imagem'].astype('string')


# %% [markdown]
# ### Verificação de chaves estrangeiras

# %%
# 1. Validar numero_nota
notas_validas = notas['numero_nota'].unique()
itens_notas = itens_notas[itens_notas['numero_nota'].isin(notas_validas)]

# 2. Validar codigo_produto
produtos_validos = produtos['codigo_produto'].unique()
itens_notas = itens_notas[itens_notas['codigo_produto'].isin(produtos_validos)]


# %% [markdown]
# ## Exportando dataframe tratado

# %% [markdown]
# ### Conexão com banco de dados

# %%
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv() # Carrega arquivos do .env

try:
    # Conexão
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    # Criar cursor (objeto usado para enviar comandos sql)
    cur = conn.cursor()

    # Teste de conexão (executando um simples SELECT)
    cur.execute("SELECT 1;")
    result = cur.fetchone()

    if result:
        print("Conexão bem-sucedida!")
    else:
        print("Falha na consulta.")

except psycopg2.OperationalError as e:
    print(f"Erro de conexão: {e}")



# %% [markdown]
# ### Criando tabelas

# %%
# Tabela Produtos
cur.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    codigo_produto INT PRIMARY KEY,
    nome TEXT,
    tipo TEXT,
    valor NUMERIC
)
""")

# Tabela Vendedores
cur.execute("""
CREATE TABLE IF NOT EXISTS vendedores (
    matricula INT PRIMARY KEY,
    nome TEXT,
    percentual_comissao NUMERIC,
    url_imagem TEXT
)
""")

# Tabela Notas
cur.execute("""
CREATE TABLE IF NOT EXISTS notas (
    numero_nota INT PRIMARY KEY,
    data_venda DATE,
    imposto NUMERIC,
    matricula_vendedor INT,
    FOREIGN KEY (matricula_vendedor) REFERENCES vendedores(matricula)
)
""")

# Tabela Itens_notas
cur.execute("""
CREATE TABLE IF NOT EXISTS itens_notas (
    numero_nota INT,
    codigo_produto INT,
    quantidade INT,
    valor_unitario NUMERIC,
    valor_venda NUMERIC,
    FOREIGN KEY (numero_nota) REFERENCES notas(numero_nota),
    FOREIGN KEY (codigo_produto) REFERENCES produtos(codigo_produto)
)
""")

# Salvar alterações
conn.commit()

# %% [markdown]
# ### Inserindo dados

# %%
# Inserir produtos
for i, row in produtos.iterrows():
    cur.execute("""
        INSERT INTO produtos (codigo_produto, nome, tipo, valor)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (codigo_produto) DO NOTHING
    """, (row['codigo_produto'], row['nome'], row['tipo'], row['valor']))

# Inserir vendedores
for i, row in vendedores.iterrows():
    cur.execute("""
        INSERT INTO vendedores (matricula, nome, percentual_comissao, url_imagem)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (matricula) DO NOTHING
    """, (row['matricula'], row['nome'], row['percentual_comissao'], row['url_imagem']))

# Inserir notas
for i, row in notas.iterrows():
    cur.execute("""
        INSERT INTO notas (numero_nota, data_venda, imposto, matricula_vendedor)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (numero_nota) DO NOTHING
    """, (row['numero_nota'], row['data_venda'], row['imposto'], row['matricula_vendedor']))

# Inserir itens_notas
for i, row in itens_notas.iterrows():
    cur.execute("""
        INSERT INTO itens_notas (numero_nota, codigo_produto, quantidade, valor_unitario, valor_venda)
        VALUES (%s, %s, %s, %s, %s)
    """, (int(row['numero_nota']), int(row['codigo_produto']), int(row['quantidade']), float(row['valor_unitario']), float(row['valor_venda'])))

# Salvar alterações
conn.commit()


# %% [markdown]
# ### Encerrando conexão

# %%
# Fecha conexão
if conn:
    cur.close()
    conn.close()
    print ("Conexão encerrada!")


