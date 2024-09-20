a=int(input("Enter the number "))
b=int(input("Enter the number "))
c=int(input("Enter the number "))

max_num=a
if max_num<b:
    max_num=b
else:
    pass

if max_num<c:
    max_num=c
else:
    pass
 
print("The largest number is ",max_num)