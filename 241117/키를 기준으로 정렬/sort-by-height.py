class Student:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math
n = int(input())
arr = [list(input().split()) for _ in range(n)]
students = [Student(kor, eng, math) for kor, eng, math in arr]

students.sort(key=lambda x: x.eng) # 국어 점수 기준 오름차순 정렬

for student in students: # 정렬 이후의 결과 출력
    print(student.kor, student.eng, student.math)
