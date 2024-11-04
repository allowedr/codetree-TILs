s = input()
target = input()

exists = False
for i in range(len(s)):
    if s[i:i + len(target)] == target :
        exists = True
        print(i)
        break     

if exists == False :
    print('-1')