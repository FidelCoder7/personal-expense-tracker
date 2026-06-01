from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():

    response = client.get("/")

    assert response.status_code == 200

def test_create_transaction_endpoint():

    payload = {
        "title": "Salary",
        "amount": 5000,
        "category": "Work",
        "transaction_type": "Income"
    }

    response = client.post(
        "/transactions/",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Salary"

def test_get_transactions():

    response = client.get(
        "/transactions/"
    )

    assert response.status_code == 200

def test_summary_endpoint():

    response = client.get(
        "/transactions/summary"
    )

    assert response.status_code == 200

    data = response.json()

    assert "income" in data
    assert "expenses" in data
    assert "balance" in data

def test_transaction_not_found():

    response = client.get(
        "/transactions/99999"
    )

    assert response.status_code == 404
