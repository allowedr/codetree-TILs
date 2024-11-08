def palindrome(A):
    A = A[::-1]
    return A

arr = input()

if arr == palindrome(arr) :
    print('Yes')
else :
    print('No')