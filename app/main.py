from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from app.database.database import Base
from app.database.database import engine

from app.models import Transaction

from app.routes.transactions import router as transaction_router

app = FastAPI(
    title="Expense Tracker API",
    description="Personal Expense Tracker Backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(transaction_router)


@app.get("/")
def root():
    return {
        "message": "Expense Tracker API is running"
    }





