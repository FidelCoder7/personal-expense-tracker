from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from app.services.transaction_services import get_summary

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
    TransactionResponse
)

from app.services.transaction_services import (
    create_transaction,
    get_transactions,
    get_transaction_by_id,
    update_transaction,
    delete_transaction
)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.post(
    "/",
    response_model=TransactionResponse,
    status_code=201
)
def create_new_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    return create_transaction(
        db,
        transaction
    )

@router.get(
    "/",
    response_model=list[TransactionResponse]
)
def get_all_transactions(
    db: Session = Depends(get_db)
):
    return get_transactions(db)

@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    return get_summary(db)

@router.get("/{transaction_id}")
def summary(db: Session = Depends(get_db)):
    return get_summary(db)


def get_single_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    transaction = get_transaction_by_id(
        db,
        transaction_id
    )

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transaction

@router.put(
    "/{transaction_id}",
    response_model=TransactionResponse
)
def update_existing_transaction(
    transaction_id: int,
    transaction: TransactionUpdate,
    db: Session = Depends(get_db)
):
    updated_transaction = update_transaction(
        db,
        transaction_id,
        transaction
    )

    if not updated_transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return updated_transaction

@router.delete(
    "/{transaction_id}"
)
def delete_existing_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    success = delete_transaction(
        db,
        transaction_id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return {
        "message": "Transaction deleted successfully"
    }





