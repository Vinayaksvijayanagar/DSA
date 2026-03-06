class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def first(self,value):
        new_node = Node(value)
        
        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
          
    def last(self,value):
        new_node=Node(value)
        if self.head is None:
                self.head = new_node
                self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
          
    def insert(self,value,pos):
        if self.length < 0  or pos > self.length:
            return False
        elif pos == 0:
            self.first(value)
            return True
        elif pos == self.length:
            self.last(value)
            return True
        else:
            temp_node = self.head
            new_node = Node(value)
            for _ in range(pos-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

            self.length += 1
            return True
    
    def __str__(self):
        temp = self.head
        res = ""
        while temp is not None:
            res += str(temp.value)
            if temp.next is not None:
                res += "->"
            temp = temp.next
        return res   
l = LL()

l.first(10)
l.last(20)
l.last(30)

print(l)