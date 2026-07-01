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
#
# success = []
# for x in TRANSACTIONS_DB:
#     if x["status"] == "success":
#         success.append(x["client"])
#
# print(success)

# success = [(trans["client"], trans["amount"]) for trans in TRANSACTIONS_DB if trans["status"] == "success"]
# success = {trans["client"]: trans["amount"] for trans in TRANSACTIONS_DB if trans["status"] == "success"}
#
# print(success)

big = [trans for trans in TRANSACTIONS_DB if trans["amount"] > 10000]
print(big)

# Ваш код для завдань нижче:
#
# raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
# clean_names = [name.title() for name in raw_names]
# print(clean_names)

# transactions = [1200, 15000, 450, 55000, 800]
# vip = [trans for trans in transactions if trans>10000]
# print(vip)

balances = [5000, -1000, 250, -500]
new_balances = [bal if bal>0 else bal*1.1 for bal in balances]
print(new_balances)