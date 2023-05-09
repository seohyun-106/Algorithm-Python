import sys

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
blackjack = list()
card_sum = 0

for i in range (N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            card_sum = card[i] + card[j] + card[k]
            if card_sum > M: continue
            else: blackjack.append(card_sum)
            card_sum = 0

print(max(blackjack))