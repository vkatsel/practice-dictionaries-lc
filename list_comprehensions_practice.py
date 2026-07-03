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
# net_salaries = [salary*0.8 for salary in gross_salaries]
# print(net_salaries)
# raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
# clean_names = [name.title() for name in raw_names]
# print(clean_names)
# balances = [5000, -1000, 250, -500]
# print([b*1.1 if b<0 else b for b in balances])
# transactions = [1200, 15000, 450, 55000, 800]
# vip_transactions = [t for t in transactions if t>10000]
# print(vip_transactions)

# Refunds = [t["amount"] for t in TRANSACTIONS_DB if t["category"]== "Refund"]
# print(Refunds)
# Total = sum([t["amount"] for t in TRANSACTIONS_DB if t["status"] == "success"])
# print(Total)
# Blacklist = [t["client"] for t in TRANSACTIONS_DB if t["status"] == "failed"]
# print(Blacklist)