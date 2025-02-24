from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory database
accounts = {
    "1234": {"balance": 1000, "pin": "1111"},
    "5678": {"balance": 500, "pin": "2222"}
}

class Transaction(BaseModel):
    pin: str
    amount: float

@app.get("/balance/{account_id}")
def get_balance(account_id: str, pin: str):
    if account_id in accounts and accounts[account_id]["pin"] == pin:
        return {"balance": accounts[account_id]["balance"]}
    raise HTTPException(status_code=400, detail="Invalid account or PIN")

@app.post("/deposit/{account_id}")
def deposit(account_id: str, transaction: Transaction):
    if account_id in accounts:
        accounts[account_id]["balance"] += transaction.amount
        return {"balance": accounts[account_id]["balance"]}
    raise HTTPException(status_code=400, detail="Account not found")

@app.post("/withdraw/{account_id}")
def withdraw(account_id: str, transaction: Transaction):
    if account_id in accounts and accounts[account_id]["pin"] == transaction.pin:
        if accounts[account_id]["balance"] >= transaction.amount:
            accounts[account_id]["balance"] -= transaction.amount
            return {"balance": accounts[account_id]["balance"]}
        raise HTTPException(status_code=400, detail="Insufficient funds")
    raise HTTPException(status_code=400, detail="Invalid account or PIN")

@app.post("/transfer/{from_id}/{to_id}")
def transfer(from_id: str, to_id: str, transaction: Transaction):
    if from_id in accounts and to_id in accounts and accounts[from_id]["pin"] == transaction.pin:
        if accounts[from_id]["balance"] >= transaction.amount:
            accounts[from_id]["balance"] -= transaction.amount
            accounts[to_id]["balance"] += transaction.amount
            return {"from_balance": accounts[from_id]["balance"], "to_balance": accounts[to_id]["balance"]}
        raise HTTPException(status_code=400, detail="Insufficient funds")
    raise HTTPException(status_code=400, detail="Invalid accounts or PIN")
