m1, d1, m2, d2 = list(map(int, input().split()))
yo = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
def Days(m, d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sums = 0

    for i in range(1, m):
        sums += days[i]
    sums += d

    return sums
if((m1 == m2 and d1 > d2) or (m1 > m2)):
    week = 7 - (Days(m1, d1) - Days(m2, d2)) % 7
else:
    week = (Days(m2, d2) - Days(m1, d1)) % 7

print(yo[week])