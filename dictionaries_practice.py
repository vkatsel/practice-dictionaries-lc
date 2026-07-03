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
# print(f"Americano: {menu["Americano"]}")
#
# menu["Latte"] = 70
# menu["Flat white"] = 65
# print(f"Updated menu: {menu}")
# print(f"Cappucino: {menu.get("Cappucino", "none")}")

# product = {"name": "Laptop", "price": 1000, "stock": 15}
#
# product["stock"] -= 1
# product["price"] *= 1.1
# print(product)

# user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
# user_profile["phone"] = "+380991234567"
# user_profile["is_premium"] = False
# removed = user_profile.pop("discount")
# print(user_profile)

# expenses = {"Marketing": 5000, "Rent": 2000, "Salaries": 15000}
#
# suma = 0
# for expence in expenses.values():
#     suma += expence
# print(f"Suma is {suma}")

# grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
#
# suma = 0
# count = 0
#
# for grade in grades.values():
#     suma += grade
#     count += 1
# print(suma/count)

# print(EMPLOYEE_DB["tech"]["alice"]["salary"])

total_salary = 0
total_employees = 0
for key, department in EMPLOYEE_DB.items():
    total_employees += len(department)

    dept_sal = 0
    for employee in department:
        total_salary += department[employee]["salary"]
        dept_sal += department[employee]["salary"]

    print(f"Average salary for {key}: {dept_sal/len(department)}")

print(f"Average salary overall: {total_salary/total_employees}")

