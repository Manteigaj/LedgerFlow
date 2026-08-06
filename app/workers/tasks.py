from app.database import SessionLocal
from app.services.processamento_service import processar_transacoes
from app.workers.celery_app import celery


@celery.task
def processar_csv(texto: str):
    db = SessionLocal()

    try:
        processar_transacoes(db, texto)

    finally:
        db.close()
