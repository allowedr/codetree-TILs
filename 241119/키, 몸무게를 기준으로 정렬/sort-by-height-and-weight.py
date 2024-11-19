class Student:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w
n = int(input())
arr = [list(input().split()) for _ in range(n)]
students = [Student(name, int(h), int(w)) for name, h, w in arr]

students.sort(key=lambda x: (x.h, -x.w))

for student in students: # 정렬 이후의 결과 출력
    print(student.name,  student.h, student.w)
