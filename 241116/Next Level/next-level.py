class Student:
    def __init__(self, _id, level):
        self._id   = _id
        self.level = level

a, b = input().split()
student1 = Student(a, b)
student2 = Student("codetree", "10")
print(f"user {student2._id} lv {student2.level}") 
print(f"user {student1._id} lv {student1.level}") 
