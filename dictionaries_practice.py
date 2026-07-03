# ==========================================
# БАЗА ДАНИХ КОМПАНІЇ (СЛОВНИК)
# Використовується для Практичної №1
# ==========================================

# for department, employee in EMPLOYEE_DB.
# ==========================================
# БАЗА ТРАНЗАКЦІЙ ТА КЛІЄНТІВ (СПИСОК СЛОВНИКІВ)
# Використовується для фінальних завдань
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
# alice = EMPLOYEE_DB["tech"]["alice"]["salary"]
# print(f"Alice salary is: {alice}")
#
# total_salary = 0
# total_employees = 0
# for key, depar in EMPLOYEE_DB.items():
#     total_employees += len(depar)
#     depar_sal = 0
#
#     for employee in depar:
#         total_salary += depar[employee]["salary"]
#         depar_sal += depar[employee]["salary"]
#
#     print(f"Salary for {key}: {depar_sal / len(depar)}")
#
# print(f"Total salary for al departs: {total_salary / total_employees}")
#
#
#
# # ```````````````============Live Coding 3: Company Mini-DB=============```````````````
# EMPLOYEE_DB["sales"]["diana"]["salary"] = 3500
# fired = EMPLOYEE_DB["tech"].pop("charlie")
# print(EMPLOYEE_DB)


# ```````````````============  Capstone: Analytical dashboard  =============```````````````
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

success_clients = [t["client"] for t in TRANSACTIONS_DB
                   if t["status"] == "success"]
print(success_clients)

high_value_t = [t for t in TRANSACTIONS_DB if t["amount"] >= 10000]
print(high_value_t)

refund = [t["amount"] for t in TRANSACTIONS_DB if t["category"] == "Refund"]
print(refund)
# menu = {"Latte": 60, "Americano": 40}
# print(f"Americano: {menu["Americano"]}")
#
# menu["Late"] = 70
# menu["Flat-white"] = 70
#
# print(f"Update dict: {menu}")
# print(f"Cappuccino: {menu.get("Cappuccino")}")

# ```````````````============FIRST GUIDED PRACTICE=============```````````````

# user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
#
# user_profile['phone'] = "+380991234567"
# user_profile["is_premium"] = False
#
# removed = user_profile.pop("discount")
# print(f"Updated profile is: {user_profile}", removed)

# expenses = {"Marketing": 5000, "Rent": 2000, "Salaries": 15000}
# print(sum(list(expenses.values())))
#
# suma = 0
# for expense in expenses.values():
#     suma += expense
# print(f"The sum is: {suma}")
#
# # ```````````````============Guided Practice: Аналіз оцінок=============```````````````
#
# grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
# total = 0
# # print(sum(list(grades.values())))
# for grade in grades.values():
#     total += grade
#
# average = total/len(grades)
# print(average)
#





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

print(experiment_json[0]["source"]["accountId"])
print(experiment_json[1]["amount"]["currency"])

suma = 0
for t in experiment_json:
    suma = t["amount"]["value"]

print(suma / len(experiment_json))