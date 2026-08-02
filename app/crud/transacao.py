from datetime import datetime

from sqlalchemy.orm import Session

from app.crud.categoria import obter_ou_criar_categoria
from app.models import Transacao
from app.services.csv_service import converter_valor
from app.services.categorizacao import categorizar


def salvar_transacoes(db: Session, linhas):
    transacoes = []

    for linha in linhas:
        categoria_nome = categorizar(linha["descricao"])

        categoria = obter_ou_criar_categoria(
            db=db,
            nome=categoria_nome,
        )

        transacao = Transacao(
            data=datetime.strptime(
                linha["data"],
                "%Y-%m-%d",
            ).date(),
            descricao=linha["descricao"],
            valor=converter_valor(linha["valor"]),
            categoria_id=categoria.id,
        )

        transacoes.append(transacao)

    db.add_all(transacoes)
    db.commit()

    return len(transacoes)
