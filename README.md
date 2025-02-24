# ATM API

## Overview

This is a simple ATM API built using FastAPI. It provides basic ATM operations such as checking account balances, depositing, and withdrawing funds. The server uses an in-memory database to store account balances.

## Design Decisions

- **Framework**: FastAPI was chosen for its ease of use and automatic generation of interactive API documentation.
- **Data Storage**: An in-memory dictionary is used to store account balances, allowing for quick access and updates.
- **Pydantic**: The `Transaction` model is defined using Pydantic to ensure that transaction amounts are validated.

## API Endpoints

### 1. Get Root

- **Endpoint**: `GET /`
- **Description**: Returns a welcome message.
- **Response**:
  ```json
  {
    "message": "Welcome to Eyal's ATM!"
  }
  ```

### 2. Get Account Balance

- **Endpoint**: `GET /accounts/{account_id}/balance`
- **Description**: Returns the balance of a given account.
- **Parameters**:
  - `account_id`: The ID of the account (integer).
- **Response**:
  - **Success**:
    ```json
    {
      "balance": <balance>
    }
    ```
  - **Error** (if account is not found):
    ```json
    {
      "detail": "Invalid account"
    }
    ```

### 3. Deposit Money

- **Endpoint**: `POST /accounts/{account_id}/deposit`
- **Description**: Deposits money into the account.
- **Parameters**:
  - `account_id`: The ID of the account (integer).
  - **Body**: A JSON object containing the amount to deposit.
    ```json
    {
      "amount": <amount>
    }
    ```
- **Response**:
  - **Success**:
    ```json
    {
      "balance": <new_balance>
    }
    ```
  - **Error** (if amount is invalid):
    ```json
    {
      "detail": "Invalid amount, must be positive"
    }
    ```

### 4. Withdraw Money

- **Endpoint**: `POST /accounts/{account_id}/withdraw`
- **Description**: Withdraws money from the account.
- **Parameters**:
  - `account_id`: The ID of the account (integer).
  - **Body**: A JSON object containing the amount to withdraw.
    ```json
    {
      "amount": <amount>
    }
    ```
- **Response**:
  - **Success**:
    ```json
    {
      "balance": <new_balance>
    }
    ```
  - **Error** (if account is not found or insufficient funds):
    ```json
    {
      "detail": "Insufficient funds"
    }
    ```

## Challenges Faced

- **Validation**: Ensuring that amounts and account IDs are valid was a challenge, which was addressed by using FastAPI's built-in validation capabilities.
- **In-memory Database**: Since the accounts are stored in memory, all data is lost when the server restarts. This is suitable for development but not for production use.

## Conclusion

This ATM API serves as a basic implementation of banking operations and can be extended with more features like persistent storage, user authentication, and transaction history.

