from app.database import SessionLocal
from app.services.processing_service import process_transactions
from app.workers.celery_app import celery


@celery.task
def process_csv(text: str, user_id: int):
    db = SessionLocal()

    try:
        process_transactions(db, text, user_id)

    finally:
        db.close()
