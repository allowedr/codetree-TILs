amonth, aday, bmonth, bday = map(int, input().split())
elapsed_days = 0

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if amonth == bmonth and aday == bday:
        break

    elapsed_days += 1
    aday += 1

    if aday > num_of_days[amonth]:
        amonth += 1
        aday = 1

print(elapsed_days)
