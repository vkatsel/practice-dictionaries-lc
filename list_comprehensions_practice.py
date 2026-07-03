# ==========================================
# ДАНІ ДЛЯ ОБРОБКИ (СПИСКИ РЯДКІВ)
# Використовується для Практичної №1
# ==========================================
from traceback import print_tb

SERVER_LOGS = [
    "INFO: User logged in",
    "ERROR: Connection timeout",
    "DEBUG: Query executed",
    "ERROR: Database locked",
    "WARNING: High memory usage",
    "ERROR: File not found",
    "INFO: User logged out"
]
errorlogs = [log[7:] for log in SERVER_LOGS if log.startswith("ERROR:")]
print(errorlogs)

RAW_PRICES = [
    "$10.50",
    "€20.00",
    "$15.99",
    "invalid",
    "$5.00",
    "$120.00",
    "N/A"
]
prices = [float(price[1:]) for price in RAW_PRICES if price.startswith("$")]
print(prices)
# Ваш код для завдань нижче:
#gross_salaries = [15000, 22000, 18500, 31000]
#net_salaries = [p*0.8 for p in gross_salaries]
#print(net_salaries)

#raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
#clean_names = [name.title() for name in raw_names]
#print(clean_names)

#balances = [5000, -1000, 250, -500]
#newbalances = [p * 1.1 if p<0 else p for p in balances]
#print(newbalances)

transactions = [1200, 15000, 450, 55000, 800]
vip = [p for p in transactions if p>10000]
print(vip)