user_input = input()

count = 0
start = 0
result = []

for i in range(len(user_input)):
    if user_input[i] == "L":
        count += 1
        
    else:
        count -= 1


    if count == 0:
        result.append(user_input[start:i + 1])
        start = i + 1


print(len(result))


for string in result:
    print(string)


