# ==========================================
# БАЗА ДАНИХ КОМПАНІЇ (СЛОВНИК)
# Використовується для Практичної №1
# ==========================================


# Ваш код для завдань нижче:

# ==========================================
# БАЗА ТРАНЗАКЦІЙ ТА КЛІЄНТІВ (СПИСОК СЛОВНИКІВ)
# Використовується для фінальних завдань
# ==========================================



# menu = {"Latte": 60, "Americano": 40}
# print(menu["Americano"])
# menu["Latte"] = 70
# menu["Flat-white"] = 65
# print(menu)

# product = {"name": "Laptop", "price": 1000, "stock": 15}
# product["price"] *= 1.5
# product["stock"] -= 1
# print(product)

# user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
# user_profile["phone"] = "+380991234567"
# user_profile["is_premium"] = False
# user_profile.pop("discount")
# print(user_profile)

# expenses = {"Marketing": 5000, "Rent": 2000, "Salaries": 15000}
# sum =0
# for expense in expenses.values():
#     sum += expense
# print(sum)

# grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
# grades_sum = sum(grades.values())
# amount_of_students = len(grades.keys())
# average_grade = grades_sum / amount_of_students
# print(average_grade)

# EMPLOYEE_DB = {
#     "tech": {
#         "alice": {"role": "Data Scientist", "salary": 4500, "status": "active"},
#         "bob": {"role": "Backend Engineer", "salary": 3800, "status": "active"},
#         "charlie": {"role": "DevOps", "salary": 4000, "status": "on_leave"}
#     },
#     "sales": {
#         "diana": {"role": "Sales Manager", "salary": 3000, "status": "active"},
#         "eve": {"role": "Account Executive", "salary": 3200, "status": "active"}
#     },
#     "hr": {
#         "frank": {"role": "HR Specialist", "salary": 2500, "status": "active"}
#     }
# }

# print(EMPLOYEE_DB["tech"]["alice"]["salary"])
# total_salary = 0
# total_employees = 0
# for department in EMPLOYEE_DB.values():
#     total_employees += len(department)
#     for employee in department:
#         total_salary += department[employee]["salary"]
#
# print(total_salary/total_employees)

# EMPLOYEE_DB["sales"]["diana"]["salary"] = 3500
# remove = EMPLOYEE_DB["tech"].pop("charlie")
# print(EMPLOYEE_DB)

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
active_clients = [transaction for transaction in TRANSACTIONS_DB if transaction["status"] == "success"]
high_value_transactions = [transaction for transaction in TRANSACTIONS_DB if transaction["amount"] >10000]
refund = [transaction["amount"] for transaction in TRANSACTIONS_DB if transaction["category"] == "Refund"]
revenue = [transaction["amount"] for transaction in TRANSACTIONS_DB if transaction["status"] == "success"]
total_revenue = sum(revenue)
