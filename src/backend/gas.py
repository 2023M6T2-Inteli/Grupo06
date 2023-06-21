from datetime import datetime
import schemas
import models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import get_db
from globalVars import projectIsRunning, currentProjectId

router = APIRouter()

@router.get('/')
def get_gas_values(db: Session = Depends(get_db)):
    gas_value = db.query(models.Gas).all()
    return {'status': 'success', 'results': len(gas_value), 'gas value': gas_value}

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_gas(payload: schemas.GasBaseSchema, db: Session = Depends(get_db)):
    new_gas_value = models.Gas(**payload.dict())
    db.add(new_gas_value)
    db.commit()
    db.refresh(new_gas_value)
    return{"status": "success", "gas value": new_gas_value}

@router.delete('/{gasId}')
def delete_gas_read(gasId: str, db: Session = Depends(get_db)):
    gas_query = db.query(models.Gas).filter(models.Gas.id == gasId)
    gas = gas_query.first()
    if not gas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No gas value with this id: {id} found')
    gas_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)