arr = []
n = int(input())
length = 0
cnt = 0
for _ in range(n):
    arr.append(input())
c = input()

for i in range(n):
    if arr[i][0] == c:
        length += len(arr[i])
        cnt += 1
print(f"{cnt} {length/cnt:.2f}")