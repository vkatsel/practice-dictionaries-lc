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