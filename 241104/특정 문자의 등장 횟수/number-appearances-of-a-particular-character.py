s = input()

eecnt = 0
ebcnt = 0

for i in range(len(s)-1):
    if 'e'== s[i] and 'e' == s[i+1] :
        eecnt += 1
    if 'e'== s[i] and 'b' == s[i+1] :
        ebcnt += 1

print(eecnt, ebcnt)