n = int(input())
s= 0
avr = 0
for i in range(n) :
    a = int(input())
    s+= a

avr = s/n
print(f"{s} {avr:.1f}")