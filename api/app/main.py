from fastapi import FastAPI
from app.predict import prever_nota
from app.notafiscal import NotaFiscal
import joblib

# Carregar modelo treinado
modelo = joblib.load("modelo/random_forest_model.pkl")

# Criação da API
app = FastAPI()

@app.get("/")  # Corrigido para FastAPI
def verify():
    return {"message": "Tudo em cima por aqui!"}

@app.post("/predict")
def predict(nota: NotaFiscal):
    resultado = prever_nota(nota, modelo)
    return {"classificacao": resultado}
