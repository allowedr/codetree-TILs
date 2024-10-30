st1, st2 =input().split()


if len(st1) > len(st2):
    print(st1, len(st1))
elif len(st1) < len(st2):
    print(st2, len(st2))
else :
    print('same')