A = input()
B = input()
cnt = 0
for i in range(len(A)):
    A = A[len(A)-1] + A[:-1]
    cnt += 1
    if B == A :
        print(cnt)
        break
    if cnt == len(A):
        print('-1')