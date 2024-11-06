arr = input()
for c in arr:
    if 'a' <= c and c <= 'z' :
        print(c.upper(),end='')
    else:
        print(c.lower(),end='')