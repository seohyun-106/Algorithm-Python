import sys

def find(x, parents):
    if parents[x] != x:
        parents[x] = find(parents[x], parents)
    return parents[x]

def union(a, b, parents):
    a = find(a, parents)
    b = find(b, parents)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

V, E = map(int, sys.stdin.readline().split())

edges = []
for _ in range(E):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))
edges.sort()

parents = [0] * (V+1)
for i in range(1, V+1):
    parents[i] = i

result = 0

for cost, a, b in edges:
    if find(a, parents) != find(b, parents):
        union(a, b, parents)
        result += cost

print(result)

# import sys
# import heapq
#
# V, E = map(int, sys.stdin.readline().split())
# visited = [False for _ in range(V+1)]
# graph = [[] for _ in range(V+1)]
#
# for _ in range(E):
#     a, b, c = map(int, sys.stdin.readline().split())
#     graph[a].append([b, c])
#     graph[b].append([a, c])
#
# result, count = 0, 0
# h = [(0, 1)]
#
# while h:
#     if count == V:
#         break
#
#     cost, now = heapq.heappop(h)
#
#     if not visited[now]:
#         visited[now] = True
#         result += cost
#         count += 1
#
#         for b, c in graph[now]:
#             if not visited[b]:
#                 heapq.heappush(h, (c, b))
#
# print(result)