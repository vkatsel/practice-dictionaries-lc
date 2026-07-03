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
# print(f"Americano: {menu['Americano']}")
# menu["Late"] = 70
# menu["Flat-white"] = 65
# print(f"Update menu: {menu}")
# print(f"Capuchino: {menu.get("Capuchino","Undefined")}")

# product = {"name": "Laptop", "price": 1000, "stock": 15}
# product["price"] *= 1.1
# product["stock"] -= 1
# print(f"Update product: {product}")

# user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
# user_profile["is_premium"] = False
# user_profile["phone"] = "+380991234567"
# user_profile.pop("discount")
# print(f"Update profile: {user_profile}")
# expenses = {"Marketing": 5000, "Rent": 2000, "Salaries": 15000}
# suma = 0
# for expense in expenses.values():
#     suma += expense
# print(f"suma: {suma}")
# grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
# average = sum(grades.values())/len(grades)
# print(f"Average grade: {average}")
# print(EMPLOYEE_DB["tech"]["alice"]["salary"])
# total_salery = 0
# total_emp = 0
# for key, department in EMPLOYEE_DB.items():
#     total_emp += len(department)
#     department_salery = 0
#     for emp in department:
#         total_salery += department[emp]["salary"]
#         department_salery += department[emp]["salary"]
#     print(f"Average salary for {key}: {department_salery/len(department)}")
# print(f"Average salery for all departments: {total_salery/total_emp}")
# TRANSACTIONS_DB = [
#     {"id": 1, "client": "Alice", "amount": 1200, "category": "Electronics", "status": "success"},
#     ...
# high_value = [t for t in TRANSACTIONS_DB if t["amount"]>10000]
# print(high_value)
# refund = [t["amount"] for t in TRANSACTIONS_DB if t["category"] = "Refund"]
# print(refund)
#
# incoms = [transaction ["amount"] for transaction in TRANSACTIONS_DB if transaction ["status"] = "success"]
# print(sum(incoms))
# experiment_json = {
#   "transactionId": "TXN-8749302-A",
#   "timestamp": "2026-07-03T12:39:00Z",
#   "type": "transfer",
#   "status": "completed",
#   "source": {
#     "accountId": "ACC-99482-S",
#     "accountHolder": "John Doe",
#     "bank": "Global Trust Bank"
#   },
#   "destination": {
#     "accountId": "ACC-11029-D",
#     "accountHolder": "Jane Smith",
#     "bank": "First National Bank"
#   },
#   "amount": {
#     "value": 1500.00,
#     "currency": "USD"
#   },
#   "metadata": {
#     "description": "Monthly rent payment",
#     "referenceCode": "RENT-JUL-2026",
#     "ipAddress": "192.168.1.15"
#   }
# }
# print(experiment_json["source"]["accountId"])

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
for transaction in experiment_json:
    suma += experiment_json["amount"]["value"]
print(suma/len(experiment_json))


