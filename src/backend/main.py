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
from yolo import get_yolo_results

from fastapi import FastAPI, APIRouter, status
import models, report
from database import engine, get_db
import schemas
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response

# Cria o servidor
app = fastapi.FastAPI()

# Define a variavel como a rota da api
router = APIRouter()

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
@app.post("/positions")
def add_positions(positions: Positions):

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


# Cria a tabela e o banco de dados
models.Base.metadata.create_all(bind=engine)

# retorna todos os reports
@router.get('/')
def get_reports(db: Session = Depends(get_db)):#, limit: int = 10, search: str = '1'):
    reports = db.query(models.Report).filter(
        models.Report.id).all()
    return {'status': 'success', 'results': len(reports), 'reports': reports}

# Cria um novo report
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_report(payload: schemas.ReportBaseSchema, db: Session = Depends(get_db)):
    new_report = models.Report(**payload.dict())
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    return {"status": "success", "report": new_report}

# Edita um report já existente
@router.patch('/{reportId}')
def update_report(reportId: str, payload: schemas.ReportBaseSchema, db: Session = Depends(get_db)):
    report_query = db.query(models.Report).filter(models.Report.id == reportId)
    db_report = report_query.first()

    if not db_report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No note with this id: {reportId} found')
    update_data = payload.dict(exclude_unset=True)
    report_query.filter(models.Report.id == reportId).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    db.refresh(db_report)
    return {"status": "success", "report": db_report}

# Retorna o reporte pela id
@router.get('/{reportId}')
def get_post(reportId: str, db: Session = Depends(get_db)):
    report = db.query(models.Report).filter(models.Report.id == reportId).first()
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No note with this id: {id} found")
    return {"status": "success", "report": report}

# Deleta um report por id
@router.delete('/{reportId}')
def delete_post(reportId: str, db: Session = Depends(get_db)):
    report_query = db.query(models.Report).filter(models.Report.id == reportId)
    report = report_query.first()
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No note with this id: {id} found')
    report_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# inclui um novo router '/api/report'
app.include_router(router, tags=['Reports'], prefix='/api/report')


# Executa o servidor
if __name__ == "__main__":
    uvicorn.run(app)