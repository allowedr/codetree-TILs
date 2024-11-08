def alpha(A):
    check = "No"
    for i in A:
        for j in A:
            if i != j:
                check = 'Yes'
                break
    return check

c = input()
print(alpha(c))