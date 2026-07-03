# ==========================================
# БАЗА ДАНИХ КОМПАНІЇ (СЛОВНИК)
# Використовується для Практичної №1
# ==========================================

EMPLOYEE_DB = {
    "tech": {
        "alice": {"role": "Data Scientist", "salary": [4500, 5000], "status": "active"},
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
# #
# product = {"name": "Laptop", "price": 1000, "stock": 15}
# product["price"] *= 1
# print["stock"] -= 1
# print(f"Updated product: {product}")



# user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
# user_profile["phone"] = "+380991234567"
# user_profile["is_premium"] = False
# removed = user_profile.pop("discount")
# print(f"Updated profile: {user_profile}")
#
# expenses = {"Marketing": 5000, "Rent": 2000, "Salaries": 15000}
#
# print(sum(expenses.values()))
#
# suma = 0
# for expense in expenses.values():
#     suma += expense
# print(f"Sum: {suma}")

# grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
# suma = 0
#
# for g in grades.values():
#     suma += g
#
# average = suma / len(grades)
# print(average)

#
# print(EMPLOYEE_DB["tech"]["alice"]["salary"][-1])

# total_salary = 0
# total_employees = 0
# for key, dept in EMPLOYEE_DB.items():
#     total_employees += len(dept)
#
#     dept_sal = 0
#     for employee in dept:
#         total_salary += dept[employee]["salary"]
#         dept_sal += dept[employee]["salary"]
#     print(f"Average salary for {key}: {dept_sal/len(dept)}")
# print(f"Average salary for all debts: {total_salary / total_employees}")

# EMPLOYEE_DB["tech"].pop("charlie")
# EMPLOYEE_DB["sales"]["diana"]["salary"] = 3500
#
# print(EMPLOYEE_DB)
#
# active_clients = [transaction for transaction in TRANSACTIONS_DB
#                   if transaction["status"]="success"]
#
# print(active_clients)
#
# new_list = [trans for trans in TRANSACTIONS_DB if trans["amount"] >= 10000]
# print(new_list)
#
#
# refunds = [t['amount'] for t in TRANSACTIONS_DB if t["category"] = ["Refund"]]
# print(refunds)
#
# incomes = [transaction["amount"] for transaction in TRANSACTIONS_DB if transaction["status"] = "success"]
# print(sum(incomes))
#
# rej_clients = [transaction['client'] for transaction in TRANSACTIONS_DB if transaction["status"] = "failed"]
# print(*rej_clients)
experiment_json = [{
  "transactionId": "TXN-8749302-A",
  "timestamp": "2026-07-03T12:39:00Z",
  "type": "transfer",
  "status": "completed",
  "source": {
    "accountId": "ACC-99482-S",
    "accountHolder": "John Doe",
    "bank": "Global Trust Bank"
  },
  "destination": {
    "accountId": "ACC-11029-D",
    "accountHolder": "Jane Smith",
    "bank": "First National Bank"
  },
  "amount": {
    "value": 1000.00,
    "currency": "USD"
  },
  "metadata": {
    "description": "Monthly rent payment",
    "referenceCode": "RENT-JUL-2026",
    "ipAddress": "192.168.1.15"
  }
},
    {
        "transactionId": "TXN-8749302-A",
        "timestamp": "2026-07-03T12:39:00Z",
        "type": "transfer",
        "status": "completed",
        "source": {
            "accountId": "ACC-99482-S",
            "accountHolder": "John Doe",
            "bank": "Global Trust Bank"
        },
        "destination": {
            "accountId": "ACC-11029-D",
            "accountHolder": "Jane Smith",
            "bank": "First National Bank"
        },
        "amount": {
            "value": 2000.00,
            "currency": "USD"
        },
        "metadata": {
            "description": "Monthly rent payment",
            "referenceCode": "RENT-JUL-2026",
            "ipAddress": "192.168.1.15"
        }
    }
,
    {
        "transactionId": "TXN-8749302-A",
        "timestamp": "2026-07-03T12:39:00Z",
        "type": "transfer",
        "status": "completed",
        "source": {
            "accountId": "ACC-99482-S",
            "accountHolder": "John Doe",
            "bank": "Global Trust Bank"
        },
        "destination": {
            "accountId": "ACC-11029-D",
            "accountHolder": "Jane Smith",
            "bank": "First National Bank"
        },
        "amount": {
            "value": 1500.00,
            "currency": "USD"
        },
        "metadata": {
            "description": "Monthly rent payment",
            "referenceCode": "RENT-JUL-2026",
            "ipAddress": "192.168.1.15"
        }
    }
]



suma = 0
for t in experiment_json:
    suma += t["amount"]["value"]
print(suma/len(experiment_json))
