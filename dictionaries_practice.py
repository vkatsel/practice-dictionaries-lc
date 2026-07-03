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
# print(EMPLOYEE_DB["tech"]["alice"]["salary"])
# total_salary = 0
# total_emp = 0
# for department in EMPLOYEE_DB.values():
#     total_emp += len(department)
#     for employee in department:
#         total_salary += department[employee]["salary"]
#
#
# print(total_salary/total_emp)

EMPLOYEE_DB ["tech"]["alice"]["salary"] = 3500
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
