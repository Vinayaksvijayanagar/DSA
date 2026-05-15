def bubblesort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

l = [2,1,3,4]
print(bubblesort(l))
