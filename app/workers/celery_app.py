import os

from celery import Celery


REDIS_URL = os.getenv("REDIS_URL")

if not REDIS_URL:
    raise RuntimeError("REDIS_URL not found.")


celery = Celery(
    "ledgerflow",
    broker=REDIS_URL,
    backend=REDIS_URL,
)

celery.autodiscover_tasks(["app.workers"])
