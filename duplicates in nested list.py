a={"list1":[2,4,5,2,],"list2":[5,6,1,2],"list3":[1,4,3,5,2]}
b=[]
for i in a:
    if a[i][0] not in b:
        b.append(a[i][0])
    if a[i][1] not in b:
        b.append(a[i][1])
    if a[i][2] not in b:
        b.append(a[i][2])
print(b)