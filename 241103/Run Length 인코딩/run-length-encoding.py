sen = input()
nsen = []
cnt = 1
lcnt = 0
if len(sen) == 1 :
    print(2)
    print(f"{sen}1")
    break
for i in range(1, len(sen)):
    if sen[i] == sen[i-1]:
        cnt += 1
    else :
        nsen.append(sen[i-1])
        nsen.append(cnt)
        lcnt += 2
        cnt = 1
    
    if i == len(sen)-1:
        nsen.append(sen[i])
        nsen.append(cnt)
        lcnt += 2

print(lcnt)        
for i in range(len(nsen)):
    print(nsen[i], end='')