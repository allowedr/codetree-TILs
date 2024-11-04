s = input()

exists = False

for i in range(len(s)-1):
    if 'e' == s[i] and 'e' == s[i+1] :
        exists = True
if exists == True :
    print('Yes', end=' ')
else :
    print('No', end=' ')

exists = False
for i in range(len(s)-1):
    if 'a' == s[i] and 'b' == s[i+1] :
        exists = True
if exists == True :
    print('Yes', end=' ')
else :
    print('No', end=' ')