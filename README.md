# Classificação de Notas Fiscais

Este projeto consiste em uma API desenvolvida com FastAPI para classificar notas fiscais como "válidas" ou "não válidas" com base em um modelo de aprendizado de máquina. Além disso, tem um notebook apresentando os experimentos e análises feitas para o conjunto de dados em questão.

## Requisitos

Antes de rodar a aplicação, verifique se você possui os seguintes requisitos instalados:

- Python 3.8+
- Docker (opcional, caso queira rodar o contêiner Docker)

## Arquitetura
O projeto é composto por:

- FastAPI: Framework para criar a API.
- [Modelo de Machine Learning](https://github.com/augustces/DeteccaoDeNotasFiscaisInvalidas/blob/main/api/modelo/random_forest_model.pkl): Modelo de classificação treinado para identificar se uma nota fiscal é válida ou não.
- Docker: Para rodar a aplicação de forma isolada e portátil.
- [Jupyter Notebook](https://github.com/augustces/DeteccaoDeNotasFiscaisInvalidas/blob/main/notebook/Detec%C3%A7%C3%A3o%20de%20Impostos%20Invalidos.ipynb): Apresentando a análise de dados, os explicando os experimentos e apresentando uma comparação entre dois modelos (Random Forest e XGBoost).

## Estrutura do Projeto
```bash
DeteccaoDeNotasFiscaisInvalidas/
├── api/                                        # Pasta que contém a aplicação da API e do Docker
│   ├── app/                                    # Pasta que contém a aplicação da API 
│   │   ├── main.py                             # Ponto de entrada da aplicação
│   │   ├── meme.jpg                            # Imagem que representa que a api está funcionando
│   │   ├── notafiscal.py                       # Modelo base de uma nota fiscal
│   │   └── predict.py                          # Lógica de previsão
│   ├── modelo/                                 # Pasta do modelo de Machine Learning
│   │   ├── modelo.py                           # Arquivo para a criação do modelo de classificação
│   │   └── random_forest_model.pkl             # Modelo treinado vindo do modelo.py
│   ├── scripts/                                # Pasta para scripts auxiliares
│   │   └── request.py                          # Arquivo de requisição para o servidor
│   ├── Dockerfile                              # Arquivo para criar a imagem Docker
│   └── requirements.txt                        # Dependências do Python
├── dataset/                                    # Pasta que contém o dataset
│   └── notasfiscais.csv                        # Dataset em csv
├── notebook                                    # Pasta que contém o Jupyter Notebook
│   └── Detecção de Impostos Invalidos.ipynb    # Jupyter Notebook com experimentos
└── README.md                                   # Este arquivo
```

## Instalação

### 1. **Instalar Dependências**

Primeiro, clone o repositório para sua máquina local e entre na pasta `api`:

```sh
git clone https://github.com/augustces/DeteccaoDeNotasFiscaisInvalidas.git
cd DeteccaoDeNotasFiscaisInvalidas/api
```

Agora instale as dependências:

```sh
pip install -r requirements.txt
```

### 2. **Rodando a Aplicação Localmente**

Com as dependências instaladas, você pode rodar a aplicação FastAPI localmente com o comando:

```sh
uvicorn app.main:app --reload
```

O servidor estará disponível em http://localhost:8000. Você pode acessar a documentação interativa da API em:

```sh
http://localhost:8000/docs
```

### 3. **Rodando com Docker**
Se for rodar a aplicação dentro de um contêiner Docker, instale o docker [neste link](https://docs.docker.com/get-started/get-docker/) e siga os passos abaixo:

#### 1. Criar a imagem Docker:

```sh
docker build -t fastapi_app .
```

#### 2. Rodar a aplicação em um contêiner:
```sh
docker run -d -p 8000:8000 --name fastapi_container fastapi_app

```

Agora, a API estará rodando em http://localhost:8000.

### 4. **Usando a API**

A API possui o seguinte endpoint principal: `POST /predict`

Esse endpoint recebe os dados de uma nota fiscal e retorna a classificação da nota como "válida" ou "não válida". Exemplo de dados para enviar:

```json
{
  "id_supplier": 7101,
  "iss_retention": true,
  "iss_tax_rate": 2.0,
  "csll_tax_rate": 0.0,
  "ir_tax_rate": 0.0,
  "cofins_tax_rate": 0.0,
  "pis_tax_rate": 0.0,
  "opting_for_simples_nacional": true,
}
```
### 5. **Testando a API**
Se você quiser testar a API com um script, você pode usar o arquivo `scripts/request_post.py`, que contém um exemplo de como fazer uma requisição `POST` para o endpoint `/predict`.

Para rodar o script de requisição, use:

```sh
python scripts/request_post.py

```


