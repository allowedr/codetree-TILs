def call(A, B) :
    if A >= B :
        A = A+25
        B = B*2
    else :
        A = A*2
        B = B+25
    return A, B



a, b = map(int, input().split())

a, b = call(a, b)

print(a, b)