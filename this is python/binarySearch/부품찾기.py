import sys

n = int(sys.stdin.readline().rstrip())
store = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
request = list(map(int, sys.stdin.readline().rstrip().split()))

store.sort()

for i in range(m):
    target = request[i]
    start = 0
    end = len(store)

    while True:
        if start > end:
            print("no", end=" ")
            break

        mid = (start + end) // 2

        if target == store[mid]:
            print("yes", end=" ")
            break
        elif target < store[mid]:
            end = mid - 1
        elif target > store[mid]:
            start = mid + 1
