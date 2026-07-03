# ==========================================
# БАЗА ДАНИХ КОМПАНІЇ (СЛОВНИК)
# Використовується для Практичної №1
# ==========================================

EMPLOYEE_DB = {
    "tech": {
        "alice": {"role": "Data Scientist", "salary": 4500, "status": "active"},
        "bob": {"role": "Backend Engineer", "salary": 3800, "status": "active"},
        "charlie": {"role": "DevOps", "salary": 4000, "status": "on_leave"}
    },
    "sales": {
        "diana": {"role": "Sales Manager", "salary": 3000, "status": "active"},
        "eve": {"role": "Account Executive", "salary": 3200, "status": "active"}
    },
    "hr": {
        "frank": {"role": "HR Specialist", "salary": 2500, "status": "active"}
    }
}

# Ваш код для завдань нижче:
alice_salary = EMPLOYEE_DB["tech"]["alice"]["salary"]
print(alice_salary)

salary_total = 0
employee_count = 0
for dep in EMPLOYEE_DB.values():
    for employee in dep.values():
        salary_total += employee["salary"]
        employee_count += 1

avg = salary_total / employee_count
print(f"Average salary: {avg}")

# оновлення salary для diana
EMPLOYEE_DB["sales"]["diana"]["salary"] = 3500

# видалення charlie
EMPLOYEE_DB["tech"].pop("charlie")
print(EMPLOYEE_DB)


# ==========================================
# БАЗА ТРАНЗАКЦІЙ ТА КЛІЄНТІВ (СПИСОК СЛОВНИКІВ)
# Використовується для фінальних завдань
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

active_clients = [tr["client"] for tr in TRANSACTIONS_DB if tr["status"]=="success"]
print(f"Active clients: {active_clients}")

high_value_transactions = [tr for tr in TRANSACTIONS_DB if tr["amount"] > 10000]
print(f"High value transactions: {high_value_transactions}")

refunds = [tr["amount"] for tr in TRANSACTIONS_DB if tr["category"] == "Refund"]
print(f"Refunds: {refunds}")

pos_transactions = [tr["amount"] for tr in TRANSACTIONS_DB if tr["amount"] > 0 and tr["status"]=="success"]
total = sum(pos_transactions)
print(f"Total successful transactions: {total}")

blacklist = [tr["client"] for tr in TRANSACTIONS_DB if tr["status"] == "failed"]
print(f"Blacklist: {blacklist}")
