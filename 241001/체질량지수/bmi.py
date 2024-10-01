h, w = map(int, input().split())
b = (10000*w)/(h*h)

print(f"{int(b)}")
if b >= 25 :
    print('Obesity')