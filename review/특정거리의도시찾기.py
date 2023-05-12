n, m, k, x = map(int, input().split())
distance = [1000000] * (n+1)
roads = list(list(map(int, input().split())) for _ in range(m))
distance[x] = 0

for road in roads:
    start = road[0]
    end = road[1]

    distance[end] = min(distance[start] + 1, distance[end])

check = False

for i in range(len(distance)):
    if distance[i] == k:
        check = True
        print(i)

if not check:
    print(-1)