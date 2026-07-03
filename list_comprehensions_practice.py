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

#
# numbers = [1, 2, 3, 4, 5]
# results = []
#
# for num in numbers:
#     squared = num ** 2
#     results.append(squared)
# results2 =[num**2 for num in numbers]
# print(results2)

# gross_salaries = [15000, 22000, 18500, 31000]
# net_salaries = [ salary - (salary*0.2) for salary in gross_salaries ]
# print(net_salaries)
#
# raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
# clean_names =[name.title() for name in raw_names]
# print(clean_names)

# balances = [5000, -1000, 250, -500]
# balances_new = [balance + (balance * 0.1) if balance < 0 else balance
#                 for balance in balances]
# print(balances_new)
#
# status_bank = "good" if sum(balances_new) > 3000 else "bad"
# print(f"Bank bancrupcy status: {status_bank}")

# transactions = [1200, 15000, 450, 55000, 800]
# # vip_transactions = [trans for trans in transactions if trans >10000]
# vip_transactions = [trans * 2 if trans % 2==0 else trans/2 for trans in transactions if trans >10000]
# print(vip_transactions)

data = [10, -5, 20, -1]
clean_data = [0 if x < 0 else x for x in data]
print(clean_data)