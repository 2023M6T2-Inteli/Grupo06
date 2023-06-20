from datetime import datetime
import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response, UploadFile
from database import get_db
from supabase import create_client, Client
import fastapi 
from globalVars import projectIsRunning, currentProjectId

router = APIRouter()

# URL e Chave de acesso 
url: str = "https://uucjxrxuwtulwesskirt.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV1Y2p4cnh1d3R1bHdlc3NraXJ0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NTY0NTk1MiwiZXhwIjoyMDAxMjIxOTUyfQ.d-_N-_88PmNh1vKtNEc_zZixnOoWKQpHw8ccD-t-cOw"
supabase: Client = create_client(url, key)

#Nome do bucket utilizado
bucket_name: str = "Images"

@router.post("/upload")
def upload(content: UploadFile = fastapi.File(...)):
    global projectIsRunning
    print(projectIsRunning)
    if projectIsRunning:
        dados = content.file.read()
        res = supabase.storage.from_(bucket_name).upload(f"project_{currentProjectId}_{time.time()}", dados)
        return {"status": "ok"}
    else: 
        return {"error": "no project running at the moment"}