TRANSACTIONS_DB = [
    {"id": 1, "client": "Alice", "amount": 1200, "category": "Electronics", "status": "success"},
    {"id": 2, "client": "Bob", "amount": 450, "category": "Groceries", "status": "success"},
    {"id": 3, "client": "Charlie", "amount": -150, "category": "Refund", "status": "success"},
    {"id": 4, "client": "Diana", "amount": 55000, "category": "Auto", "status": "pending"},
    {"id": 5, "client": "Eve", "amount": 800, "category": "Electronics", "status": "failed"},
    {"id": 6, "client": "Frank", "amount": 200, "category": "Groceries", "status": "success"},
    {"id": 7, "client": "Grace", "amount": 15000, "category": "Electronics", "status": "success"},
    {"id": 8, "client": "Hank", "amount": -50, "category": "Refund", "status": "failed"},
]
successful_transactions = [transaction for transaction in TRANSACTIONS_DB if transaction["status"] == "success"]
print(f"Successful transactions: {successful_transactions}")
high_value = [transaction for transaction in TRANSACTIONS_DB if transaction["amount"]>10000]
print(f"High-value transactions: {high_value}")
refund_category = [transaction["amount"] for transaction in TRANSACTIONS_DB if transaction["category"] == "Refund"]
print(f"Refund: {refund_category}")
amounts = [transaction["amount"] for transaction in TRANSACTIONS_DB if transaction["status"]=="success"]
print(f"Total revenue: {sum(amounts)}")
rejected_clients = [transaction["client"] for transaction in TRANSACTIONS_DB if transaction["status"]=="failed"]
print(f"Rejected clients: {rejected_clients}")
