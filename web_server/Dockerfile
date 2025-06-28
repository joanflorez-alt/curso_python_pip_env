FROM python:3.11-slim

WORKDIR /app

#instalar las dependencias en local / contenedor (copiar el archivo requiriments.txt)
COPY requiriments.txt /app/requiriments.txt

RUN pip install --no-cache-dir --upgrade -r /app/requiriments.txt

#ahora hacemos la copia de todo el proyecto
COPY . /app


#creamos el comando de activación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port","8000"]