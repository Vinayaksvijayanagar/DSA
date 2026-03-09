class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class Cll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    #print
    def __str__(self):
        temp_node = self.head
        res = ""
        while temp_node is not None:
            res += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node is self.head:
                break
            res += "->"
        return res
    
    #append adding last
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    #prepend adding in the begining
    def prepend(self ,value):
        new_node= Node(value)
        if self.length == 0 :
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
        self.length += 1
        
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp_node = self.head
        for _ in range(index-1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1
        
    #Traversal
    def traversal(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node is self.head:
                break
        
    #search
    def search(self,target):
        temp_node = self.head
        while temp_node is not None:
            if temp_node.value == target:
                print("it is there",target)
                return True
            temp_node = temp_node.next
            if temp_node is self.head:
                break
                
        return False
            
    #get
    def get(self,index):
        if index  < -1 or index >= self.length:
            return None
        elif index == -1:
            return self.tail
        else:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            return temp_node
    
    #set
    def set(self,index,value):
        temp_node = self.get(index)
        if temp_node is not None:
            temp_node.value = value            
    #remove  first
    def frst(self):
        curr_node = self.head
        self.head = self.head.next
        self.tail.next = self.head
        curr_node = None
        self.length -= 1
        
    #pop last
    def pop(self):
        curr_node = self.tail
        temp_node = self.head
        while temp_node.next is not self.tail:
            temp_node = temp_node.next
            
        temp_node.next = self.head
        self.tail = temp_node
        self.length -= 1
            
    # remove 
    def remove (self,index):
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
    
    
    
l = Cll()
l.append(1)
l.append(12)
l.append(56)
l.append(77)
print(l.head.value)
print(l.tail.value)
print(l.head.next)
print(l)
l.prepend(3)
print(l)
l.insert(1,55)
print(l)
l.traversal()
l.search(55)
print(l.get(-1))
l.set(1,77)
print(l)
l.frst()
print(l)
l.pop()
print(l)
l.remove(2)
print(l)