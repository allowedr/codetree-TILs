n = int(input())
arr = list(map(float, input().split()))
plus = 0
for i in range(n) :
    plus += arr[i]
print(f'{plus/n:.1f}')

if plus/n >= 4.0 :
    print('Perfect')
elif plus/n >= 3.0 :
    print('Good')
else :
    print('Poor')