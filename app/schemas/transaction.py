from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class TransactionBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=1, max_length=50)
    transaction_type: str = Field(..., min_length=1, max_length=20)


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    amount: Optional[float] = Field(None, gt=0)
    category: Optional[str] = Field(None, min_length=1, max_length=50)
    transaction_type: Optional[str] = Field(None, min_length=1, max_length=20)


class TransactionResponse(TransactionBase):
    id: int
    date: date

    model_config = {
        "from_attributes": True
    }
