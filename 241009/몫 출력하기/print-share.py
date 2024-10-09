cnt = 0
while True :
    a = int(input());
    if cnt == 3 :
        break
    if a % 2 == 0 :
        print(int(a/2))
        cnt +=1