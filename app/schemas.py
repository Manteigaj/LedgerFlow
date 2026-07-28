from datetime import date
from pydantic import BaseModel, ConfigDict


class TransacaoBase(BaseModel):
    data: date
    descricao: str
    valor: float


class TransacaoCreate(TransacaoBase):
    pass


class TransacaoResponse(TransacaoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class UploadResponse(BaseModel):
    mensagem: str
    quantidade: int
