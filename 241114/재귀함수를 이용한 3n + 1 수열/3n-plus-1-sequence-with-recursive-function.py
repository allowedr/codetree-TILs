def aa(n):
    global cnt
    if n == 1 :
        return cnt

    cnt += 1
    return aa(int(n/2)) if n%2==0 else aa(int(n*3+1))



n = int(input())
cnt = 0
print(aa(n))