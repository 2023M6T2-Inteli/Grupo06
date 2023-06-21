
from datetime import datetime
import schemas
import models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import get_db

router = APIRouter()

# retorna todos os reports
@router.get('/')
def get_reports(db: Session = Depends(get_db), limit: int = 10, search: str = ''):
    reports = db.query(models.Report).all()
    return {'status': 'success', 'results': len(reports), 'reports': reports}


@router.get('/last')
def get_current_state(db: Session = Depends(get_db)):
    last = db.query(models.Report).order_by(models.Report.id.desc()).first()
    return {
        "last": last
    }

# Cria um novo report
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_report(payload: schemas.ReportBaseSchema, db: Session = Depends(get_db)):
    new_report = models.Report(**payload.dict())
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    return {"status": "success", "report": new_report}

@router.get('/finish')
def get_current_state(db: Session = Depends(get_db)):
    last = db.query(models.Report).order_by(models.Report.id.desc()).first()
    last.isFinished = 1
    db.commit()
    return {
        'status': 'success',
    }

# Edita um report já existente
@router.put('/{reportId}')
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
    report = db.query(models.Report).filter(
        models.Report.id == reportId).first()
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No note with this id: {id} found")
    return {"status": "success", "report": report.return_json()}

# Deleta um report por id
@router.delete('/{reportId}')
def delete_post(reportId: str, db: Session = Depends(get_db)):
    report_query = db.query(models.Report).filter(models.Report.id == reportId)
    report = report_query.first()
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No report with this id: {id} found')
    report_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
