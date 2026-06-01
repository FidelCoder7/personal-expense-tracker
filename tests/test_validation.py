from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_empty_title():

    payload = {
        "title": "",
        "amount": 100,
        "category": "Food",
        "transaction_type": "Expense"
    }

    response = client.post(
        "/transactions/",
        json=payload
    )

    assert response.status_code == 422

def test_missing_amount():

    payload = {
        "title": "Food",
        "category": "Food",
        "transaction_type": "Expense"
    }

    response = client.post(
        "/transactions/",
        json=payload
    )

    assert response.status_code == 422
