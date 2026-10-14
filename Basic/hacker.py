n = int(input())
students = []

for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

print(students)