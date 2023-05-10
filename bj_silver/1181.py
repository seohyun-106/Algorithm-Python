# 길이로 정렬 가능
# 정렬할 땐 상위 조건을 마지막으로

import sys

N = int(input())
word_list = list(sys.stdin.readline().strip() for _ in range(N))

word_list.sort()
word_list.sort(key=len)

for i in range(N):
    if i == N-1:
        print(word_list[i])
    else:
        if word_list[i] == word_list[i+1]:
            continue
        else:
            print(word_list[i])