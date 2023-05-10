now = input()

ap = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = ap.index(now[0])
y = int(now[1]) - 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

count = 0

for i in range(0, len(steps)):
    nx = x + steps[i][0]
    ny = y + steps[i][1]

    if 0 <= nx <= 7 and 0 <= ny <= 7:
        count += 1

print(count)
