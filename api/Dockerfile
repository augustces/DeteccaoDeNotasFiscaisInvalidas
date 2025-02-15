# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar arquivos da aplicação para dentro do contêiner
COPY . /app

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta 8000
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
