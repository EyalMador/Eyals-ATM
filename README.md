# Eyal's ATM API

Welcome to **Eyal's ATM**, a simple banking service implemented using FastAPI.

## Base URL

```
https://eyals-atm.onrender.com/
```

## Endpoints

### Get Account Balance

- **Endpoint:** `GET /accounts/{account_id}/balance`
- **Description:** Returns the balance of the specified account.
- **Response:**
  - `200 OK`: `{"balance": <current_balance>}`
  - `400 Bad Request`: `{"detail": "Invalid account"}`

### Deposit Money

- **Endpoint:** `POST /accounts/{account_id}/deposit`
- **Description:** Deposits money into the account. If the account does not exist, it is initialized.
- **Request Body:**
  ```json
  { "amount": <positive_float> }
  ```
- **Response:**
  - `200 OK`: `{"balance": <updated_balance>}`
  - `400 Bad Request`: `{"detail": "Invalid amount, must be positive"}`

### Withdraw Money

- **Endpoint:** `POST /accounts/{account_id}/withdraw`
- **Description:** Withdraws money from the account if sufficient funds exist.
- **Request Body:**
  ```json
  { "amount": <positive_float> }
  ```
- **Response:**
  - `200 OK`: `{"balance": <updated_balance>}`
  - `400 Bad Request`: `{"detail": "Invalid amount, must be positive"}`
  - `400 Bad Request`: `{"detail": "Invalid account"}`
  - `400 Bad Request`: `{"detail": "Insufficient funds"}`

## Design Decisions

- **In-Memory Storage:** The application uses an in-memory dictionary to store account balances, meaning data resets on each server restart.
- **Pydantic Validation:** The API enforces correct data input using Pydantic models.
- **Automatic Account Creation:** Depositing into a nonexistent account initializes it with the deposited amount.

## Challenges Faced

- **Persisting Data:** Since the application runs in-memory, data does not persist between deployments.
- **Error Handling:** Proper error messages were implemented for invalid operations and incorrect inputs.

## Future Improvements

- **Database Integration:** Using a database like PostgreSQL or SQLite to persist accounts.
- **Authentication:** Adding authentication to secure accounts.
- **Transaction History:** Keeping a log of transactions for each account.

This API is currently deployed and accessible at: [ATM API](https://eyals-atm.onrender.com/).

