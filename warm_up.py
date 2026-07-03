numbers = [1, 2, 3, 4, 5]
results = []

for num in numbers:
    squared = num ** 2
    results.append(squared)

result_2 = [num ** 2 for num in numbers]
print(result_2)