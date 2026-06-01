from app.schemas.transaction import TransactionCreate
from app.services.transaction_services import (
    create_transaction,
    get_summary
)
def test_create_transaction(db_session):

    transaction = TransactionCreate(
        title="Salary",
        amount=5000,
        category="Work",
        transaction_type="Income"
    )

    created = create_transaction(
        db_session,
        transaction
    )

    assert created.id is not None
    assert created.title == "Salary"
    assert created.amount == 5000

def test_summary_calculation(db_session):

    income = TransactionCreate(
        title="Salary",
        amount=5000,
        category="Work",
        transaction_type="Income"
    )

    expense = TransactionCreate(
        title="Food",
        amount=1000,
        category="Food",
        transaction_type="Expense"
    )

    create_transaction(db_session, income)
    create_transaction(db_session, expense)

    summary = get_summary(db_session)

    assert summary["income"] == 5000
    assert summary["expenses"] == 1000
    assert summary["balance"] == 4000
