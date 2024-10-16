n = int(input())
cnt = 1
plus = n+1

for i in range(n-1, -1, -1):      #열을 완료하면 다시 실행됨
    for j in range(n):      #열을 수행함
            if j % 2 == 0:
                print(n-i, end='')
            else :
                print(i+1, end='')
    print()