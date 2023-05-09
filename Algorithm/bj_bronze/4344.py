# n = int(input())
# scores = []
# # averages = []
# ratio = []
#
# for i in range(n):
#     scores.append(list((map(int, input().split()))))
#     student = scores[i][0]
#     sum = 0
#     cnt = 0
#     for j in range(len(scores[i])):
#         if j == 0:
#             continue
#         else:
#             sum += scores[i][j]
#     averages.append(sum/student)
#     for j in (scores[i][1:]):
#         if j > averages[i]: cnt += 1
#     ratio.append(cnt/student*100)
#
# for i in ratio:
#     print("%0.3f%%" %i)

# for i in range(n):
#     scores.append(list((map(int, input().split()))))
#     student = scores[i][0]
#     cnt = 0
#     average = sum(scores[i][1:])/scores[i][0]
#     for j in (scores[i][1:]):
#         if j > average: cnt += 1
#     ratio.append(cnt/student*100)
#
# for i in ratio:
#     print("%0.3f%%" %i)

## 반복적으로 입력 받을 땐 input 대신 sys 사용하기 -> 런타임에러 !!

import sys
n = int(sys.stdin.readline())
for _ in range(n):
    scores = list(map(int, sys.stdin.readline().split()))
    student = scores[0]
    cnt = 0
    average = sum(scores[1:])/student
    for i in scores[1:]:
        if i > average: cnt += 1
    ratio = cnt/student*100
    print("{:.3f}%".format(ratio))