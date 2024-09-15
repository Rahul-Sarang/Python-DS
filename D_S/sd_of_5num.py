import math
x1,x2,x3,x4,x5=input("enter 5 numbers").split()
x1=int(x1)
x2=int(x2)
x3=int(x3)
x4=int(x4)
x5=int(x5)
avg=(x1+x2+x3+x4+x5)/5
x1_avg=(x1-avg)*(x1-avg)
x2_avg=(x2-avg)*(x2-avg)
x3_avg=(x3-avg)*(x3-avg)
x4_avg=(x4-avg)*(x4-avg)
x5_avg=(x5-avg)*(x5-avg)

SD = math.sqrt((x1_avg+x2_avg+x3_avg+x4_avg+x5_avg)/4)


print("The average is =",avg)
print("The SD is =",SD)