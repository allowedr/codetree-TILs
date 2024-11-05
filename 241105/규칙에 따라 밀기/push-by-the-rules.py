A = input()
Command = list(input())
for i in range(len(Command)):
    if Command[i] == 'R':
        A = A[-1] + A[:-1]
    if Command[i] == 'L':
        A = A[1:] + A[0]
print(A)