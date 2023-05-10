n = int(input())
students = []

for i in range(n):
    name, kor, eng, math = input().split()
    students.append((name, int(kor), int(eng), int(math)))

students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])
