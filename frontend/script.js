const API_URL = "http://127.0.0.1:8000";

let expenseChart = null;

let editingTransactionId = null;

function renderChart(summaryData) {

    const ctx =
        document
            .getElementById("expenseChart")
            .getContext("2d");

    if (expenseChart) {
        expenseChart.destroy();
    }

    expenseChart = new Chart(ctx, {
        type: "bar",

        data: {
            labels: [
                "Income",
                "Expenses"
            ],

            datasets: [
                {
                    label: "Amount",

                    data: [
                        summaryData.income,
                        summaryData.expenses
                    ],

                    backgroundcolor: [
                        "#16a34a",
                        "#dc2626"

                    
                    ],
                    borderwidth: 1
                }
            ]
        },

        options: {
            responsive: true,

            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

async function loadSummary() {
    const response = await fetch(
        `${API_URL}/transactions/summary`
    );

    const data = await response.json();

    document.getElementById("income").textContent =
        `KES ${data.income.toFixed(2)}`;

    document.getElementById("expenses").textContent =
        `KES ${data.expenses.toFixed(2)}`;

    document.getElementById("balance").textContent =
        `KES ${data.balance.toFixed(2)}`;

    renderChart(data);
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
                    onclick="editTransaction(${transaction.id})"
                >
                    Edit
                 </button>

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

     let url =
        `${API_URL}/transactions/`;

    let method = "POST";

    if (editingTransactionId) {

        url =
            `${API_URL}/transactions/${editingTransactionId}`;

        method = "PUT";
    }

    const response = await fetch(
        url,
        {
            method: method,

            headers: {
                "Content-Type":
                    "application/json"
            },

            body:
                JSON.stringify(transaction)
        }
    );

    if (!response.ok) {
        alert("Operation failed");
        return;
    }

    document
        .getElementById(
            "transaction-form"
        )
        .reset();
        
    document.getElementById(
    "cancel-edit"
).style.display = "none";

    editingTransactionId = null;

    document.querySelector(
        "#transaction-form button"
    ).textContent = "Add Transaction";

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

async function editTransaction(id) {

    const response = await fetch(
        `${API_URL}/transactions/${id}`
    );

    const transaction =
        await response.json();

    document.getElementById("title").value =
        transaction.title;

    document.getElementById("amount").value =
        transaction.amount;

    document.getElementById("category").value =
        transaction.category;

    document.getElementById("transaction_type").value =
        transaction.transaction_type;
    
    document.getElementById(
    "cancel-edit"
    ).style.display = "inline-block";

    editingTransactionId = id;

    document.querySelector(
        "#transaction-form button"
    ).textContent = "Update Transaction";
}

function cancelEdit() {

    editingTransactionId = null;

    document
        .getElementById(
            "transaction-form"
        )
        .reset();

    document.querySelector(
        "#transaction-form button"
    ).textContent = "Add Transaction";

    document.getElementById(
        "cancel-edit"
    ).style.display = "none";
}

document
    .getElementById("transaction-form")
    .addEventListener(
        "submit",
        createTransaction
    );

document
    .getElementById("cancel-edit")
    .addEventListener(
        "click",
        cancelEdit
    );

initializeDashboard();

