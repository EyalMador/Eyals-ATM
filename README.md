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

1. **In-Memory Storage**: The application uses a simple dictionary to store account balances. This keeps the implementation lightweight but does not persist data across server restarts.
2. **Pydantic Model for Transactions**: A `Transaction` model is used to enforce structured data input, ensuring that deposits and withdrawals always receive a valid `amount`.
3. **Error Handling**: The API provides clear error messages and uses appropriate HTTP status codes (400 for invalid input, 200 for successful operations).
4. **Automatic Account Creation**: If a deposit is made to a non-existent account, it is automatically initialized with a balance of zero before adding the deposit.

## Challenges Faced

1. **Handling JSON Input Correctly**: Initially, the API was designed to accept amounts as query parameters, but this caused issues with `requests.post()`. Switching to JSON input using a Pydantic model resolved the problem.
2. **Deploying on Render**: Setting up the `Procfile` and ensuring the correct dependencies in `requirements.txt` was necessary to successfully deploy the API.

This API is currently deployed and accessible at: [ATM API](https://eyals-atm.onrender.com/).
