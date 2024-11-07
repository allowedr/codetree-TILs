n = int(input())
odd = 0
even = 0
for i in range(n-1):
    c = int(input())
    if c == 0 :
        break
    elif c%2 != 0 :
        even += 1
    else :
        odd += 1
print(odd)
print(even)