N, B = map(int, input().split())
digits = []
num = 0

B = int(B)
if B == 4
    while True:
        if N < 4:
            digits.append(N)
            break

        digits.append(N % 4)
        N //= 4

    # print binary number
    for digit in digits[::-1]:
        print(digit, end="")
if B == 8 :
    while True:
        if N < 8:
            digits.append(N)
            break

        digits.append(N % 8)
        N //= 8

    # print binary number
    for digit in digits[::-1]:
        print(digit, end="")
