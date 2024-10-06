a, b = map(int,input().split())
c = a/b
c +=0.0000000000000000005
print("%.21f" % c)