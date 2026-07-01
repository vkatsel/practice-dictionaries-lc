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
new_list=[i["client"] for i in TRANSACTIONS_DB if i["status"]=="success" ]
print(new_list)

new_list1=[i["client"] for i in TRANSACTIONS_DB if i["amount"]>10000 ]
print(new_list1)




raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
clean_names=[name.title() for name in raw_names]
print(clean_names)



transactions = [1200, 15000, 450, 55000, 800]
vip_transactions=[i for i in transactions if i>10000]
print(vip_transactions)



balances = [5000, -1000, 250, -500]
new_balance=[x if x>=0 else x*1.1 for x in balances]
print(new_balance)