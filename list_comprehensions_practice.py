# ==========================================
# БАЗА ТРАНЗАКЦІЙ ТА КЛІЄНТІВ (СПИСОК СЛОВНИКІВ)
# Використовується для Практичної №2
# ==========================================

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

# Ваш код для завдань нижче:
gross_salaries = [15000, 22000, 18500, 31000]
net_salaries = [salary*0.8 for salary in gross_salaries]
# Refunds = [t["amount"] for t in TRANSACTIONS_DB if t["category"]== "Refund"]
# print(Refunds)
# Total = sum([t["amount"] for t in TRANSACTIONS_DB if t["status"] == "success"])
# print(Total)
# Blacklist = [t["client"] for t in TRANSACTIONS_DB if t["status"] == "failed"]
# print(Blacklist)