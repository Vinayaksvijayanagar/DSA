class Element:
    def __init__(self,element):
        self.element = element
        self.length = 0
    def __str__(self):
        return str(self.element)

class Stack:
    def __init__(self):
        self.items = []
        self.length = 0
        
    def isempty(self):
        if self.length == 0:
            return "empty string"
        
    def __str__(self):
        res = []
        for x in reversed(self.items):  #or use [xtr(x) for x in reversed(self.itmes)]
            res.append(str(x))
        return "\n".join(res)
        
    def push(self,element):
        self.items.append(element)
        self.length += 1
        
    def pop(self):
        self.length -= 1
        return self.items.pop()
        
        
    def get_length(self):
        return self.length
        
    def peak(self):
        return f"the first elemnet is {self.items[-1]}"
    
s = Stack()
print(s.isempty())
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s)
s.pop()
print(s)
print(s.length)
print(s.peak())