from fastapi import FastAPI

app = FastAPI(
    title="Expense Tracker API",
    description="Personal Expense Tracker Backend",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Expense Tracker API is running"
    }
