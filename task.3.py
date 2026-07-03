balances = [5000, -1000, 250, -500]
balances_new = [balance*1.1 if balance<0 else balance for balance in balances]
print(balances_new)

status_bank = "good" if sum(balances) > 3000 else "baaad"
print(f"Bank bancrupcy status: {status_bank}")
