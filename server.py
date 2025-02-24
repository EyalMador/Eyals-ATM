from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="ATM API", description="Basic ATM operations", version="1.0")

# In-memory database
accounts = {
    "account1": {"balance": 1000},
    "account2": {"balance": 1500},
    "account3": {"balance": 2000}
}

class Transaction(BaseModel):
    amount: float

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/balance/{account_id}")
def get_balance(account_id: str):
    """Returns the balance of a given account."""
    if account_id in accounts:
        return {"balance": accounts[account_id]["balance"]}
    raise HTTPException(status_code=400, detail="Invalid account")

@app.post("/deposit/{account_id}")
def deposit(account_id: str, transaction: Transaction):
    """Deposits money into the account."""
    if account_id in accounts:
        accounts[account_id]["balance"] += transaction.amount
        return {"balance": accounts[account_id]["balance"]}
    raise HTTPException(status_code=400, detail="Account not found")

@app.post("/withdraw/{account_id}")
def withdraw(account_id: str, transaction: Transaction):
    """Withdraws money from the account."""
    if account_id in accounts:
        if accounts[account_id]["balance"] >= transaction.amount:
            accounts[account_id]["balance"] -= transaction.amount
            return {"balance": accounts[account_id]["balance"]}
        raise HTTPException(status_code=400, detail="Insufficient funds")
    raise HTTPException(status_code=400, detail="Invalid account")
