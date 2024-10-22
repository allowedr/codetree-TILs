A = input()
arr = ['L', 'E', 'B', 'R', 'O', 'S']
idx = -1
for i in range(len(arr)):
    if arr[i] == A :
        idx = i
        break
if idx == -1 :
    print('None')
else :
    print(idx)