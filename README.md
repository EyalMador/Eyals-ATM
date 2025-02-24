ATM API
Overview
The ATM API is a simple FastAPI application designed to handle basic banking operations such as checking account balances, depositing, and withdrawing funds. It utilizes an in-memory database to store account information, providing a quick and easy way to manage multiple accounts without the complexity of persistent storage.

Features
Check Balance: Retrieve the balance for any existing account.
Deposit Funds: Add funds to an account. If the account does not exist, it will be created with the deposited amount.
Withdraw Funds: Withdraw funds from an account, ensuring sufficient balance is available.
Technology Stack
FastAPI: A modern web framework for building APIs with Python 3.6+ based on standard Python type hints.
Pydantic: Data validation and settings management using Python type annotations.
Design Decisions
In-Memory Database: The application uses a Python dictionary to store account information. This design choice simplifies development and allows for quick testing. However, it is important to note that this data will be lost when the server restarts.

API Structure: The API has three main endpoints:

GET /: A welcome message.
GET /accounts/{account_id}/balance: Retrieves the balance for the specified account.
POST /accounts/{account_id}/deposit: Accepts a JSON object containing an amount to deposit into the specified account.
POST /accounts/{account_id}/withdraw: Accepts a JSON object containing an amount to withdraw from the specified account.
Pydantic Models: A Pydantic model (Transaction) is used for validating incoming JSON requests for deposit and withdrawal operations. This ensures that the amount is of the correct type and within the expected range.

API Endpoints
1. Welcome Endpoint
URL: /
Method: GET
Description: Returns a welcome message.
2. Get Balance
URL: /accounts/{account_id}/balance
Method: GET
Description: Returns the balance of the specified account.
Parameters:
account_id: The ID of the account (integer).
Response:
200 OK with balance information.
400 Bad Request if the account does not exist.
3. Deposit Funds
URL: /accounts/{account_id}/deposit
Method: POST
Description: Deposits funds into the specified account.
Parameters:
account_id: The ID of the account (integer).
Body: A JSON object with the following structure:
json
Copy
Edit
{
  "amount": float
}
Response:
200 OK with updated balance information.
400 Bad Request if the amount is negative or if the account ID is invalid.
4. Withdraw Funds
URL: /accounts/{account_id}/withdraw
Method: POST
Description: Withdraws funds from the specified account.
Parameters:
account_id: The ID of the account (integer).
Body: A JSON object with the following structure:
json
Copy
Edit
{
  "amount": float
}
Response:
200 OK with updated balance information.
400 Bad Request if the amount is negative, if the account ID is invalid, or if there are insufficient funds.
Challenges Faced
Data Persistence: Since the application uses an in-memory database, all account data is lost when the server is restarted. Future versions could implement persistent storage (e.g., a database) to solve this issue.

Validation: Ensuring proper validation of inputs was crucial, especially for withdrawal operations where insufficient funds could lead to errors. Using Pydantic helped streamline this process.

Concurrency: The current implementation does not handle concurrent access to accounts. In a production environment, care should be taken to manage concurrent modifications safely.

How to Run the Server
Clone the repository:

bash
Copy
Edit
git clone <repository-url>
cd <repository-directory>
Install the required packages:

bash
Copy
Edit
pip install fastapi[all]
Run the application:

bash
Copy
Edit
uvicorn main:app --reload
Access the API documentation at http://127.0.0.1:8000/docs.

Conclusion
The ATM API provides a foundational understanding of building APIs with FastAPI and demonstrates key principles of web development, including RESTful design, data validation, and in-memory storage. Future enhancements could include improved data persistence and concurrency management to support real-world banking scenarios.
