a, b, c = map(int, input().split(' '))

s = a+b+c
avr = int(s/3)
ans = int(s-avr)

print(s)
print(avr)
print(ans)