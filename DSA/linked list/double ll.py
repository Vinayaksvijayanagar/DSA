class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.value)
#double linked list creation
class Dll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
#node append
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = None
        self.length += 1
#str tp display
    def __str__(self):
        temp_node = self.head
        res = ''
        while temp_node is not None:
            res += str(temp_node.value)
            if temp_node.next is not None:
                res += '<->'
            temp_node = temp_node.next
        return res
#prepend
    def prepend (self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1 
           
#last add
    def postpend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = None
        self.length += 1   
              
#insert
    def insert(self,pos,value):
        if pos>self.length and pos < 0 :
            return None
        elif pos == 0 :
            return self.prepend(value)
        elif pos == self.length:
            return self.postpend(value)
        else:
            new_node = Node(value)
            temp_node = self.head
            for _ in range(pos -1): 
                temp_node = temp_node.next
            new_node.next = temp_node.next
            new_node.prev = temp_node
            temp_node.next.prev = new_node
            temp_node.next = new_node
        self.length += 1        
#traverse
    def tranverse(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
               
#reverse
    def reverse(self):
        temp_node = self.tail
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.prev
#search
    def search(self,target):
        index = 0 
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == target:
                print("element is present",index)
                return True
            curr_node = curr_node.next
            index += 1
        return False
#get
    def get(self,index):
        if index < -1 or  index > self.length:
            return None
        elif index == 0:
            return self.head
        elif index == -1 :
            return self.tail
        else:   
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
        return temp_node
        
#set
    def set(self,index,value):
        current_node = self.get(index)
        current_node.value = value
#pop first element
    def frstpop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            curr_node = self.head
            self.head = self.head.next
            self.head.prev = None
            curr_node.next = None       
            self.length -= 1    
#pop last element
    def lastpop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            curr_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            curr_node.prev = None 
        self.length -= 1   
#remove
    def remove(self,index):
        current_node = self.get(index)
        current_node.next.prev = current_node.prev
        current_node.prev.next= current_node.next
        current_node.next  = None
        current_node.prev = None   
              
l = Dll()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
print(l)
l.prepend(6)
print(l)
l.postpend(7)
print(l)
l.insert(0,8)
print(l)
l.tranverse()
l.reverse()
l.search(4)
print(l.get(-1))
l.set(0,99)
print(l)
l.frstpop()
print(l)
l.lastpop()
print(l)
l.remove(2)
print(l)