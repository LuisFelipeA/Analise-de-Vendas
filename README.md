# Projeto de Importação e Tratamento de Dados

Este projeto tem como objetivo ler um arquivo Excel com várias planilhas, processar esses dados, armazená-los em um banco de dados PostgreSQL e, posteriormente, realizar consultas utilizando o Power BI diretamente no banco de dados.

## Funcionalidade

- **Leitura de Arquivo Excel**: O projeto é capaz de ler arquivos Excel contendo várias planilhas.
- **Tratamento de Dados**: O tratamento envolve a limpeza, formatação e normalização dos dados.
- **Armazenamento em PostgreSQL**: Após o tratamento, os dados são armazenados em um banco de dados PostgreSQL.
- **Consulta via Power BI**: O Power BI se conecta diretamente ao banco de dados PostgreSQL para visualizar os dados.

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