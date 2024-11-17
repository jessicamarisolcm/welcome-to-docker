FROM python:3.8-slim

# Instalar dependencias
RUN pip install --no-cache-dir pandas scikit-learn fastapi uvicorn hyperopt optuna joblib pyarrow

# Copiar archivos al contenedor
COPY . /app
WORKDIR /app

# Exponer el puerto para la API
EXPOSE 8000

# Comando de entrada
CMD ["python", "main.py"]
