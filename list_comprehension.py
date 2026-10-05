numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = []

for num in numbers:
    if num % 2 == 1 and num % 3 == 0:
       odds.append(num)

print(odds)
odds_numbers = [num for num in numbers if num % 2 == 1 and num % 3 == 0]
print(odds_numbers)