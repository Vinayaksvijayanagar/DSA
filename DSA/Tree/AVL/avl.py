from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1
        
def trverse(root):
    if not root:
        return None
    else:
        custom_queue = deque()
        custom_queue.append(root)
        while custom_queue:
            root_value = custom_queue.popleft()
            print(root_value)
            if root_value.leftchild is not None:
                custom_queue.append(root.leftchild)
            if root_value.rightchild is not None:
                custom_queue.append(custom_queue.rightchild)
                
# def search(root,key):
#     if not root:
#         return None
#     else:
#         custom_queue = deque()
#         custom_queue.append(root)
#         while custom_queue:
#             root_val = custom_queue.popleft()
#             if root_val.data == key:
#                 return "got buddy"
#             if root_val.leftchild:
#                 custom_queue.append(root_val.leftchild)
#             if root_val.rightchild:
#                 custom_queue.append(root_val.rightchild)
#         return "not found"

# def search(root,key):
#     if not root:
#         return None
#     if root.data == key:
#         return "found"
    
#     else:
#         if value < root.data:
#             if root.leftchild is not None and root.leftchild.data == key:
#                 return "found"
#             else:
#                 search(root.leftchild,key)
#         else:
#             if root.rightchild is not None and root.rightchild.data == key:
#                 return "found"
#             else:
#                 search(root.rightchild,key)   
                
                
                
                
def search(root, key):
    if not root:
        return "not found"

    if root.data == key:
        return "found"

    elif key < root.data:
        return search(root.leftchild, key)

    else: #key > root.data:
        return search(root.rightchild, key)

def gethight(root):
    if not root:
        return 0
    return root.height

def balance_hight(root):
    if not root:
        return 0
    return gethight(root.leftchild) - gethight(root.rightchild)
    
def right_rotation(root):
    new_node = root.leftchild
    temp = root.leftchild.rightchild
    root.leftchild = temp
    new_node.rightchild = root
    root.height = 1 + max(gethight(root.leftchild),gethight(root.rightchild))
    new_node.height = 1 + max(gethight(new_node.leftchild),gethight(new_node.rightchild))
    return new_node
def left_rotation(root):
    new_node = root.rightchild
    temp = root.rightchild.leftchild
    root.rightchild = temp
    new_node.leftchild  = root
    root.height = 1 + max(gethight(root.leftchild),gethight(root.rightchild))
    new_node.height = 1 + max(gethight(new_node.leftchild),gethight(new_node.rightchild))
    return new_node # because after rotation new node will become root


def insert(root,node): # here node means value
    
    if not root:
        return Node(node)
    elif node < root.data:
        root.leftchild = insert(root.leftchild,node)
    else:
        root.rightchild = insert(root.rightchild,node)
        
    root.height = 1 + max(gethight(root.leftchild),gethight(root.rightchild))
    balance = balance_hight(root)
    
    if balance > 1 and node < root.leftchild.data:
        return right_rotation(root)
    if balance > 1 and node > root.leftchild.data:
        root.leftchild = left_rotation(root.leftchild)
        return right_rotation(root)
    if balance < -1 and node > root.rightchild.data:
        return left_rotation(root)
    if balance < -1 and node < root.rightchild.data:
        root.rightchild = right_rotation(root.rightchild)
        return left_rotation(root)
    return None
def getmin(node):
    current = node
    while current.left is not None:
        current = current.left
    return current 
def delete(root,key):
    if not root:
        return None
    elif key < root.data:
        root.leftchild = delete(root.leftchild,key)
    elif key > root.data:
        root.rightchild = delete(root.rightchild,key)
    else: # here key == value
        #case1 : no child /leaf
        if  root.leftchild is None:
            return root.rightchild
        elif root.rightchild is None:
            return root.leftchild
        #case 2 : two leaf nodes
        temp = getmin(root.rightchild)
        root.data = temp.data
        root.rightchild = delete(root.rightchild,temp.data)
    
    root.height = 1 + max(gethight(root.leftchild),gethight(root.rightchild))
    balance = balance_hight(root)
    if balance>1 and balance_hight(root.leftchild)>= 0 :
            return right_rotation(root)
    if balance>1 and balance_hight(root.leftchild)<0 :
            root.leftchild = left_rotation(root.leftchild)
            return right_rotation(root)
    if balance < -1 and balance_hight(root.rightchild) <= 0:
            return left_rotation(root)
    # RL
    if balance < -1 and balance_hight(root.rightchild) > 0:
             root.rightchild = right_rotation(root.rightchild)
             return left_rotation(root)

    return root