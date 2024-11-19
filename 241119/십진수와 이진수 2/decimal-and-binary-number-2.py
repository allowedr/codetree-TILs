binary = input()
num = 0
digits = []

for i in range(len(binary)):
    num = num * 2 + int(binary[i])

N= num * 17


while True:
    if N < 2:
        digits.append(N)
        break

    digits.append(N % 2)
    N //= 2

# print binary number
for digit in digits[::-1]:
    print(digit, end="")
