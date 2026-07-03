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
#
# # 1. Створення словника
# user = {"name": "Alice", "age": 25}
# empty_dict = {}
#
# # 2. Читання, Додавання та Оновлення
# print(user["name"])       # Alice
# user["balance"] = 100     # Додає новий ключ
# user["age"] = 26          # Оновлює існуючий ключ
#
# # 3. Безпечний доступ та Видалення
# # .get() не видає помилку, якщо ключа немає
# phone = user.get("phone", "Невідомо")
#
# # .pop() видаляє пару і повертає значення
# age = user.pop("age")
#
# # 4. Ітерація (Цикли)
# for key, value in user.items():
#     print(f"{key}: {value}")
#
# menu = {"Latte": 60, "Americano": 40}
# print(f"Americano: {menu['Americano']}")
#
# menu["Latte"] = 70
# menu["Flat White"] = 65
#
# print(f"Updated menu: {menu}")
# print(f"Cappucino: {menu.get("Cappucino", "Unknown)}")


# user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
# user_profile["phone"] = "+380991234567"
# user_profile["is_premium"] = False
# user_profile.pop("discount")
#
# print(f"Updated user profile = {user_profile}")

# expenses = {"Marketing": 5000, "Rent": 2000, "Salaries": 15000}
#
# suma = 0
# for expense in expenses.values():
#     suma += expense
#
# print(suma)

# grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
# suma = 0
# for grade in grades.values():
#     suma += grade
#
# print(f"average: {suma/len(grades)}")

# print(EMPLOYEE_DB["tech"]["alice"]["salary"][-1])
#
# total_salary = 0
# total_employees = 0
# for key, dept in EMPLOYEE_DB.items():
#     total_employees += len(dept)
#     dept_sal = 0
#
#     for employee in dept:
#         total_salary += dept[employee]["salary"]
#         dept_sal += dept[employee]["salary"]
#
#     print(f"Total salary for {key}: {dept_sal / len(dept)}")
#
# print(f"Total salary for all depts: {total_salary / total_employees}")

# EMPLOYEE_DB["sales"]["diana"]["salary"] = 3500
# EMPLOYEE_DB["tech"].pop("charlie")
# print(f"New EMPLOYEE_DB = {EMPLOYEE_DB}")

# active_clients = [transaction for transaction in TRANSACTIONS_DB
#            if transaction["status"] == "success"]
#
# print(active_clients)
#
# high_value_clients = [amount for amount in TRANSACTIONS_DB
#            if amount["amount"] > 10000]
#
# print(high_value_clients)
#
refund = [amount["amount"] for amount in TRANSACTIONS_DB
           if amount["category"] == "Refund"]

print(refund)

incomes = [transaction["amount"] for transaction in TRANSACTIONS_DB
           if transaction["status"] == "success"]
print(incomes)

rej_clients = [transaction["client"] for transaction in TRANSACTIONS_DB
           if transaction["status"] == "failed"]
print(rej_clients)