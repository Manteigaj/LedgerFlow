from fastapi import APIRouter, File, UploadFile
from app.schemas import UploadResponse
from app.services.csv_service import ler_csv


router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post(
    "/csv",
    response_model=UploadResponse,
)
async def upload_csv(
    arquivo: UploadFile = File(...),
):
    conteudo = await arquivo.read()

    texto = conteudo.decode("utf-8")

    dados = ler_csv(texto)

    quantidade = len(dados)

    return UploadResponse(
        mensagem="Arquivo importado com sucesso.",
        quantidade=quantidade,
    )
