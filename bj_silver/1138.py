n = int(input())
info = list(map(int, input().split()))

answer = [0 for _ in range(n)]

# for i in range(1, n + 1):
#     index = info[i-1]
#
#     while True:
#         if answer[index] == 0:
#             answer[index] = i
#             break
#         else:
#             index += 1
#
# print(answer)

for i in range(n):
    print("i: ", i)
    now_info = info[i]
    # for j in range(0, ):
    #     if answer[j] == 0:
    #         count += 1
    count = 0
    while count < now_info:
        j = 0
        if answer[j] == 0:
            print("공백 ")
            count += 1
        j += 1
        print(count)

    answer[count] = i

print(answer)