def findmax(arr,n):
    if n == 1:
        return arr[0]
    return max((arr[n-1],findmax(arr,n-1)))
print(findmax([1,2,3],3))