from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate
)

def create_transaction(
    db: Session,
    transaction_data: TransactionCreate
):
    transaction = Transaction(
        title=transaction_data.title,
        amount=transaction_data.amount,
        category=transaction_data.category,
        transaction_type=transaction_data.transaction_type
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction

def get_transactions(db: Session):
    return db.query(Transaction).all()

def get_transaction_by_id(
    db: Session,
    transaction_id: int
):
    return (
        db.query(Transaction)
        .filter(Transaction.id == transaction_id)
        .first()
    )

def update_transaction(
    db: Session,
    transaction_id: int,
    transaction_data: TransactionUpdate
):
    transaction = get_transaction_by_id(
        db,
        transaction_id
    )

    if not transaction:
        return None

    update_data = transaction_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(transaction, field, value)

    db.commit()
    db.refresh(transaction)

    return transaction

def delete_transaction(
    db: Session,
    transaction_id: int
):
    transaction = get_transaction_by_id(
        db,
        transaction_id
    )

    if not transaction:
        return False

    db.delete(transaction)
    db.commit()

    return True

def get_summary(db: Session):
    transactions = db.query(Transaction).all()

    income = 0
    expenses = 0

    for t in transactions:
        if not t.amount or not t.transaction_type:
            continue

        if t.transaction_type.lower() == "income":
            income += t.amount
        elif t.transaction_type.lower() == "expense":
            expenses += t.amount


    return {
        "income": income,
        "expenses": expenses,
        "balance": income - expenses
    }


