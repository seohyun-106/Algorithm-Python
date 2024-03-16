from collections import Counter

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

counter = Counter(cards)
answer = []
for c in check:
    answer.append(counter[c])

print(*answer)
