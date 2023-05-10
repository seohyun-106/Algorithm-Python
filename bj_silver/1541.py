expressions = input().split('-')

result = []

for expression in expressions:
    numbers = list(map(int, expression.split('+')))
    temp = 0
    for i in numbers:
        temp += i
    result.append(temp)

answer = result[0]

for i in range(1, len(result)):
    answer -= result[i]

print(answer)
