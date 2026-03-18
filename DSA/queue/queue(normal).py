class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return(str(self.value))
   
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
            if self.head is None:
                return "empty"
            else:
                 curr = self.head
                 res = ""
                 while curr is not None:
                     res += str(curr.value)
                     curr = curr.next
                     if curr is None:
                         break
                     res += "->"
                 return res
                     
                    
    
        
    def enque(self,value):
        new_val = Node(value)
        if self.head is None:
            self.head = new_val
            self.tail = new_val
        else:
            self.tail.next = new_val
            self.tail = new_val
        self.length += 1
        
    def deque(self):
        if self.head is None:
            return "empty"
        pop_ele = self.head   

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            pop_ele.next = None

        self.length -= 1
        return pop_ele.value
       

q = Queue()
q.enque(1)
q.enque(2)
q.enque(3)
print(q)
q.deque()
print(q)
a