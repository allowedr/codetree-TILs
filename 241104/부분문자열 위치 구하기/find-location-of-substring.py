s = input()
target = input()

for i in range(len(s)):
    if s[i:i + len(target)] == target :
        print(i)
        break