A = input()
arr = ['L', 'E', 'B', 'R', 'O', 'S']
for i in range(len(arr)):
    if arr[i] == A :
        print(i)
        break
    if i == len(arr):
        print('None')