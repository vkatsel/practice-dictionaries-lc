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

# menu = {"Latte" : 60, "Americano": 40}
# print(f"Americano: {menu['Americano']}")
# menu["Latte"] = 70


# user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
# user_profile["phone"]="+380991234567"
# user_profile["is_premium"]=False
# user_profile.pop("discount")
# print(user_profile)


# expenses = {"Marketing": 5000, "Rent": 2000, "Salaries": 15000}
# suma = 0
# for i in expenses.values():
#     suma+=i
# print(sum(expenses.values()))


# grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
# # print(sum(grades.values())/len(grades.values()))
#
# suma = 0
# for grade in grades:
#     suma+=grades[grade]


# print(EMPLOYEE_DB["tech"])
# print(EMPLOYEE_DB["tech"]["alice"]["salary"])
#
#
# suma = 0
# length = 0
# salaries=[]
# for department in EMPLOYEE_DB:
#     suma = 0
#     length = 0
#     for name in EMPLOYEE_DB[department]:
#         suma+=EMPLOYEE_DB[department][name]["salary"]
#         length+=1
#     avg = suma/length
#     print(f"{department} department's average salary: {suma/length}")

#
# EMPLOYEE_DB["sales"]["diana"]["salary"] = 3500
# EMPLOYEE_DB["tech"].pop("charlie")
# print(EMPLOYEE_DB)

# active = [t["client"] for t in TRANSACTIONS_DB if t["status"]=="success"]
# print(active)
# high_value = [t for t in TRANSACTIONS_DB if t["amount"]>=10000]
# print(high_value)
# refund = [t["amount"] for t in TRANSACTIONS_DB if t["category"]=="Refund"]
# print(refund)
# total_rev = sum([t["amount"] for t in TRANSACTIONS_DB if t["amount"]>0 and t["status"]=="success"])
# print(total_rev)
# blacklis = [t["client"] for t in TRANSACTIONS_DB if t["status"]=="failed"]
# print(blacklis)

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
    suma +=transaction["amount"]["value"]
avg = suma/len(experiment_json)
print(avg)