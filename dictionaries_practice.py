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
# print (f"Americano: {menu["Americano"]}")
#
# menu["Latte"] = 70
# menu["Americano"] = 65
#
# print(f"Update dict: {menu}")
# print(f"Capuchino : {menu.get( "Capuchino", "Undefined")}")


# product = {"name": "Laptop", "price": 1000, "stock": 15}
# product["price"]*= 1.1
# product["stock"] -= 1
#
# print(f"Updated product: {product}")



# expenses = {"Marketing": 5000, "Rent": 2000, "Salaries": 15000}
# print(sum(expenses.values()))

# grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
# print(sum(grades.values()) / len(grades))


# print(EMPLOYEE_DB["tech"]["alice"]["salary"][-1])
# total_salary = 0
# total_employees = 0
# for dept in EMPLOYEE_DB.values():
#     total_employees += len(dept)
#     dept_salary = 0
#
#
#     for employee in dept:
#         total_salary += dept[employee]["salary"]
#         dept_salary += dept[employee]["salary"]
#
#     print(f"Average salary for {dept}: {dept_salary/len(dept)}")
#
# print(f"Average salary for all depts: {total_salary/total_employees}")



# EMPLOYEE_DB["sales"]["diana"]["salary"] = 3500
# EMPLOYEE_DB["tech"].pop("charlie")
#
# print(EMPLOYEE_DB)



# active_clients = [transaction for transaction in TRANSACTIONS_DB if transaction["status"] == "success"]
# print(active_clients)
#
# high_value_transactions = [transaction for transaction in TRANSACTIONS_DB if transaction["amount"] >= 10000]
# print(high_value_transactions)
#
# refunds = [transaction["amount"] for transaction in TRANSACTIONS_DB if transaction["category"] == "Refund"]
# print(refunds)
#
# total_revenue = sum([transaction["amount"] for transaction in TRANSACTIONS_DB if transaction["status"] == "success" and transaction["amount"] > 0])
# print(total_revenue)
#
# blacklist = [transaction["client"] for transaction in TRANSACTIONS_DB if transaction["status"] == "failed"]
# print(blacklist)


