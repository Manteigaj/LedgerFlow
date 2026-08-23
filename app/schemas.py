from datetime import date

from pydantic import BaseModel, ConfigDict, Field


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

    model_config = ConfigDict(from_attributes=True)


class UploadResponse(BaseModel):
    message: str
    quantity: int


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=255)
    password: str = Field(min_length=8, max_length=128)


class UserResponse(BaseModel):
    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    username: str
    password: str
