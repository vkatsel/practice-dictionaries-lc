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

# numbers = [i ** 2 for i in range (1,6)]
# print(numbers)

# gross_salaries = [15000, 22000, 18500, 31000]
# net_salaries = [salary - (salary * 0.2) for salary in gross_salaries]
# print(net_salaries)

# raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
# clean_names = [names.title() for names in raw_names]
# print(clean_names)

# balances = [5000, -1000, 250, -500]
# new_balance = [balances + (balances * 0.1) if balances < 0 else balances
#                for balances in balances]
# print(new_balance)
#
# status_bank = "good" if sum(balances) > 3000 else "bad"
# print(f"bank: {status_bank}")

# transactions = [1200, 15000, 450, 55000, 800]
# vip_transactions = [transactions * 2 if transactions % 2 == 0 else transactions / 2
#                     for transactions in transactions if transactions > 10000]
# print(vip_transactions)

# data = [10, -5, 20, -1]
# clean_data = [0 if x < 0 else x for x in data]
# print(clean_data)
#
# # cleaned_massages = [log.replace("ERROR:"," ").strip()for log in SERVER_LOGS if log.startswith("ERROR")]
# # print(cleaned_massages)
#
# prices = [float(price[1:]) for price in RAW_PRICES if price.startswith("$")]
# print(prices)
#
# menu = {"Latte": 60, "Americano": 40}
# print(f"Latte {menu["Latte"]}")
#
# menu["Americano"] = 70
# menu["Flat white"] = 65
# print(f"updated dict: {menu}")
# print(f"Cappucino: {menu.get('Cappucino', "unknown")}")
