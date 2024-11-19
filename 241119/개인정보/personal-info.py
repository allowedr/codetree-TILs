class Student:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w
arr = [list(input().split()) for _ in range(5)]
students = [Student(name, int(h), float(w)) for name, h, w in arr]

students.sort(key=lambda x: (x.name))

print('name')
for student in students: # 정렬 이후의 결과 출력
    print(student.name,  student.h, student.w)
print()
students.sort(key=lambda x: (-x.h)) 
print('height')
for student in students: # 정렬 이후의 결과 출력
    print(student.name,  student.h, student.w)
