# ==========================================
# ДАНІ ДЛЯ ОБРОБКИ (СПИСКИ РЯДКІВ)
# Використовується для Практичної №1
# ==========================================

# SERVER_LOGS = [
#     "INFO: User logged in",
#     "ERROR: Connection timeout",
#     "DEBUG: Query executed",
#     "ERROR: Database locked",
#     "WARNING: High memory usage",
#     "ERROR: File not found",
#     "INFO: User logged out"
# ]
#
# RAW_PRICES = [
#     "$10.50",
#     "€20.00",
#     "$15.99",
#     "invalid",
#     "$5.00",
#     "$120.00",
#     "N/A"
# ]

# Ваш код для завдань нижче:


raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
clean_names = []

for name in raw_names:
    clean_names.append(name.tittle())

print(clean_names)
