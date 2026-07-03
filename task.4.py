transactions = [1200, 15000, 450, 55000, 800]
vip_clients = [transaction for transaction in transactions if transaction>10000]
print(vip_clients)
