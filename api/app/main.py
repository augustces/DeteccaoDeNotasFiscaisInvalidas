from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from app.predict import prever_nota
from app.notafiscal import NotaFiscal
import joblib
import os

# Caminhos do meme
MEME_PATH = os.path.join("app", "img", "status200.jpg") 

# Criação da API
app = FastAPI()

# Função para carregar o modelo em cada requisição (evita concorrência)
def get_model():
    return joblib.load("modelo/random_forest_model.pkl")

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
async def predict(nota: NotaFiscal, modelo=Depends(get_model)):
    resultado = prever_nota(nota, modelo)
    return {"classificacao": resultado}
