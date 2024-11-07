n = int(input())
odd = 0
even = 0
for i in range(1,n-1):
    c = int(input())
    if c == 0 :
        odd += 1
        break
    elif c%2 == 0 :
        even += 1
    else :
        odd += 1
print(odd)
print(even)