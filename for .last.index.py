# to add the last index in the empty list
a=[[4,5,1],[3,2,6],[9,6,3]]
c=[]
i=0
while i<len(a):
    b=a[i][-1]
    c.append(b)
    i=i+1
print(c)