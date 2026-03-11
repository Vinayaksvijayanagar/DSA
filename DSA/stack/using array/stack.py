class Element:
    def __init__(self,element):
        self.element = element
        self.length = 0
    def __str__(self):
        return str(self.element)

class Stack:
    def __init__(self):
        self.itmes = []
        self.length = 0
        
    def isempty(self):
        if self.length == 0:
            return "empty string"
s = Stack()
print(s.isempty())