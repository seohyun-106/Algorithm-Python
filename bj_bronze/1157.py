# 대문자 -> upper, capitalize
# 문자 아스키코드 ord, chr
# 길이가 정해진 list 만들
# sys -> 개행문자도 같이 읽음 !! len 쓸라면 -1 해야
# 특정 값 count
# 최댓값 구할 땐 max max max max

# import sys
#
# word = sys.stdin.readline().upper()

# def check_freq(word, cnt):
#     for i in range(0, len(word)):
#         index = ord(word[i]) - 65
#         cnt[index] += 1
#     max = 0
#     for i in cnt:
#         if i > max: max = i
#         elif i == max: max = '?'
#     if max == '?': print(max)
#     else: print(chr(cnt.index(max)+65))

# max = 0
# duplicate = False
# for i in cnt:
#     if i > max: max = i
    # elif i == max and i != 0:
    #     max = i
    #     duplicate = True

# print('?' if duplicate else chr(cnt.index(max)+65))


word = input().upper()
cnt = [0 for i in range(26)]

for i in range(0, len(word)):
    index = ord(word[i]) - 65
    cnt[index] += 1

if cnt.count(max(cnt)) > 1: print('?')
else: print(chr(cnt.index(max(cnt))+65))
