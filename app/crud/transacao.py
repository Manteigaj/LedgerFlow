from datetime import datetime
from sqlalchemy.orm import Session
from app.models import Transacao


def salvar_transacoes(db: Session, linhas):
    transacoes = []

    for linha in linhas:
        transacoes.append(
            Transacao(
                data=datetime.strptime(linha["data"], "%d/%m/%Y").date(),
                descricao=linha["descricao"],
                valor=float(linha["valor"]),
            )
        )

    db.add_all(transacoes)
    db.commit()

    return len(transacoes)
