import sys

N = int(sys.stdin.readline())

time = []
for _ in range(N):
    time.append(list(map(int, sys.stdin.readline().split())))

time.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0

for i in range(N):
    if time[i][0] >= end:
        count += 1
        end = time[i][1]

print(count)