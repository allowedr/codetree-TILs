#문제 4번
T = int(input())#괄호 문자열 갯수
test = [input() for i in range(T)]#테스트 리스트에 문자열 append

for test_case in test:
     left_count = 0#괄호 열기 카운트
     right_count = 0#괄호 닫기 카운드
     tmp_list = list(test_case)#테스트 케이스를 리스트로 변환
     for gwalho in tmp_list:
        if gwalho == '(':
            left_count += 1
        else:
            right_count += 1
     if left_count == right_count:# 괄호 열기와 닫기의 갯수가 맞다면 vps라고 판단
        print('YES')
     else:
        print('No')