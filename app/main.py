from fastapi import FastAPI

from app.database.database import Base
from app.database.database import engine
from app.schemas import TransactionCreate

from app.models import Transaction
app = FastAPI(
    title="Expense Tracker API",
    description="Personal Expense Tracker Backend",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "Expense Tracker API is running"
    }

@app.post("/test")
def test_schema(transaction: TransactionCreate):
    return transaction
