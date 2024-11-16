class defuse:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

code, color, sec = input().split()
defuser = defuse(code, color, sec)

print("code :", defuser.code)
print("color :", defuser.color)
print("second :", defuser.sec)