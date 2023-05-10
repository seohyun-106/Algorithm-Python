# 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

# 변수 여러개의 입력 -> split
# 변수 여러개 형변환 -> map

a, b = map(int, input().split())
print(a/b)