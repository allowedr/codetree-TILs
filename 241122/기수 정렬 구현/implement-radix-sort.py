# 기수 정렬(Radix Sort) 
# : 주어진 수 들간의 비교를 하지 않고 버킷을 사용해 정렬하는  방법으로,
# 낮은 자리(1의 자리)에서 높은 자리(10^n 자리) 순으로 버킷에 넣는 방법으로 정렬한다.
# 실제로 숫자들 간의 비교를 통해 정렬을 하는 것이 아닌, 
# 0~9까지의 버킷이 있고 이 버킷에 숫자를 넣어가며 분류한다고 생각하면 된다.

from collections import deque # O(r*n) : r은 수의 자릿수

def Radix_sort(arr) :
    buckets = [deque() for _ in range(10)]

    max_value = max(arr)
    queue = deque(arr)
    digit = 1

    while max_value >= digit :
        while queue :
            num = queue.popleft()
            buckets[(num // digit) % 10].append(num)
    
        for bucket in buckets :
            while bucket :
                queue.append(bucket.popleft())
    
        
        digit *= 10

    return list(queue)
n = int(input())
lst = [*map(int, input().split())]

print(*Radix_sort(lst))