cnt = 0
while True :
    n = int(input())
    if cnt == 3 :
        break
    if n % 2 == 0 :
        print(n/2)
        cnt +=1