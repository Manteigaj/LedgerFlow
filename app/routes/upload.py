from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UploadResponse
from app.services.csv_service import ler_csv
from app.crud.transacao import salvar_transacoes
from app.schemas import TransacaoResponse
from app.models import Transacao

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/csv", response_model=UploadResponse)
async def upload_csv(arquivo: UploadFile = File(...), db: Session = Depends(get_db)):
    conteudo = await arquivo.read()

    texto = conteudo.decode("utf-8")

    dados = ler_csv(texto)

    quantidade = len(dados)

    salvar_transacoes(db, dados)

    return UploadResponse(
        mensagem="Arquivo importado com sucesso.",
        quantidade=quantidade,
    )


@router.get("/listar_transacoes", response_model=list[TransacaoResponse])
async def listar_transacoes(db: Session = Depends(get_db)):
    transacoes = db.query(Transacao).all()
    return transacoes
