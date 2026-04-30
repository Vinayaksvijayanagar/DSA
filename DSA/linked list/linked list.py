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
            self.head = new_node # use  arrow trick like here self.head -> new_node
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
            self.first(value)  # use self for inclass calling function
            return True
        elif pos == self.length:
            self.last(value)
            return True
        else:
            temp_node = self.head
            new_node = Node(value)
            for _ in range(pos-1): #go to previous node of insertion position
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
    
    def transverse(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
            
    def gets(self,index):
        if index < 0 or index >= self.length:
            return None
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node.value

    def sets(self,index,value):
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        temp_node.value = value
        
    def frstpop(self):
        if self.head is None:
            return None
        temp_node = self.head
        self.head = self.head.next
        temp_node.next = None
        
    def lastpop(self):
        temp_node = self.head
        while temp_node.next is not self.tail:
            temp_node = temp_node.next
        removed = self.tail
        self.tail = temp_node
        temp_node.next = None
        return removed 
    def remove(self,index):
        prev_node = self.head
        for _ in range(index-1):
            prev_node = prev_node.next
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
             
            
               
l = LL()

l.first(10)
l.first(5)

l.last(20)
l.last(30)

l.insert(15,2)

print(l)

l.transverse()

print(l.gets(2))