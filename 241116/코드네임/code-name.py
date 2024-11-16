class Codename:
    def __init__(self, name=0, score=0):
        self.name = name
        self.score = score

codenames = []
ary = []
for _ in range(5):
    name, score =(input().split())
    codenames.append(Codename(name, score))

for i in range(5):
    codenamess = codenames[i]
    ary.append(int(codenamess.score))
codenamess = codenames[ary.index(min(ary))]
print(codenamess.name, codenamess.score)

