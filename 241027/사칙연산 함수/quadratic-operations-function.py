def cal(a,o,c):
    if o == '+':
        return (f"{a} {o} {c} = {a+c}")
    elif o == '-':
        return (f"{a} {o} {c} = {a-c}")
    elif o == '/':
        return (f"{a} {o} {c} = {int(a/c)}")
    elif o == '*':
        return (f"{a} {o} {c} = {a*c}")
    else :
        return ("False")



a, o, c = input().split()
a = int(a)
c = int(c)
print(cal(a,o,c))