from fastapi import APIRouter, File, UploadFile
from app.schemas import UploadResponse
from app.workers.tasks import process_csv


router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/csv", response_model=UploadResponse)
async def upload_csv(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    process_csv.delay(text)

    return UploadResponse(
        message="File sent for processing.",
        quantity=0,
    )
