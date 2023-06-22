# CÓDIGO DO SERVIDOR
# Para executar o servidor, basta executar o comando "python main.py" no terminal

# Importa bibliotecas - Em ordem alfabética 
import asyncio
import cv2
import fastapi
import os
import pydantic
import pymysql
import uvicorn
import aiofiles
from fastapi import FastAPI, File, UploadFile, Request, Body, APIRouter, status, Depends, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from typing import List, Tuple
import time
import models
import schemas
from database import engine, get_db
from report import router as reportsRouter
from images import router as imagesRouter 
from gas import router as gasRouter

app = fastapi.FastAPI()

origins = [
    "*"
]

# Define as configurações do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cria a tabela e o banco de dados
models.Base.metadata.create_all(bind=engine)

# inclui um novo router '/report'
app.include_router(reportsRouter, tags=['Reports'], prefix='/report')
app.include_router(imagesRouter, tags=['Images'], prefix='/image')
app.include_router(gasRouter, tags=['Gas'], prefix='/gas')



# Executa o servidor
if __name__ == "__main__":
    uvicorn.run(app)