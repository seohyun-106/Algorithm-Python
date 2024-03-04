import heapq
import sys
N = int(sys.stdin.readline())
h = []
answer = []
for _ in range(N):
    i = int(sys.stdin.readline())
    if i:
        heapq.heappush(h, (abs(i), i))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)
