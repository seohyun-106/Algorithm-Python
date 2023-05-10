n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(k):
    a_min = min(a)
    b_max = max(b)

    if a_min > b_max:
        break

    a[a.index(a_min)], b[b.index(b_max)] = b_max, a_min

print(sum(a))