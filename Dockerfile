# Usa a imagem base Python 3.11 slim, que é uma versão menor e otimizada com Linguagem Python.
FROM python:3.11-slim-buster

# Define o diretório de trabalho dentro do container como /app.
WORKDIR /app

# Copia todos os arquivos do diretório atual no host para o diretório de trabalho no container.
ADD . /app

# Instala as dependências listadas no arquivo requirements.txt sem usar o cache do pip.
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8787 para que a aplicação possa ser acessada externamente.
EXPOSE 8787

# Define o comando para iniciar a aplicação usando uvicorn no host 0.0.0.0 e porta 8787.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8787"]

