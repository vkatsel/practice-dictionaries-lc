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
# print(results)
#
# results_2 = [num ** 2 for num in numbers]
# print(results_2)
# gross_salaries = [15000, 22000, 18500, 31000]
#
# net_seleries = [seleries - (seleries * 0.2) for seleries in gross_salaries]
#
# print(net_seleries)
# raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
# clean_names = [i.title() for i in raw_names]
# print(clean_names)
# balances = [5000, -10000, 250, -500]
# new_balances = [i * 1.1 if i < 0 else i for i in balances]
# print(new_balances)
#
# status_bank = "good" if sum(balances) > 3000 else "bad"
# print(f"status_bank:{status_bank}")
# transactions = [1200, 15000, 450, 55000, 800]
# vip_transactions = [i for i in transactions if i > 10000]
# print(vip_transactions)
# SERVER_LOGS = [
#     "INFO: User logged in",
#     "ERROR: Connection timeout",
#     "DEBUG: Query executed",
#     "ERROR: Database locked",
# ]
# cleand_messages = [  log.replace("ERROR", "").strip() for log in SERVER_LOGS if log.startswith("ERROR")]
# print(cleand_messages)

New_prices =[float(i[1:]) for i in RAW_PRICES if i.startswith("$")]
print(New_prices)


