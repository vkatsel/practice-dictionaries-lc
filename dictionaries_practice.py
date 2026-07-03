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

# menu = {"Latte": 60, "Americano": 40}
# print(menu["Americano"])
# menu["Latte"] = 70
# menu["Cappucino"] = 65
# print(f"Updated menu: {menu}")
# print(f"Flat White: {menu.get("Flat White", "Undefined")}")

# product = {"name": "Laptop", "price": 1000, "stock": 15}
# product["price"] = 1100
# product["stock"] = 14
# print(f"Updated product: {product}")

# user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
# user_profile["phone"] = +380991234567
# user_profile["is premium"] = False
# removed = user_profile.pop("discount")
# print(user_profile)
# print(removed)
#
# expenses = {"Marketing": 5000, "Rent": 2000, "Salaries": 15000}
# suma = 0
# for expense in expenses.values():
#     suma += expense
#
# print(f"Suma: {suma}")
# print(sum(list(expenses.values())))

# grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
# print(sum(list(grades.values())) / len(list(grades.values())))
# suma = 0
# lst = []
# for grade in grades.values():
#     suma += grade
#     lst.append(grade)
#
# print(suma / len(lst))

# print(EMPLOYEE_DB["tech"]["alice"]["salary"])

# total_salary = 0
# total_employees = 0
# for key, department in EMPLOYEE_DB.values():
#     total_employees += len(department)
#     department_sal = 0
#
#     for employee in department:
#         total_salary += department[employee]["salary"]
#         department_sal += department[employee]["salary"]
#
#     print(f"Average salary for {key}: {department / department_sal}")
#
# print(total_salary / total_employees)
#
# EMPLOYEE_DB["sales"]["diana"]["salary"] = 3500
# EMPLOYEE_DB["tech"].pop("charlie")
# print(f"Updated DB: {EMPLOYEE_DB}")

# active_clients = [transaction for transaction in TRANSACTIONS_DB if transaction["status"] == "success"]
# print(active_clients)

# high_value = [transaction for transaction in TRANSACTIONS_DB if transaction["amount"] > 10000]
# print(high_value)

refund = [transaction for transaction in TRANSACTIONS_DB if transaction["category"] == "Refund"]
print(refund)

