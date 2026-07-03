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

net_salaries = [sal * 0.8 for sal in gross_salaries]
print(net_salaries)

raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
clean_names = [name.title() for name in raw_names]
print(clean_names)

balances = [5000, -1000, 250, -500]
with_fine = [balance*1.1 if balance <0 else balance for balance in balances]
print(with_fine)

transactions = [1200, 15000, 450, 55000, 800]
vip_transactions = [tr for tr in transactions if tr > 10000]
print(vip_transactions)

error_logs = [text[7:]for text in SERVER_LOGS if text.startswith("ERROR:")]
print(error_logs)

new_prices = [float(price[1:]) for price in RAW_PRICES if price.startswith("$")]
print(new_prices)