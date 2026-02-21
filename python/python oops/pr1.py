class Student:
    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    def is_pass(self):
        if self.marks >= 40:
            print("Student is pass")
        else:
            print("Student is fail")
            
if __name__ == "__main__":
    s1 = Student("Rani",101,19)
    s1.is_pass()