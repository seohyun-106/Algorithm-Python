n = int(input())
student = []

for _ in range(n):
    name, score = input().split()
    student.append((name, int(score)))

student.sort(key=lambda student: student[1])
# array = sorted(student, key=lambda student: student[1])

for i in student:
    print(i[0], end=" ")
