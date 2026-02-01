bfpg = 190
max_priority = 40
transaction_fee = 21_000
price_cost = ((bfpg + max_priority) * transaction_fee)
eth_cost = price_cost * (10 ** -9)
print(f"{price_cost} gwei, or {eth_cost} eth")