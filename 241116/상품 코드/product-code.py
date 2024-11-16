class thing:
    def __init__(self, name, code):
        self.name = name
        self.code = code

name, code = input().split()
_object = []
_object = [thing("codetree", "50")]
_object.append(thing(name, code))
for i in range(2):
    codenamess = _object[i]
    print(f"product {codenamess.code} is {codenamess.name}")