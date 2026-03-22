# import queue_ds as queue
from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        
    def __str__(self):
        return str(self.data)
    
def preorder(root):
    if not root:
        return None
    print(root.data)
    preorder(root.leftchild)
    preorder(root.rightchild)   
    
def inorder(root):
    if not root:
        return None
    inorder(root.leftchild)
    print(root.data)
    inorder(root.rightchild)

def postorder(root):
    if not root:
        return None
    postorder(root.leftchild)
    postorder(root.rightchild)
    print(root.data)
    
#levelorder

# def levelorder(root):
#     custom_queue = queue.Queue()
#     custom_queue.enque(root)
#     while not custom_queue.isEmpty():
#         root_node = custom_queue.deque(root)
#         print(root_node.value.data)
        
#         if root.value.leftchild is not None:
#             custom_queue.enque(root.value.leftchild)
#         if root.value.rightchild is not None:
#             custom_queue.enque(root.value.rightchild)
  
# for built in functions      
def levelorder(root):
    custom_queue = deque()
    custom_queue.append(root)
    while   custom_queue:
        root_node = custom_queue.popleft()
        print(root_node.data)
        if root_node.leftchild is not None:
            custom_queue.append(root_node.leftchild)
        if root_node.rightchild is not None:
            custom_queue.append(root_node.rightchild)  
            
def search(root,value):
    custom_queue = deque()
    custom_queue.append(root)
    while custom_queue:
        root_node = custom_queue.popleft()
        if root_node.data == value :
            return "present sir"
        if root_node.leftchild is not None:
            custom_queue.append(root_node.leftchild)
        if root_node.rightchild is not None:
            custom_queue.append(root_node.rightchild)
            
def  insert(root,value):
    new_node = Node(value)
    custom_queue = deque()
    custom_queue.append(root)
    while custom_queue:
        root = custom_queue.popleft()
        if root.leftchild is not None:
            custom_queue.append(root.leftchild)
        else:
            root.leftchild = new_node
            return "insert succesfully"
            
        if root.rightchild is not None:
            custom_queue.append(root.rightchild)
        else:
            root.rightchild = new_node
            return "insert succesfully"
def getdeep(root):
    if not root:
        return None
    else:
        custom_queue = deque()
        custom_queue.append(root)
        while custom_queue: #LOOP imp step dont use while custom_queue isnot none
            root = custom_queue.popleft()
            if root.leftchild is not None:
                custom_queue.append(root.leftchild)
            if root.rightchild is not None:
                custom_queue.append(root.rightchild)
        return root
def  deldeep(root,dnode):
    if not root :
        return None
    else:
        custom_queue = deque()
        custom_queue.append(root)
        while custom_queue:
            root = custom_queue.popleft()
            if root == dnode:
                    root = None
            if root.leftchild is not None:
                if root.leftchild == dnode:
                     root.leftchild = None
                     return root
                else:   
                    custom_queue.append(root.leftchild)
            if root.rightchild is not None:
                if root.rightchild == dnode:
                     root.rightchild = None
                     return root
                else:  
                    custom_queue.append(root.rightchild)
        return root
        
def delete(root,value):
    if not root:
        return None
    else:
        custom_queue = deque()
        custom_queue.append(root)
        while custom_queue :
            node = custom_queue.popleft()
            if node.data == value:
                dnode = getdeep(root)
                node.data= dnode.data
                deldeep(root,dnode)
                return "deleted bro"
            if node.leftchild is not None:
                custom_queue.append(node.leftchild)
            if node.rightchild is not None:
                custom_queue.append(node.rightchild)
                
            
                
    
                        


new_t = Node("Drinks")
new_t.leftchild = Node("Hot")
new_t.rightchild = Node("cold")
# print(new_t.leftchild)
# preorder(new_t)
# inorder(new_t)
# postorder(new_t)
# levelorder(new_t)
# print(search(new_t,"D"))
# insert(new_t,"coffe")
# insert(new_t,"tea")
# levelorder(new_t)
# print(new_t.leftchild.rightchild)
dnode= getdeep(new_t)
# deldeep(new_t,dnode)
delete(new_t,"Hot")
levelorder(new_t)

