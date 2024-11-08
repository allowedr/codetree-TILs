def call(A, B) :
    if A >= B :
        A = A*2
        B = B+10
    else :
        A = A+10
        B = B*2
    return A, B



a, b = map(int, input().split())

a, b = call(a, b)

print(a, b)