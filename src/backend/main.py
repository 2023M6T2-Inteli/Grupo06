# CÓDIGO DO SERVIDOR

# Este script cria o servidor e define rotas para o controle da trajetória do
# robô na simulação e para a detecção de rachaduras em imagens. O envio de pontos
# ainda não foi integrado com a nova navegação por Nav2.
# Para executar o servidor, basta executar o comando "python main.py" no terminal

# Importa bibliotecas
import fastapi
import uvicorn 
import pydantic
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Tuple
# from yolo import get_yolo_results

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

# Array de list de posições
stored_positions = []

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

# Adiciona array de posições
# @app.post("/positions")
# def add_positions(positions: Positions):

#     # Verifica se o array de posições já está cheio
#     if len(stored_positions) == 4:
#         raise fastapi.HTTPException(status_code=400, detail="Positions array is full")
    
#     stored_positions.append(positions.positions)
#     return {"message": "Positions added successfully"}

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
    # print(get_yolo_results("uploaded_image.jpg"))

    return {"message": "Image uploaded successfully"}


#---------------------- 
from fastapi import FastAPI, APIRouter, status

# app = FastAPI()
router = APIRouter()


@router.get('/')
def get_reports():
    return "return a list of scout routes"


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_report():
    return "create report"


@router.patch('/{reportId}')
def update_report(reportId: str):
    return f"update scout with id {reportId}"


@router.get('/{reportId}')
def get_report(reportId: str):
    return f"get scout route with id {reportId}"


@router.delete('/{reportId}')
def delete_report(reportId: str):
    return f"delete scout route with id {reportId}"


app.include_router(router, tags=['Reports'], prefix='/api/report')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with SQLAlchemy"}



#----------------------



# Executa o servidor
if __name__ == "__main__":
    uvicorn.run(app)