# API e documentação da API.

## Passos para execução
- Instalar os requerimentos necessários.
- Executar o arquivo `inserir.py` (para popular o banco de dados).
- Executar o arquivo `api.py` (para executar a API).
- Escolher um request de um dos [possíveis requests (pdf)](Manual_endpoints.pdf) ou [documentação yaml](API_FTT-1.0.0-resolved.yaml), ou [export do Postman](FTT_API_Etapa_4.postman_collection.json) (só importar para o Postman). 
- Enviar request. Se tiver body seguir os data types da documentação.

## Informações principais
- Utiliza Python 3.9.6
- Só foi testado no Windows 10.
- Não possui autenticação.
- Bibliotecas utilizadas:
    - sys (padrão)
    - json (padrão)
    - textwrap (padrão)
    - sqlite3 (padrão)
    - Flask
    - Flask-RESTful
    - SQLAlchemy

## Requerimentos necessários
Para instalar os requerimentos necessários, nas versões corretas. Inserir comando `pip install -r requirements.txt`.

O script inserir.py, serve para popular o banco de dados, para realizar testes. Executando-o, ele insere 4 linhas em cada tabela.