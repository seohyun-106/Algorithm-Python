n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

answer = 0
count = 0

# if numbers[0] == numbers[1]:
#     answer = numbers[0] * m
# else:
#     for i in range(0, m):
#         if count == k:
#             answer += numbers[1]
#             count = 0
#         else:
#             answer += numbers[0]
#             count += 1
#
# print(answer)

while m > 0:
    if count == k:
        answer += numbers[1]
        count = 0
    else:
        answer += numbers[0]
        count += 1
    m -= 1
print(answer)
