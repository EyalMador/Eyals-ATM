from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="ATM API", description="Basic ATM operations", version="1.0")

# In-memory database
accounts = {}

# Define a Pydantic model for transaction
class Transaction(BaseModel):
    amount: float

@app.get("/")
async def read_root():
    return {"message": "Welcome to Eyal's ATM!"}

@app.get("/accounts/{account_id}/balance")
def get_balance(account_id: int):
    """Returns the balance of a given account."""
    if account_id in accounts:
        return {"balance": accounts[account_id]}
    raise HTTPException(status_code=400, detail="Invalid account")

@app.post("/accounts/{account_id}/deposit")
def deposit(account_id: int, transaction: Transaction):
    """Deposits money into the account."""
    amount = transaction.amount
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount, must be positive")
    
    if account_id not in accounts:
        accounts[account_id] = 0  # Initialize the account if it doesn't exist
    
    accounts[account_id] += amount
    return {"balance": accounts[account_id]}

@app.post("/accounts/{account_id}/withdraw")
def withdraw(account_id: int, transaction: Transaction):
    """Withdraws money from the account."""
    amount = transaction.amount
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount, must be positive")
    
    if account_id not in accounts:
        raise HTTPException(status_code=400, detail="Invalid account")
    
    if accounts[account_id] >= amount:
        accounts[account_id] -= amount
        return {"balance": accounts[account_id]}
    
    raise HTTPException(status_code=400, detail="Insufficient funds")
