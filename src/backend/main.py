# CÓDIGO DO SERVIDOR

# Este script cria o servidor e define três rotas para o controle da rota do
# robô na simulação. É possível enviar o comando de formato (letra G ou quadrado) 
# ou de ponto específico para onde o robô deve ir. Nesse sentido, duas rotas POST
# são definidas para receber o formato ou a posição, e uma rota GET é definida para
# retornar o comando ou a posição, dependendo do que foi enviado por último.

# Para executar o servidor, basta executar o comando "python main.py" no terminal

# Importa bibliotecas
import fastapi
import uvicorn 
import pydantic
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request, Body
from fastapi.responses import FileResponse, StreamingResponse
import cv2
import os
from supabase import create_client, Client
import asyncio
import aiofiles
import time
from yolo import get_yolo_results

# Cria o servidor
app = fastapi.FastAPI()

# Define as origens permitidas para o servidor
origins = [
    "http://localhost",
    "http://localhost:3000",
]

# Define as configurações do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define as classes para o formato e a posição
class Shape(pydantic.BaseModel):
    shape: str

class Position(pydantic.BaseModel):
    x: float
    y: float

# Define as variáveis globais para o formato e a posição
shape = Shape(shape='')
point = Position(x=0.0, y=0.0)

# Define a variável global para indicar se o comando enviado foi de formato ou posição
is_shape = False

# URL e Chave de acesso 
url: str = "https://uucjxrxuwtulwesskirt.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV1Y2p4cnh1d3R1bHdlc3NraXJ0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NTY0NTk1MiwiZXhwIjoyMDAxMjIxOTUyfQ.d-_N-_88PmNh1vKtNEc_zZixnOoWKQpHw8ccD-t-cOw"
supabase: Client = create_client(url, key)

#Nome do bucket utilizado
bucket_name: str = "Images"


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

# Rotas para receber o comando de formato 
@app.post("/shape")
def set_shape(_shape: Shape):
    global is_shape
    is_shape = True

    global shape
    shape = _shape

# Rota para receber o comando de posição
@app.post("/position")
def set_position(_position: Position):
    global is_shape
    is_shape = False

    global point
    point = _position

# @app.post("/upload-image")
# async def upload_image(image: bytes = fastapi.File(...)): 
#     print('bati')
#     with open("uploaded_image.jpg", "wb") as file:
#         file.write(image)
#     print(get_yolo_results("uploaded_image.jpg"))

#     return {"message": "Image uploaded successfully"}

@app.get('/video')
def video_feed(request:Request):
    return StreamingResponse(get_yolo_results(), media_type='multipart/x-mixed-replace; boundary=frame')

@app.get("/hi")
def hi():
    return "hi"

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