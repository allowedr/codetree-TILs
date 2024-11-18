ahour, amins, bhour, bmins  = map(int, input().split())
elapsed_time = 0

while True:
    if ahour == bhour and amins == bmins:
        break

    elapsed_time += 1
    amins += 1

    if amins == 60:
        ahour += 1
        amins = 0

print(elapsed_time)
