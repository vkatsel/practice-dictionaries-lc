# ==========================================
# ДАНІ ДЛЯ ОБРОБКИ (СПИСКИ РЯДКІВ)
# Використовується для Практичної №1
# ==========================================

SERVER_LOGS = [
    "INFO: User logged in",
    "ERROR: Connection timeout",
    "DEBUG: Query executed",
    "ERROR: Database locked",
    "WARNING: High memory usage",
    "ERROR: File not found",
    "INFO: User logged out"
]

RAW_PRICES = [
    "$10.50",
    "€20.00",
    "$15.99",
    "invalid",
    "$5.00",
    "$120.00",
    "N/A"
]

# Ваш код для завдань нижче:
# gross_salaries = [15000, 22000, 18500, 31000]
# net_salaries =[sal*0.8 for sal in gross_salaries]
# print(net_salaries)
#
# raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
# clean_names = [name.title() for name in raw_names]
# print(*clean_names)

# balances = [5000, -1000, 250, -500]
# with_fine = [bal*1.1 if bal<0 else bal for bal in balances]
# print(*with_fine)
#
# transactions = [1200, 15000, 450, 55000, 800]
# vip_trans = [transaction for transaction in transactions if transaction > 10000]
# print(*vip_trans)
#
# error_logs = [log[7:] for log in SERVER_LOGS if log.startswith("ERROR:")]
# print(error_logs)

# clear_prices = [price.replace("$", "") for price in RAW_PRICES if price.startswith("$")]
# clear_prices = [float(price) for price in clear_prices]
# print(clear_prices)

# menu = {"Latte": 60, "Americano": 40}
# americano_price = menu["Americano"]
# print(americano_price)
# menu["Latte"] = 70
# menu["Cappucino"] = 65
# print(menu)
# print(menu.get("Flat white", "Nema"))
#
# product = {"name": "Laptop", "price": 1000, "stock": 15}
# product["stock"] -=1
# product["price"] *= 1.1
# print(product)
#
#
# user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
# user_profile["phone"] = "+380991234567"
# user_profile["is_premium"] = False
# user_profile.pop("discount")
# print(user_profile)


# expenses = {"Marketing": 5000, "Rent": 2000, "Salaries": 15000}
# suma = 0
# for key, value in expenses.items():
#     suma += value
# print(suma)
# total = sum(expenses.values())

grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
total = sum(grades.values())
average = total / len(grades)
print(average)
total = 0
for grade in grades.values():
    total += grade
average = total / len(grades)
print(average)
