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

# Cria o servidor
app = fastapi.FastAPI()

from yolo import get_yolo_results

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

stored_positions = []

class Positions:
    def __init__(self, positions: List[Tuple[int, int]]):
        self.positions = positions

    def get_positions(self) -> List[Tuple[int, int]]:
        return self.positions

@app.get("/positions")
def get_positions():
    return stored_positions

@app.post("/positions")
def add_positions(positions: Positions):
    if len(stored_positions) == 4:
        raise HTTPException(status_code=400, detail="Positions array is full")
    stored_positions.append(positions.positions)
    return {"message": "Positions added successfully"}

@app.delete("/positions")
def clear_positions():
    stored_positions.clear()
    return {"message": "Positions cleared successfully"}

@app.post("/upload-image")
async def upload_image(image: bytes = fastapi.File(...)): 
    print('bati')
    with open("uploaded_image.jpg", "wb") as file:
        file.write(image)
    print(get_yolo_results("uploaded_image.jpg"))

    return {"message": "Image uploaded successfully"}

# Executa o servidor
if __name__ == "__main__":
    uvicorn.run(app)