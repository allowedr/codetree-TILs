amonth, aday, ahour, amins, bmonth= 11, 11, 11, 11, 11
bday, bhour, bmins  = map(int, input().split())
elapsed_time = 0

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if bday < 11 :
        print('-1')
        break
    if bday <= 11 and bhour < 11 :
        print('-1')
        break
    if bday <= 11 and bhour <= 11 and bmins < 11 :
        print('-1')
        break
    if amonth == bmonth and aday == bday and ahour == bhour and amins == bmins:
        break
    elapsed_time += 1
    amins += 1
    if aday > num_of_days[amonth]:
        amonth += 1
        aday = 1

    if ahour == 24:
        aday += 1
        ahour = 0

    if amins == 60:
        ahour += 1
        amins = 0
if elapsed_time >= 0 and amins == bmins:
    print(elapsed_time)

