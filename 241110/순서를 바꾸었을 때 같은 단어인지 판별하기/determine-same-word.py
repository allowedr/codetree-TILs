A = input()
sorted_arr = sorted(A)
A = ''.join(sorted_arr)
B = input()
sorted_arr = sorted(B)
B = ''.join(sorted_arr)

if A == B :
    print("Yes")
else :
    print("No")