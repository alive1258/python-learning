def all_sum(num1, *numbers):
    total = num1

    for num in numbers:
        print(num)
        total = total + num

    return total


total = all_sum(5, 6, 7, 8, 9)

print("total all sum:", total)


