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

# numbers = [1, 2, 3, 4, 5]
# results = []
#
# for num in numbers:
#     squared = num ** 2
#     results.append(squared)
#
# results_2 = [num ** 2 for num in numbers]
# print(results)
# print(results_2)

# gross_salaries = [15000, 22000, 18500, 31000]
# net_salaries = [salary - (salary * 0.2) for salary in gross_salaries]
# print(f"Net salaries: {net_salaries}")

# raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
# clean_names = [name.title() for name in raw_names]
# print(clean_names)

# balances = [5000, -1000, 250, -500]
# balances_new = [balance + (balance * 0.1) if balance < 0 else balance
#              for balance in balances]
# print(balances_new)
#
# status_bank = "good" if sum(balances) > 3000 else "bad"
# print(f"Bank bancrucy status is {status_bank}")

# transactions = [1200, 15000, 450, 55000, 800]
# vip_transactions = [transaction for transaction in transactions if transaction > 10000]
# print(vip_transactions)

# clean_messages = [log.replace("ERROR:", "").strip()
#                   for log in SERVER_LOGS if log.startswith("ERROR:") ]
# print(clean_messages)
#
# clean_prices = [float(price.replace("$", "")) for price in RAW_PRICES if price.startswith("$")]
# print(clean_prices)

# menu = {"Latte": 60, "Americano": 40}
# print(f"Americano: {menu["Americano"]}")
#
# menu["Latte"] = 70
# menu["Flat white"] = 65
# print(f"Updated menu: {menu}")
# print(f"Cappucino: {menu.get("Cappucino", "none")}")

# product = {"name": "Laptop", "price": 1000, "stock": 15}
#
# product["stock"] -= 1
# product["price"] *= 1.1
# print(product)

user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
user_profile["phone"] = "+380991234567"
user_profile["is_premium"] = False
removed = user_profile.pop("discount")
print(user_profile)