A, B = input().split()
a = []
b = []
for c in A:
    if c.isalnum() == True and c.isalpha() != True :
        a.append(c)
    else :
        break
a = ''.join(a)        
for c in B:
    if c.isalnum() == True and c.isalpha() != True :
        b.append(c)
    else :
        break
b = ''.join(b)
print(int(a) + int(b))