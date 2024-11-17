class DoW:
    def __init__(self, day, week, weather):
        self.day = day
        self.week = week
        self.weather = weather
        
        
# 변수 선언 및 입력
n = int(input())
arr = [list(input().split()) for _ in range(n)]
ary = []
for i in range(n):
    if arr[i][2] == "Rain":
        ary.append(arr[i])
people = [DoW(day, week, weather) for day, week, weather in ary]
# 사전순으로 이름이 가장 느린 사람 찾기
target_idx = 0
for i, person in enumerate(people):
    if person.day < people[target_idx].day:
        target_idx = i
# 결과 출력
print(f"{people[target_idx].day} {people[target_idx].week} {people[target_idx].weather}")