s = 0
avr=0
cnt=0
for _ in range(10) :
    a = int(input())
    if a>=0 and a<=200 :
        s+=a
        cnt+=1
avr = s/cnt
print(f"{s} {avr:.1f}")