n = int(input())
su = 0
ss = []
cnt = 0
for i in range(n) :
    ss.append(list(map(int, input().split())))
    for  j in range(4):
        su += ss[i][j]
    if su // 4 >= 60 :
        print('pass') 
        cnt += 1
    else :
        print('fail')
    su = 0
print(cnt)