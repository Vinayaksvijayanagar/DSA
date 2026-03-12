#composition method
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
    
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 

class Queue:
    def __init__(self):
        self.element = Linkedlist()
        
    def __str__(self):
        if self.element.head is None:
            return "empty queue"
        else:
            res = ''
            curr = self.element.head
            while curr is not None:
                res += str(curr.value)
                curr = curr.next
                if curr is None:
                    break
                res += "->"
            return res
        
    def enque(self,value):
        new_node = Node(value)
        if self.element.head is None:
            self.element.head = new_node
            self.element.tail = new_node
        else:
            self.element.tail.next = new_node
            self.element.tail = new_node
            new_node.next = None
            
    def deque(self):
        if self.element.head is None:
            return None
        else:
            popped_element = self.element.head
            self.element.head = self.element.head.next
            popped_element.next = None
q = Queue()
q.enque(1)
q.enque(2)
q.enque(3)
print(q)
q.deque()
print(q)