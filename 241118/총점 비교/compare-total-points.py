class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
n = int(input())
arr = [list(input().split()) for _ in range(n)]
students = [Student(name, int(kor), int(eng), int(math)) for name, kor, eng, math in arr]

# 첫 번째 우선순위는 국어 점수 오름차순
# 국어 점수가 같다면 두 번째 우선순위는 영어 점수 오름차순
students.sort(key=lambda x: (x.kor + x.eng + x.math)) 

for student in students: # 정렬 이후의 결과 출력
    print(student.name,  student.kor, student.eng, student.math)