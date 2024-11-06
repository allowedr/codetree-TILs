A = input()
B = input()
a = []
b = []
for c in A:
    if c.isalpha() != True :
        a.append(c)
for c in B :
    if c.isalpha() != True :
        b.append(c)
a = ''.join(a)
b = ''.join(b)
print(int(a)+ int(b))