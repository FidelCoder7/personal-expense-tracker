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
        `;

        tableBody.appendChild(row);

    });
}

async function initializeDashboard() {
    await loadSummary();
    await loadTransactions();
}

initializeDashboard();

