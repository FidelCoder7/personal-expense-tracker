const API_URL = "http://127.0.0.1:8000";

async function loadSummary() {
    const response = await fetch(
        `${API_URL}/transactions/summary`
    );

    const data = await response.json();

    document.getElementById("income").textContent =
        data.income;

    document.getElementById("expenses").textContent =
        data.expenses;

    document.getElementById("balance").textContent =
        data.balance;
}

async function loadTransactions() {

    const response = await fetch(
        `${API_URL}/transactions`
    );

    const transactions =
        await response.json();

    const tableBody =
        document.getElementById(
            "transactions-body"
        );

    tableBody.innerHTML = "";

    transactions.forEach(transaction => {

        const row =
            document.createElement("tr");

        row.innerHTML = `
            <td>${transaction.id}</td>
            <td>${transaction.title}</td>
            <td>${transaction.amount}</td>
            <td>${transaction.category}</td>
            <td>${transaction.transaction_type}</td>
            <td>${transaction.date}</td>

            <td>
                 <button
                   class="delete-btn"
                   onclick="deleteTransaction(${transaction.id})"
                 >
                   Delete
                 </button>
            </td>
        `;

        tableBody.appendChild(row);

    });
}

async function initializeDashboard() {
    await loadSummary();
    await loadTransactions();
}



async function createTransaction(event) {

    event.preventDefault();

    const transaction = {

        title:
            document.getElementById("title").value,

        amount:
            parseFloat(
                document.getElementById("amount").value
            ),

        category:
            document.getElementById("category").value,

        transaction_type:
            document.getElementById(
                "transaction_type"
            ).value
    };

    const response = await fetch(
        `${API_URL}/transactions/`,
        {
            method: "POST",
            headers: {
                "Content-Type":
                    "application/json"
            },
            body: JSON.stringify(transaction)
        }
    );

    if (!response.ok) {
        alert("Failed to create transaction");
        return;
    }


    document.getElementById(
        "transaction-form"
    ).reset();

    await loadSummary();
    await loadTransactions();
}

    async function deleteTransaction(id) {

    const confirmed = confirm(
        "Delete this transaction?"
    );

    if (!confirmed) {
        return;
    }

    const response = await fetch(
        `${API_URL}/transactions/${id}`,
        {
            method: "DELETE"
        }
    );

    if (!response.ok) {
        alert("Failed to delete transaction");
        return;
    }

    await loadSummary();
    await loadTransactions();
}

document
    .getElementById("transaction-form")
    .addEventListener(
        "submit",
        createTransaction
    );

initializeDashboard();

