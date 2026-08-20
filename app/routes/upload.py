from fastapi import APIRouter, Depends, File, UploadFile
from app.auth.dependencies import get_current_user_id
from app.schemas import UploadResponse
from app.workers.tasks import process_csv


router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/csv", response_model=UploadResponse)
async def upload_csv(
    file: UploadFile = File(...), user_id: int = Depends(get_current_user_id)
):
    content = await file.read()
    text = content.decode("utf-8")

    process_csv.delay(text, user_id)

    return UploadResponse(
        message="File sent for processing.",
        quantity=0,
    )
