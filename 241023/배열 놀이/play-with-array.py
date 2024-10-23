n, p = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
cnt_arr = []
for i in range(n):
    question = list(map(int, input().split()))
    if len(question) == 3 :
        print(question, end=' ')
        for i in range(question[1]-1, question[2]):
            print(arr[i], end=' ')
        print()
    elif question[0] == 1 :
        print(arr[question[1]-1])
    else :
        for j in range(len(arr)):
            if arr[j] == question[1] :
                cnt += 1
                cnt_arr.append(arr.index(question[1])+1)
        if cnt == 0 :
            print('0')
        elif cnt == 1 :
            print(cnt_arr[0])
            cnt == 0
        else :
            print(cnt_arr[0])
            cnt == 0