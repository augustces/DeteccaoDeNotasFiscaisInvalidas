from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse
from app.predict import prever_nota
from app.notafiscal import NotaFiscal
import joblib
import os

# Carregar modelo treinado
modelo = joblib.load("modelo/random_forest_model.pkl")

# Criação da API
app = FastAPI()

# Caminhos do meme
MEME_PATH = os.path.join("app", "img", "status200.jpg") 

# Rota principal - Status 200
@app.get("/", response_class=HTMLResponse)
def verify():
    if os.path.exists(MEME_PATH):
        html_content = f"""
        <html>
            <body style="text-align: center; font-family: Arial, sans-serif;">
                <h2 style="color: green;">Tudo funcionando bem !!!</h2>
                <img src="/meme" alt="Meme de sucesso" width="400">
            </body>
        </html>
        """
        return HTMLResponse(content=html_content)
    return JSONResponse({"message": "Meme não encontrado!"}, status_code=404)

@app.get("/meme")
def get_meme():
    if os.path.exists(MEME_PATH):
        return FileResponse(MEME_PATH, media_type="image/jpeg")
    return {"message": "Meme não encontrado!"}

@app.post("/predict")
def predict(nota: NotaFiscal):
    resultado = prever_nota(nota, modelo)
    return {"classificacao": resultado}
