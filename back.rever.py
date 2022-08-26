# l=[1,2,3,4,5,6]
# a=[]
# i=0
# j=-1
# while i<len(l)/2:
#     a.append(l[j])
#     a.append(l[i])
#     i=i+1
#     j=j-1
# print(a)

a=[1,2,3,4]
# i=0
# while i<len(a)-1:
#     if a[0]>a[1]:
#         t=a[i]
#         a[i]=a[i+1]
#         a[i+1]=t
#     if a[3]>a[2]:
#         j=a[i]
#         a[i]=a[i+1]
#         a[i+1]=j
#     i=i+1
# print(a)
i=0
while i<len(a)-1:
    j=0
    while j<len(a)-1:
        if a[j+1]>a[i]:
            c=a[j+1],a[i]
            j=j+1
        i=i+1
    print(c)
    