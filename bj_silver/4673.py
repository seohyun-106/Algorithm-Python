def d(n):
    n = str(n)
    sum = 0
    for i in range(0, len(n)):
        sum += int(n[i])
    n = int(n) + sum
    return n

numbers = set()
for i in range(1, 10001):
    numbers.add(i)

d_numbers = set()
for i in range(1,10001):
    d_numbers.add(d(i))

self_numbers = list(numbers - d_numbers)
self_numbers.sort()

for i in self_numbers:
    print(i)