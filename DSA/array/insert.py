
#insert
import numpy as np
arr = np.array([1,2,3,4,5])
# def insert(arr,pos,value):
#     arr = np.insert(arr,pos,value)
#     print(arr)
#     return arr
# pos = int(input("enter the position"))
# value = int(input("enter the value to add"))
# insert(arr,pos,value)  
#traverse
# def transverse(arr):
#     for i in range(len(arr)):
#         print(arr[i])
# transverse(arr)

#assess/search
# def search(arr,key):
#     for i in arr:
#         if i == key:
#             print("found",i)
#     print("not found")   
# search(arr,9)

#delete
def delete(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            arr = np.delete(arr,key)
            print(arr)
            return arr
    
key =int(input("enter the element to delete"))
delete(arr,key)
        
