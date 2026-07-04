balances = [5000, -1000, 250, -500]
calculated=[p if p>=0 else p*1.1 for p in balances]
print(*calculated)