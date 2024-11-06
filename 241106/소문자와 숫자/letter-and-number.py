arr = input()
for c in arr:
    if c.isalpha() == True:
        print(c.lower(),end='')
    elif c.isalnum() == True :
        print(c, end='')