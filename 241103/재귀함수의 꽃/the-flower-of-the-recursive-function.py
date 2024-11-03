def print_star(n):  
    if n == 0:      
        return

    print(n, end=' ')
    print_star(n - 1)
    print(n, end=' ')
print_star(int(input()))