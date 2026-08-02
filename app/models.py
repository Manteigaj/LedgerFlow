from datetime import date

from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Categoria(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(255))

    transacoes: Mapped[list["Transacao"]] = relationship(back_populates="categoria")


class Transacao(Base):
    __tablename__ = "transacoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[date]
    descricao: Mapped[str] = mapped_column(String(255))
    valor: Mapped[float] = mapped_column(Float)

    categoria_id: Mapped[int | None] = mapped_column(ForeignKey("categorias.id"))

    categoria: Mapped["Categoria"] = relationship(back_populates="transacoes")
