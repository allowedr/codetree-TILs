arr = input()
for c in arr:
    if c.isalpha() == True:
        print(c.lower(),end='')
    else :
        print(c, end='')