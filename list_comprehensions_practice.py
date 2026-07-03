# # ==========================================
# # ДАНІ ДЛЯ ОБРОБКИ (СПИСКИ РЯДКІВ)
# # Використовується для Практичної №1
# # ==========================================
#
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
# # ]
# #
# # # Ваш код для завдань нижче:
# #
# numbers = [1, 2, 3, 4, 5]
# results = []
#
# for num in numbers:
#     squared = num ** 2
#     results.append(squared)
#
# result2 = [num ** 2 for num in numbers]
# print(results)
#
#
# gross_salaries = [15000, 22000, 18500, 31000]
# net_salaries = [salary - salary* 0.2 for salary in gross_salaries]
# print( net_salaries )
#
# raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
# clean_names = [names.title() for names in raw_names]
# print(clean_names)
#
# balances = [5000, -1000, 250, -500]
# balanses_new = [b + (b * 0.1) if b < 0 else b
#     for b in balances]
# print(balanses_new)
# status = 'good' if sum(balances) > 3000 else 'bad'
# print(f'nnn {status}')
#
# transactions = [1200, 15000, 450, 55000, 800]
# s = [i for i in transactions if i > 1000]
# print(s)
#
# SERVER_LOGS = [
#     "INFO: User logged in",
#     "ERROR: Connection timeout",
#     "DEBUG: Query executed",
#     "ERROR: Database locked",
# ]
# cl_m = [log.replace('ERROR','').strip() for log in SERVER_LOGS if log.startswith('ERROR')]
# print(cl_m)

# RAW_PRICES = [
#     "$10.50",
#     "€20.00",
#     "$15.99",
#     "invalid",
#     "$5.00",
#     "$120.00",
#     "N/A"]
# pr = [log.replace('$','') for log in RAW_PRICES if log.startswith('$')]
# print(pr)