A, B = input().split()
A, B = (A + ''.join(B)), (B + ''.join(A))

print(int(A)+int(B))