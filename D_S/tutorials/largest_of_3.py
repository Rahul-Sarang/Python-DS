x,y,z=input("Enter 3 numbers :").split()
x,y,z=int(x),int(y),int(z)

if x>y and y>z:
    print(f"{x} is largest")
elif y>x and x>z:
     print(f"{y} is largest")
else:
    print(f"{z} is largest")
    
    