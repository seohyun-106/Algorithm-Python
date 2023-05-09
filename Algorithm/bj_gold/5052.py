# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     phone_numbers = [str(sys.stdin.readline().strip()) for _ in range(n)]
#     phone_numbers.sort()
#
#     flag = True
#     for i in range(len(phone_numbers)-1):
#         length = len(phone_numbers[i])
#         if phone_numbers[i] == phone_numbers[i+1][:length]:
#             flag = False
#             break
#
#     if flag:
#         print('YES')
#     else:
#         print('NO')

numbers = input().rstrip()
temp = ''
answer = 0

while True:
    if numbers == temp:
        break
    length = len(temp)

    if numbers[length] == '0':
        answer += 1
        temp += numbers[length]

    elif length == len(numbers) - 1:
        answer += 2
        temp += numbers[length]

    else:
        if int(numbers[length]) + 1 == int(numbers[length+1]):
            answer += 1
            temp += numbers[length] + numbers[length+1]
        else:
            answer += 2
            temp += numbers[length]

    print(answer)

print(answer)
