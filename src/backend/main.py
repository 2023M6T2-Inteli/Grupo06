# CÓDIGO DO SERVIDOR
# Este script cria o servidor e define rotas para o controle da trajetória do
# robô na simulação e para a detecção de rachaduras em imagens. O envio de pontos
# ainda não foi integrado com a nova navegação por Nav2.
# Para executar o servidor, basta executar o comando "python main.py" no terminal

# Importa bibliotecas - Em ordem alfabética 
import asyncio
import aiofiles
import cv2
import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request, Body
from fastapi.responses import FileResponse, StreamingResponse
import os
import pydantic
from supabase import create_client, Client
import time
from typing import List, Tuple
import uvicorn 
from yolo import get_yolo_results

from database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, create_engine, Integer, Date, Float
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "sqlite://admin:Gerdaudb#1@db-gerdau.cfssllf0qlz6.us-east-1.rds.amazonaws.com/db-gerdau.db"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# Base.metadata.create_all(bind=engine)

# Cria o servidor
app = fastapi.FastAPI()

# Define as origens permitidas para o servidor
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]

# Define as configurações do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Array de list de posições
stored_positions = []

# URL e Chave de acesso 
url: str = "https://uucjxrxuwtulwesskirt.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV1Y2p4cnh1d3R1bHdlc3NraXJ0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NTY0NTk1MiwiZXhwIjoyMDAxMjIxOTUyfQ.d-_N-_88PmNh1vKtNEc_zZixnOoWKQpHw8ccD-t-cOw"
supabase: Client = create_client(url, key)

#Nome do bucket utilizado
bucket_name: str = "Images"

# Classe para representar posições nas rotas
class Positions:
    def __init__(self, positions: List[Tuple[int, int]]):
        self.positions = positions

    def get_positions(self) -> List[Tuple[int, int]]:
        return self.positions

# Retorna array de posições
@app.get("/positions")
def get_positions():
    return stored_positions

# Rota para retornar o comando ou a posição
@app.get("/mission")
def get_mission():
    global is_shape
    # Se o comando enviado foi de formato, retorna o formato
    if(is_shape):
        global shape
        past_shape = shape
        shape = Shape(shape='') # Reseta o formato
        return past_shape
    # Se o comando enviado foi de posição, retorna a posição
    else:
        is_shape = True # Muda para formato para o próximo comando, evitando que o robô tenta ir para a mesma posição
        global point
        return point

    # Verifica se o array de posições já está cheio
    if len(stored_positions) == 4:
        raise fastapi.HTTPException(status_code=400, detail="Positions array is full")
    
    stored_positions.append(positions.positions)
    return {"message": "Positions added successfully"}

# Deleta posições
@app.delete("/positions")
def clear_positions():
    stored_positions.clear()
    return {"message": "Positions cleared successfully"}

# Rota para enviar imagem para detecção de rachaduras
@app.post("/upload-image")
async def upload_image(image: bytes = fastapi.File(...)): 
    # Salva imagem
    with open("uploaded_image.jpg", "wb") as file:
        file.write(image)

    # Printa resultados
    print(get_yolo_results("uploaded_image.jpg"))

    return {"message": "Image uploaded successfully"}

@app.get('/video')
def video_feed(request:Request):
    return StreamingResponse(get_yolo_results(), media_type='multipart/x-mixed-replace; boundary=frame')

@app.get("/list")
async def list():
    # Lista todas as imagens do Bucket 
    res = supabase.storage.from_(bucket_name).list()
    print(res)

@app.post("/upload")
def upload(content: UploadFile = fastapi.File(...)):    
    with open(f"./recebidos/imagem{time.time()}.png", 'wb') as f:
        dados = content.file.read()
        f.write(dados)
        #pass
    return {"status": "ok"}

@app.post("/images")
def images():
    list_files = os.listdir("./recebidos")
    # Rota da imagem local para ser feito o upload (no meu caso esta na pasta mock e é a imagem "lala.png")
    for arquivo in list_files:
        with open(os.path.join("./recebidos", arquivo), 'rb+') as f:
            dados = f.read()
            res = supabase.storage.from_(bucket_name).upload(f"{time.time()}_{arquivo}", dados)
    return {"message": "Image uploaded successfully"}


# Executa o servidor
if __name__ == "__main__":
    uvicorn.run(app)