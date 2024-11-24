# #문제 1 MAX-HEAPIFY 알고리즘 구현, HEAP정렬 구현
def max_heapify(A, i,heap_size):  #노드 i를 루트로 하는 서브트리를 heapify한다.

    largest = i
    if i*2+1 < heap_size and i*2+1 < len(A) and A[i*2+1] > A[largest]:
        largest = i*2+1
    if i*2+2 < heap_size and i*2+2 < len(A) and A[i*2+2] > A[largest]:
        largest = i*2+2

    if largest != i: # 루트가 가장 크지 않으면
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest,heap_size)

def heapsort(A) :
    heap_size = len(A)
    for i in range(heap_size//2-1, -1, -1):
        max_heapify(A,i,heap_size)
    for i in range(heap_size -1, 0, -1) :
        heap_size = heap_size-1
        A[0], A[i]= A[i], A[0]
        max_heapify(A,0,heap_size)

n = int(input())
A = list(map(int, input().split()))
max_heapify(A, 0, len(A))

heapsort(A)
print(*A)