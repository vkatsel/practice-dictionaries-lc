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

numbers = [1, 2, 3, 4, 5]
results = []

for num in numbers:
    squared = num ** 2
    results.append(squared)

print(results)
result_2 = [num**2 for num in numbers]
print(result_2)

gross_salaries = [15000, 22000, 18500, 31000]
net_salaries = [salary - (salary*0.2) for salaries in gross_salaries]
print(f"Net salaries: {net_salaries}")

raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
clean_names = [name.title() for name in raw_names]
print(clean_names)