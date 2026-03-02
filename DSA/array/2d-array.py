
# #insert 
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# def insert(arr,pos,value,axis):
#     arr =  np.insert(arr,pos,value,axis = axis)
#     print(arr)
#     return arr
# insert(arr,5,[99,99],axis = 1) 
# insert(arr,2,[1,2,3,4,5],axis=0)      #axis = 0 for row add
#                                       #axis = 1 for column add
                                
                                
#transverse
# def transverse(arr):
#     for i in range(len(arr)):            #len(arr) → number of rows
#         for j in range(len(arr[0])):      #len(arr[0]) → number of columnf
#             print(arr[i][j])                             
# transverse(arr)                            #or use arr.shape


#search
# def search(arr,key):
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if arr[i][j] == key:
#                 print("found",key)
#     print("not found")
# search(arr,105)

#delete
def delete(arr,value,axis):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == value:
             arr = np.delete(arr,value,axis=axis)
             print(arr)
             return arr
delete(arr,0,axis = 0)