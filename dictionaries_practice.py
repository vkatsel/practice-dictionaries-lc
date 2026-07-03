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
menu = {"Latte": 60, "Americano": 40}
price_am=menu["Americano"]
print(price_am)
menu["Latte"]=70
menu["Americano"]=65
print(menu)
print(menu.get("Flat White","Nope"))

product = {"name": "Laptop", "price": 1000, "stock": 15}
product["stock"] -= 1
product["price"] *= 1.1
print(product)

user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
user_profile["phone"] = "+380991234567"
user_profile["is_premium"] = False
user_profile.pop("discount")
print(user_profile)

client = {"name": "Іван", "email": "ivan@example.com"}
phone_number = client.get("phone")
print(f"Телефонуйте за номером: {phone_number}")

cart = {"items_count": 3, "total_price": 450}
cart["promo_code"] = "SALE20"

settings = {
    "theme": "dark",
    "notifications": True,
    "volume": 80
}

expenses = {"Marketing": 5000, "Rent": 2000, "Salaries": 15000}
suma=0
for i in expenses.values():
    suma+=i
print(suma)

grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
average_grade=sum(grades.values())/len(grades)
print(average_grade)

total=0
for i in grades.values():
    total+=i
print(total/len(grades))

alice_salary=EMPLOYEE_DB["tech"]["alice"]["salary"]
print(alice_salary)

total=0
count=0
for dep in EMPLOYEE_DB.values():
    for guy in dep.values():
        total+=guy["salary"]
        count+=1
averag=total/count
print("Average salary: "+str(averag))
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
