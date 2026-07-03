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
#
# # Ваш код для завдань нижче:
# 1.
alice_salary = EMPLOYEE_DB["tech"]["alice"]["salary"]
# print(f"Зарплата Аліси: {alice_salary}")
#
#
# # 2.
# total_salary = 0
# employee_count = 0
#
# for department in EMPLOYEE_DB.values():
#     for employee in department.values():
#         total_salary += employee["salary"]
#         employee_count += 1
#
# average_salary = total_salary / employee_count
# print(f"Середня зарплата: {average_salary}")

EMPLOYEE_DB["sales"]["diana"]["salary"] = 3500
EMPLOYEE_DB["tech"].pop("charlie")

print(EMPLOYEE_DB)


#
# # ==========================================
# # БАЗА ТРАНЗАКЦІЙ ТА КЛІЄНТІВ (СПИСОК СЛОВНИКІВ)
# # Використовується для фінальних завдань
# # ==========================================
#
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
# 1.
active_clients = [t["client"] for t in TRANSACTIONS_DB if t["status"] == "success"]
print(active_clients)


# 2.
high_value = [t for t in TRANSACTIONS_DB if t["amount"] > 10000]
print(high_value)


# 3.
refunds = [t["amount"] for t in TRANSACTIONS_DB if t["category"] == "Refund"]
print(refunds)


# 4.
successful_amounts = [
    t["amount"] for t in TRANSACTIONS_DB
    if t["status"] == "success" and t["amount"] > 0
]
total_revenue = sum(successful_amounts)
print(total_revenue)


# 5.
blacklist = [t["client"] for t in TRANSACTIONS_DB if t["status"] == "failed"]
print(blacklist)



# gross_salaries = [15000, 22000, 18500, 31000]
# net_salaries = [i * 0.8 for i in gross_salaries]
# print(*net_salaries)



# raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
# clean_names = [name.title() for name in raw_names]
# print(clean_names)


# balances = [5000, -1000, 250, -500]
# new_balances = [i * 1.1 if i < 0 else i for i in balances]
# print(new_balances)

#
# transactions = [1200, 15000, 450, 55000, 800]
# vip_trancations = [ i for i in transactions if i > 10000]
# print(vip_trancations)

# menu = {"Latte": 60, "Americano": 40}
# print(f"Americano: {menu['Americano']}")
#
# menu["Latte"] = 70
# menu["Flat White"] = 65


# product = {"name": "Laptop", "price": 1000, "stock": 15}
#
# product["stock"] -= 1
# product["price"] *= 1.1
#
# print(product)


# user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 20}
# user_profile["phone"] = "+380991234567"
# user_profile["is_premium"] = False
# user_profile.pop("discount")
# print(user_profile)



# expenses = {"Marketing": 5000, "Rent": 2000, "Salaries": 15000}
# print(total = sum(expenses.values()))
# average = sum(grades.values()) / len(grades)


