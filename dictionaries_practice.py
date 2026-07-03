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

# №1
menu = {"Latte": 60, "Americano": 40}
menu["Latte"]=70
menu["Cappuccino"]= 65
print(menu)
print(menu.get("Raff", "We have no raff"))

# №1
product = {"name": "Laptop", "price": 1000, "stock": 15}
product["stock"] -= 1
product["price"] *= 1.1
print(product)

# №2
user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
user_profile["phone"]="+380991234567"
user_profile["is_premium"] = False
user_profile.pop("discount")
print(user_profile)

# №3
expenses = {"Marketing": 5000, "Rent": 2000, "Salaries": 15000}
total = 0
for key, value in expenses.items():
    total += value
print(f"Total expenses: {total}")

# №4
grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
count = 0
total = 0
for grade in grades.values():
    count += 1
    total += grade
average_grade = total / count
print(f"Average grade is {average_grade}")

# №5
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
print("Зарплата Аліси становить", EMPLOYEE_DB["tech"]["alice"]["salary"])
total = 0
count = 0
for key, value in EMPLOYEE_DB.items():
    for key, value in value.items():
        count += 1
        total += value["salary"]
print("Розрахована середня зарплата становить", total/count)

# №6
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
EMPLOYEE_DB["sales"]["diana"]["salary"]=3500
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
