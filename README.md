# Rick and Morty API Data Extractor

Este projeto é uma aplicação em Python para extrair dados da API pública do Rick and Morty, carregar esses dados no Google BigQuery e exportá-los para o Google Sheets.

## Funcionalidades

- Extrai dados de personagens, locais e episódios da API do Rick and Morty.
- Carrega os dados extraídos para o Google BigQuery.
- Exporta os dados do BigQuery para o Google Sheets.

## Pré-requisitos

- Python 3.x instalado no sistema.
- Conta do Google Cloud Platform com acesso ao BigQuery e Google Sheets.
- Credenciais do serviço do Google Cloud Platform para autenticar no BigQuery e Google Sheets.
- Bibliotecas Python necessárias, instaladas via `pip install -r requirements.txt`.

## Configuração

1. Clone o repositório para o seu ambiente local:

- git clone https://github.com/seu-usuario/rick-and-morty-api.git

2. Instale as dependências do projeto:

- pip install -r requirements.txt


## Uso

1. Execute o script `main.py` para extrair os dados da API do Rick and Morty, carregá-los no BigQuery e exportá-los para o Google Sheets:

- python main.py


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias, correções de bugs, ou novas funcionalidades.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
