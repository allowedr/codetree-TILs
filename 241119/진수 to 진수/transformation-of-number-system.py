a, b = map(int, input().split())
n = input()
num = 0
digits = []

for i in range(len(n)):
    num = num * a + int(n[i])

N = num    
while True:
    if N < b:
        digits.append(N)
        break

    digits.append(N % b)
    N //= b

# print binary number
for digit in digits[::-1]:
    print(digit, end="")