# double_prices = [p for p in range(10) if p % 2 == 0]
# print(double_prices)
#
# numbers = [1, 2, 3, 4, 5]
# results = [num ** 2 for num in numbers]
# print(results)

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
valid = [ float(price[1:]) for price in RAW_PRICES if price[0]=="$"]
print(valid)

# gross_salaries = [15000, 22000, 18500, 31000]
# net_salaries = [ salary*(salary*0.2) for salary in gross_salaries]
# print(f"Yours salry: {net_salaries}")
#
# raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
# clean_names = [name.title() for name in raw_names]
# print(*clean_names)

# balances = [5000, -1000, 250, -500]
# bal_new = [balance-balance*0.1 if balance <0 else balance
#             for balance in balances]
# print(bal_new)
#
# bal_new_2 = "good" if sum(balances) > 6000 else "very bad 👎🏼"
# print(bal_new_2)

# transactions = [1200, 15000, 450, 55000, 800]
# vip = [trans for trans in transactions if trans > 10000]
# vipvip = [t*2 if t % 2 == 0 else t/2 for t in transactions if t > 10000]
# print(*vip)
# print(*vipvip)

SERVER_LOGS = [
    "INFO: User logged in",
    "ERROR: Connection timeout",
    "DEBUG: Query executed",
    "ERROR: Database locked",
]

# error_logs = [log.replace("ERROR:", "").strip() ]
# print(error_logs)
