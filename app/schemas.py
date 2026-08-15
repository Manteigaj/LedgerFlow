from datetime import date

from pydantic import BaseModel


class TransactionBase(BaseModel):
    date: date
    description: str
    amount: float


class TransactionCreate(TransactionBase):
    pass


class TransactionResponse(BaseModel):
    id: int
    date: date
    description: str
    amount: float

    class Config:
        from_attributes = True


class UploadResponse(BaseModel):
    message: str
    quantity: int
