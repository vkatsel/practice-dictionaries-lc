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
active_clients = [transaction for transaction in TRANSACTIONS_DB if transaction["status"] == "success"]
high_value_transactions = [transaction for transaction in TRANSACTIONS_DB if transaction["amount"] >10000]
refund = [transaction["amount"] for transaction in TRANSACTIONS_DB if transaction["category"] == "Refund"]
revenue = [transaction["amount"] for transaction in TRANSACTIONS_DB if transaction["status"] == "success"]
total_revenue = sum(revenue)
blacklist = [ transaction["client"] for transaction in TRANSACTIONS_DB if transaction["status"] == "failed"]
print(blacklist)