from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="ATM System", description="A simple ATM server", version="1.0")

# In-memory account storage
accounts = {
    "1001": {"balance": 1000},
    "1002": {"balance": 500}
}

class Transaction(BaseModel):
    amount: float

@app.get("/accounts/{account_number}/balance", summary="Get account balance")
def get_balance(account_number: str):
    if account_number in accounts:
        return {"account_number": account_number, "balance": accounts[account_number]["balance"]}
    raise HTTPException(status_code=404, detail="Account not found")

@app.post("/accounts/{account_number}/deposit", summary="Deposit money")
def deposit(account_number: str, transaction: Transaction):
    if account_number in accounts:
        accounts[account_number]["balance"] += transaction.amount
        return {"message": "Deposit successful", "balance": accounts[account_number]["balance"]}
    raise HTTPException(status_code=404, detail="Account not found")

@app.post("/accounts/{account_number}/withdraw", summary="Withdraw money")
def withdraw(account_number: str, transaction: Transaction):
    if account_number in accounts:
        if accounts[account_number]["balance"] >= transaction.amount:
            accounts[account_number]["balance"] -= transaction.amount
            return {"message": "Withdrawal successful", "balance": accounts[account_number]["balance"]}
        raise HTTPException(status_code=400, detail="Insufficient funds")
    raise HTTPException(status_code=404, detail="Account not found")
