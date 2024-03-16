from collections import Counter

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

counter = Counter(numbers)

for c in check:
    if counter[c]:
        print(1)
    else:
        print(0)