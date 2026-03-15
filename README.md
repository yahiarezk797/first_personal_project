Bank Account Management Program
Overview
This program is a simple simulation of a bank account management system. It allows you to open new accounts, transfer money between accounts in the same bank, and saves all account information in individual folders. Additionally, it records every operation performed with the exact date and time, providing a clear transaction history.
Features
- Open a New Account: Create a new account with a unique ID, name, and initial balance.
- Transfer Money: Transfer funds from one account to another within the same bank.
- Data Persistence: Each account’s information (ID, name, password, balance) is saved in its own folder for easy management.
- Operation Logging: Every action (account creation, login, transfer, etc.) is stored with a timestamp, ensuring a complete record of activity.
How to Use
- Setup: Make sure you have Python installed along with the required packages (like Argon2 for password hashing).
- Creating an Account: Run the program and follow the prompts to create a new account. The program will securely hash the password and store the account details.
- Logging In: Use the log_in function to access an account by providing the account ID, name, and password.
- Transferring Funds: Once logged in, you can transfer money from one account to another.
- Viewing Logs: Check the account folder to see the log file containing all operations with their date and time.
Requirements
- Python 3.x
- argon2-cffi for password hashing
