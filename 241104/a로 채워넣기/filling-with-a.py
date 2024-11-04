s = input()

s = s[:1] + 'a' + s[2:len(s)-2] + 'a' + s[len(s)-1:]
print(s)

#s = 'leebroscode'
#arr = list(s)
#arr[1], arr[len(arr)-2] = 'a', 'a'
#s = ''.join(arr)
#print(s)