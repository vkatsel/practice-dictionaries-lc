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


# raw_names = ["aLice", "BOB", "charlie", "dIAnA"]
# clean_names = []
#
# for name in raw_names:
#     clean_names.append(name.title())
#
# print(clean_names)



# balances = [5000, -1000, 250, -500]
#
# new_balances = [balance * 1.1 if balance < 0 else balance for balance in balances]
#
# print(new_balances)
#
# status_bank  ="good" if sum(balances) > 3000 else "bad"
# print(f"Bank bancruty status: {status_bank}")


# transactions = [1200, 15000, 450, 55000, 800]
# # vip_transactions = [transaction for transaction in transactions if transaction > 10000]
#
# print(vip_transactions)


# SERVER_LOGS = [
#     "INFO: User logged in",
#     "ERROR: Connection timeout",
#     "DEBUG: Query executed",
#     "ERROR: Database locked",
# ]
# clean_messages = [log for log in SERVER_LOGS if log.startswith ("ERROR")]
# print(clean_messages)


# RAW_PRICES = ["$10.5", "hello", "$15.99", "text", "$5.0"]
# prices = [float(price.replace("$", "")) for price in RAW_PRICES if price.startswith("$")]
# print(prices)
