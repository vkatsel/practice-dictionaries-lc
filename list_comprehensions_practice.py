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
net_salaries=[n*0.8 for n in gross_salaries]
print(net_salaries)

raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
clean_names=[name.title() for name in raw_names]
print(clean_names)

balances = [5000, -1000, 250, -500]
new_balances = [n if n>0 else n*1.1 for n in balances]
print(new_balances)

transactions = [1200, 15000, 450, 55000, 800]
vip_transactions = [n for n in transactions if n>10000]
print(vip_transactions)

errors = [n[7:] for n in SERVER_LOGS if n.startswith("ERROR:")]
print(errors)

normal_prices = [float(n[1:]) for n in RAW_PRICES if n.startswith("$")]
print(normal_prices)

