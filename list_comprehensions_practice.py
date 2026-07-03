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
# results = [num**2 for num in numbers]
# print(results)

# gross_salaries = [15000, 22000, 18500, 31000]
# net_salaries=[salary-(salary*0.2) for salary in gross_salaries]
# print(f"Net salaries: {net_salaries}")

# raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
# clean_names=[name.title() for name in raw_names]
# print(clean_names)

# balances = [5000, -1000, 250, -500]
# balances_new=[balances*1.1 if balances<0 else balances
#                 for balances in balances]
# print(balances_new)
#
# status_bank="good" if sum (balances)>3000 else "baaaaaaad"
# print(f"Bank bancrupcy status: {status_bank}")

# transactions = [1200, 15000, 450, 55000, 800]
# vip_transactions=[transaction*2 if transaction%2==0 else transaction/2
#                 for transaction in transactions if transaction>10000]
# print(vip_transactions)

# data=[10, -5, 20, -1]
# clean_data=[0 if x<0 else x for x in data]
# print(clean_data)

# cleane_messages = [log.replace("ERROR:", " ").strip() for log in SERVER_LOGS if log.startswith("ERROR")]
# print(cleane_messages)

clean_prices=[float(price[1:]) for price in RAW_PRICES if price.startswith("$")]
print(clean_prices)