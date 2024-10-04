Am, Ae = map(int, input().split())
Bm, Be = map(int, input().split())

if Am > Bm :
    print('A')
if Am < Bm :
    print('B')
if Am == Bm :
    if Ae > Be :
        print('A')
    if Ae < Be :
        print('B')