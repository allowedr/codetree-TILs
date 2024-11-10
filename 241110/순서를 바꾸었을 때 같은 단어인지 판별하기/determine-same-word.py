A = input()
sorted_arr = sorted(A)
A = ''.join(sorted_arr)
print(A)
B = input()
sorted_arr = sorted(B)
B = ''.join(sorted_arr)
print(B)

if A == B :
    print("Yes")
else :
    print("No")