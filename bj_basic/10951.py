# 입력이 끝날 때까지 받아오는 방법
# 1. sys
# import sys
# lines = sys.stdin.readlines()
# for line in lines:
#     a, b = map(int, line.split())
# 2. EOFError
# while True:
#     try:
#         a, b = map(int, input().spilit())
#     except EOFError:
#         파일의 끝 End of File
#         break

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError:
        break