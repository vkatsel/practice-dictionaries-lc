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
net_salaries = [sal*0.8 for sal in gross_salaries]
print(net_salaries)

raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
clean_names = [name.title() for name in raw_names]
print(clean_names)

balances = [5000, -1000, 250, -500]
new_balances=[p if p>0 else p*1.1 for p in balances]
print(new_balances)

transactions = [1200, 15000, 450, 55000, 800]
vip_transactions=[p for p in transactions if p>10000]
print(vip_transactions)

errors=[p[7:] for p in SERVER_LOGS if p.startswith("ERROR")]
print(errors)

prices=[float(p[1:]) for p in RAW_PRICES if p.startswith("$")]
print(prices)