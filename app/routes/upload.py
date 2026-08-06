from fastapi import APIRouter, UploadFile, File
from app.schemas import UploadResponse
from app.workers.tasks import processar_csv

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/csv", response_model=UploadResponse)
async def upload_csv(arquivo: UploadFile = File(...)):
    conteudo = await arquivo.read()
    texto = conteudo.decode("utf-8")

    processar_csv.delay(texto)

    return UploadResponse(
        mensagem="Arquivo enviado para processamento.",
        quantidade=0,
    )
