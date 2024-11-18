class Student:
    def __init__(self, kor, eng, num):
        self.kor = kor
        self.eng = eng
        self.num = num
n = int(input())
arr = [list(input().split()) for _ in range(n)]
students = [Student(int(kor), int(eng), int(num)) for kor, eng, num in arr]
students.sort(key=lambda x: -x.kor, -x.eng, -x.num) # 국어 점수 기준 내림차순 정렬

# 정렬 이후 등수별 학생 번호 출력
for student in enumerate(students):
    print(f"{student.kor} {student.eng} {student.num}")
