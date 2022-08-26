# first way
# a=float(input("enter the number"))
# if a>0:
#     print("positive")
# else:
#     print("negative")
    
# a=input("enter the number")
# if a>"0":
#     print("positive")
# else:
#     print("negative")


# a=input("enter the number")
# b=int(a)
# if b>0:
#     print("positive")
# else:
#     print("negative")


time=float(input("enter the timings in the campus scheldule timings:"))
if time>6.00 and time<=7.00 :
    print(time,"students can do the exercise" )
elif time>7.00 and time<=8.30 :
    print(time,"break time for the studets and can did their break fast in the given time")
elif time>8.30 and time<=12.30 :
    print(time, "can students do thecoding in the given time")
elif time>12.30 and time<=14.00 :
    print(time,"lunch break for the students and taking the rest")
elif time>14.00 and time<=17.00 :
    print("second coding time for the students")
elif time>17.00 and time<=18.00 :
    print("break for the students and taking the snacks")
elif time>18.00 and time<20.00 :
    print("english class and soft skills")
elif time>=20.00 :
    print("take dinner and take rest  ")