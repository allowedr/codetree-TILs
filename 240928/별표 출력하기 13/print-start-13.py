n = int(input())
print("* "*n)
for i in range(1, n) :
    if i%2 ==0 :
        print("* " * i)
    else :
        print("* " * i)
        i += 1
for j in  range(i) :
    if i%2 !=0 :
        print("* " * i)
    else :
        print("* " * i)
        i -= 1
print("* " * n)