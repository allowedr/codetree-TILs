def mini(*args):
    return(min(*args))

a, b, c = map(int, input().split())

print(mini(a, b, c))