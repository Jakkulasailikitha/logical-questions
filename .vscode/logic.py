# a=[[5,-6],[-1,-2],[5,-9]]
# i=0
# m=[]
# while i<len(a):
#         j=0
#         while j<len(a[i]):
#             if a[i][j]<0:
#                 m.append(a[i][j])
#             j+=1
#         i+=1
# print(m)

# marks=[[3,4,5],[1,3,5],[5,6,7,1]]
# i=0
# while i<len(marks):
#     num=marks[i]
#     length=len(num)
#     j=0
#     a=0
#     s=0
#     while j<len(num):
#        s=s+marks[i][j]
#        a=s//length
#        j=j+1
#     i=i+1
#     print(a)

# l=[[1,2],[3,4,5],[1,4,5,6]]
# print(l[0][0])
# print(l[1][0])
# print(l[2][0])
# i=0
# a=[]
# while i<len(l):
#     j=0
#     while j<len(l[i]):
#         c=l[i][j]
#         j=j+1
#     i=i+1  
# print(c)
        
# 


password=input("enter the password")
if len(password)>=1 and len(password)<=10:
    if "@" in password or "#" in password or "$" in password:
        # if password>="A" and password<="Z" in password:
        if password>="a" and password<="z" in password:
            if password>="A" and password<="Z" in password:

                if password>="0" or password<="9" in password:
                    print("strong password")
                else:
                    print("numbers are missing")
            else:
                print("capital letter is missing")
        else:
            print("small letter is missing")
    else:
        print("special character is missing")
else:
    print("your password is long")
    
    
l=[[1,2],[2,3,4],[6,5,4,5]]
a=[]
b=len(l)
i=0
for i in range(len(l)-1):
    j=0
    for j in range(len(l)-1):
        c=l[i][j]+l[i+1][j]+l[i+2][j]
        a.append(c)
    print(a)