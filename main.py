from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

# Crear instancia de FastAPI
app = FastAPI()

# Definir un modelo de datos para entrada
class PredictionRequest(BaseModel):
    input_data: list

# Función para preprocesamiento automático
def preprocess_data(input_data):
    """
    Realiza preprocesamiento automático en los datos.
    - input_data: lista de diccionarios con datos de entrada.
    """
    # Convertir la lista de entrada en un DataFrame
    df = pd.DataFrame(input_data)
    
    # Paso 1: Eliminar duplicados
    df = df.drop_duplicates()

    # Paso 2: Manejar valores nulos (rellenar con la media)
    df.fillna(df.mean(), inplace=True)

    # Paso 3: Escalar datos (normalización simple)
    for column in df.select_dtypes(include=["float64", "int64"]).columns:
        df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    
    return df

# Ruta principal
@app.get("/")
async def root():
    return {"message": "¡La API está funcionando!"}

# Endpoint para predicciones
@app.post("/predict")
async def predict(data: PredictionRequest):
    # Procesar datos de entrada
    input_data = data.input_data

    # Preprocesar los datos
    preprocessed_data = preprocess_data(input_data)

    # Simular una predicción usando el preprocesamiento
    # (Puedes integrar aquí tu modelo de Machine Learning)
    prediction = preprocessed_data.mean(axis=1).tolist()

    return {"preprocessed_data": preprocessed_data.to_dict(orient="records"), "prediction": prediction}

