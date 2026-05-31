from fastapi import FastAPI

from app.database.database import Base
from app.database.database import engine

from app.models import Transaction

from app.routes.transactions import router as transaction_router

app = FastAPI(
    title="Expense Tracker API",
    description="Personal Expense Tracker Backend",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(transaction_router)


@app.get("/")
def root():
    return {
        "message": "Expense Tracker API is running"
    }




