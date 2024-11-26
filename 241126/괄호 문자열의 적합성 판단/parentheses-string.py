#문제 4번
test = input()


left_count = 0#괄호 열기 카운트
right_count = 0#괄호 닫기 카운드
for gwalho in test:
    if gwalho == '(':
        left_count += 1
    else:
        right_count += 1
if left_count == right_count:# 괄호 열기와 닫기의 갯수가 맞다면 vps라고 판단
    print('YES')
else:
    print('No')