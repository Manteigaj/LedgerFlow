from sqlalchemy.orm import Session
from app.services.categorizacao import categorizar
from app.crud.transacao import salvar_transacoes
from app.services.csv_service import ler_csv


def processar_transacoes(
    db: Session,
    texto: str,
):
    dados = ler_csv(texto)

    for transacao in dados:
        categoria = categorizar(transacao["descricao"])

        transacao["categoria"] = categoria

    salvar_transacoes(db, dados)
