def printt(a):
    if a == 0 :
        return

    printt(a-1)
    print('*' * a)
    

printt(int(input()))