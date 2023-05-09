n, m = map(int, input().split())
cards = list(map(int, input().split()) for _ in range(n))

min_arr = []
for i in range(0, n):
    min_arr.append(min(cards[i]))

print(max(min_arr))
