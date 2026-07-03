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

# №1
gross_salaries = [15000, 22000, 18500, 31000]
net_salaries = [sal*0.8 for sal in gross_salaries]
print(net_salaries)

# №2
raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
clear_names = [name.title() for name in raw_names]
print(clear_names)

# №3
balances = [5000, -1000, 250, -500]
new_balance = [balance*1.1  if balance<0 else balance for balance in balances]
print(new_balance)

# №4
transactions = [1200, 15000, 450, 55000, 800]
vip_transactions = [trans for trans in transactions if trans>10000]
print(f"Vip transactions: ", end="")
print(*vip_transactions)

# №5
SERVER_LOGS = [
    "INFO: User logged in",
    "ERROR: Connection timeout",
    "DEBUG: Query executed",
    "ERROR: Database locked",
    "WARNING: High memory usage",
    "ERROR: File not found",
    "INFO: User logged out"
]
no_error = [text[7:] for text in SERVER_LOGS if text.startswith("ERROR")]
print(no_error)

# №6
RAW_PRICES = [
    "$10.50",
    "€20.00",
    "$15.99",
    "invalid",
    "$5.00",
    "$120.00",
    "N/A"
]
valid_prices = [float(price[1:]) for price in RAW_PRICES if price.startswith("$") or price.startswith("€")]
print(valid_prices)