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
gross_salaries = [15000, 22000, 18500, 31000]

net_salaries=[sal*0.8 for sal in gross_salaries]
print(net_salaries)

raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
clean_names=[name.title() for name in raw_names]
print(clean_names)

balances = [5000, -1000, 250, -500]
with_fine = [bal*1.1 if bal<0 else bal for bal in balances]
print(with_fine)

transactions = [1200, 15000, 450, 55000, 800]
vip_trans=[trans for trans in transactions if trans >10000]
print("VIP transactions", *vip_trans)

numbers = [1, 2, 3]
doubled = [x*2 for x in numbers]

amounts = [50, 120, 30]
high_amounts = [a for a in amounts if a > 100]
print(high_amounts)

data = [10, -5, 20, -1]
clean_data = [0 if x < 0 else x for x in data]

error_logs=[log[7:] for log in SERVER_LOGS if log.startswith("ERROR:")]
print(error_logs)

valid_prices=[float(price[1:]) for price in RAW_PRICES if price.startswith("$")]
print(valid_prices)