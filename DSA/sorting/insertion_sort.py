def insertion_sort(l):
    for i in range(1,len(l)):
        key = l[i]
        j = i-1
        while j>=0 and l[j]>key:
            l[j+1]=l[j]
            j -=1
        l[j+1] = key
    return l
            
l = [4, 2, 1, 3]
print(insertion_sort(l))    