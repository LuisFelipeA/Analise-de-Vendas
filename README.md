# Projeto de Importação e Tratamento de Dados

Este projeto tem como foco o tratamento e organização de dados de vendas, produtos e vendedores de uma empresa varejista fictícia.
O objetivo é preparar esses dados para análises que apoiem a área de negócios na avaliação de desempenho, receita e identificação de oportunidades.

Para isso, o projeto realiza a leitura de um arquivo Excel com múltiplas planilhas, faz o processamento e limpeza dos dados, armazena-os em um banco PostgreSQL e permite consultas via Power BI diretamente no banco.

## Funcionalidades

- Leitura de arquivos Excel com múltiplas abas (Itens Notas, Notas, Produtos, Vendedores);
- Limpeza e tratamento dos dados (remoção de colunas vazias, padronização de nomes e tipos);
- Criação de novas colunas calculadas para enriquecer a análise (ex: valor total da venda);
- Validação das chaves estrangeiras para garantir integridade dos dados;
- Criação das tabelas no PostgreSQL e inserção dos dados tratados;
- Consulta dos dados via Power BI diretamente no banco.


## Pré-requisitos

Antes de rodar o projeto, você precisará ter os seguintes componentes instalados:

- **Python 3.10**: O projeto é desenvolvido em Python.
- **Bibliotecas Python**:
  - `pandas` (para manipulação de dados)
  - `psycopg2` (para conexão com banco de dados)
  - `dotenv` (para ler .env)
- **Banco de Dados PostgreSQL**: Instalar e configurar um banco de dados PostgreSQL.
- **Power BI**: Para visualizar os dados diretamente do banco.

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/LuisFelipeA/Analise-de-Vendas.git
   cd Analise-de-Vendas

2. **Dataset utilizado**:

   link https://caelum-online-public.s3.amazonaws.com/2030-entendendo-formulas-dax/01/Preparando-o-ambiente.zip

2. **Criar arquivo .env**:

   Criar arquivo com nome de '.env' para colocar informações do banco de dados.
   Exemplo de conteudo do arquivo:

   DB_HOST=localhost
   DB_NAME=meubanco
   DB_USER=usuario
   DB_PASSWORD=senha
   DB_PORT=5432

   Substituir por informações do seu banco de dados

## Próximos passos

- Automatizar o pipeline com ferramentas de orquestração como Apache Airflow ou Azure Data Factory;
- Migrar o processamento para Azure Databricks utilizando PySpark para escalabilidade;
- Implementar monitoramento e alertas para garantir qualidade e disponibilidade dos dados;
- Desenvolver dashboards interativos mais complexos no Power BI.
