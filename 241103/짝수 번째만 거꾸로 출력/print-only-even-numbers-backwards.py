A = input()

for i in range(len(A)-1, -1, -1):
    if i % 2 != 0 :
        print(A[i],end='')