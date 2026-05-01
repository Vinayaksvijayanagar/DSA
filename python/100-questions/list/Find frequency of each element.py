#Find frequency of each element

l = list(map(int,input().split()))
d = {}

# for i in range(len(l)):
#     if l[i] not in d:
#         d[l[i]] = 1
#     else:
#         d[l[i]] += 1
# print(d)

for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

