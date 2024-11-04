s = input()

s = s[:1] + 'a' + s[2:len(s)-2] + 'a' + s[len(s)-1:]
print(s)