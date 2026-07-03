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
#1
gross_salaries = [15000, 22000, 18500, 31000]
new_salaries = [sal*0.8 for sal in gross_salaries]
print (new_salaries)

#2
raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
new_nanes = [name.title() for name in raw_names]
print (new_nanes)

#3
balances = [5000, -1000, 250, -500]
new_balances = [bal * 1.1 if bal <0 else bal for bal in balances ]
print (new_balances)

#4
transactions = [1200, 15000, 450, 55000, 800]
vip_transactions = [bal for bal in transactions if bal > 10000 ]
print ("Vip_transactions: ", *vip_transactions)












