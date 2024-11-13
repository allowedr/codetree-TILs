def summary(n):
    global cnt, a
    if n <= a :
        cnt += n
        return cnt
    cnt += n
    return summary(n-2)

a = 0
cnt = 0
N = int(input())
if N % 2 == 0 :
    a = 2
else :
    a = 1
print(summary(N))