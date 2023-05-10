n = int(input())
routes = list(input().split())

x = 1
y = 1

for route in routes:
    if route == 'L' and y - 1 > 0:
        y -= 1
    elif route == 'R' and y + 1 < 6:
        y += 1
    elif route == 'U' and x - 1 > 0:
        x -= 1
    elif route == 'D' and x + 1 < 6:
        x += 1

print(x, y)
