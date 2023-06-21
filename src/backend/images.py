from datetime import datetime
import schemas
import models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response, UploadFile
from database import get_db
from supabase import create_client, Client
import fastapi
import time
import schemas

router = APIRouter()

# URL e Chave de acesso
url: str = "https://uucjxrxuwtulwesskirt.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV1Y2p4cnh1d3R1bHdlc3NraXJ0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NTY0NTk1MiwiZXhwIjoyMDAxMjIxOTUyfQ.d-_N-_88PmNh1vKtNEc_zZixnOoWKQpHw8ccD-t-cOw"
supabase: Client = create_client(url, key)

# Nome do bucket utilizado
bucket_name: str = "Images"


@router.post("/upload")
def upload(content: UploadFile = fastapi.File(...), db: Session = Depends(get_db)):
    last = db.query(models.Report).order_by(models.Report.id.desc()).first()

    if last.isFinished == 0:
        dados = content.file.read()
        filename = f"project_{last.id}_{time.time()}"
        res = supabase.storage.from_(bucket_name).upload(filename, dados)
        url = f'https://uucjxrxuwtulwesskirt.supabase.co/storage/v1/object/public/Images/{filename}'
        img = models.Image()
        img.reportId = last.id
        img.url = url
        db.add(img)
        db.commit()
        db.refresh(img)
        return {"status": "ok"}
    else:
        return {"error": "no project running at the moment"}

