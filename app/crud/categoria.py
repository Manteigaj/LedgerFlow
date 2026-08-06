from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Categoria


def criar_categoria(db: Session, nome: str) -> Categoria:
    categoria = Categoria(nome=nome)

    db.add(categoria)
    db.commit()
    db.refresh(categoria)

    return categoria


def buscar_categoria_por_id(
    db: Session,
    categoria_id: int,
) -> Categoria | None:
    return db.get(Categoria, categoria_id)


def buscar_categoria_por_nome(
    db: Session,
    nome: str,
) -> Categoria | None:
    stmt = select(Categoria).where(Categoria.nome == nome)

    return db.scalar(stmt)


def listar_categorias(db: Session) -> list[Categoria]:
    stmt = select(Categoria).order_by(Categoria.nome)

    return list(db.scalars(stmt))


def obter_ou_criar_categoria(
    db: Session,
    nome: str,
) -> Categoria:
    categoria = buscar_categoria_por_nome(db, nome)

    if categoria is not None:
        return categoria

    return criar_categoria(db, nome)
