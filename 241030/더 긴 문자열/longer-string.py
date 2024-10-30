st1=input()
st2=input()

if len(st1) > len(st2):
    print(st1, len(st1))
elif len(st1) < len(st2):
    print(st2, len(st2))
else :
    print('same')