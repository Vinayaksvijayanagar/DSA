class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return self.value
    
class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
#append
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
            
#__STR__   
    def __str__(self):
        curr_node = self.head
        res = ''
        while curr_node is not None:
            res += str(curr_node.value)
            curr_node = curr_node.next
            if curr_node is self.head:break
            res += "<->"
        return res
#add first
    def firstadd(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:    
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        self.length += 1    
        
# add last
    def addlast(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next  = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1

#traverse
    def traverse(self):
        temp_node = self.head
        if self.head is None:
            return None
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node is self.head:
                break
        return True   
#reverse
    def reverse(self):
        curr_node = self.tail
        if self.head is None:
            return None
        while curr_node is not None:
            print(curr_node.value, end = " ")
            curr_node = curr_node.prev
            if curr_node is self.tail:
                break
        return True   
l = CDLL()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
print(l)
l.firstadd(5)
print(l)
l.addlast(6)
print(l)
l.traverse()
l.reverse()