from datetime import date
from pydantic import BaseModel


class TransacaoBase(BaseModel):
    data: date
    descricao: str
    valor: float


class TransacaoCreate(TransacaoBase):
    pass


class TransacaoResponse(BaseModel):
    id: int
    data: date
    descricao: str
    valor: float

    class Config:
        from_attributes = True


class UploadResponse(BaseModel):
    mensagem: str
    quantidade: int
