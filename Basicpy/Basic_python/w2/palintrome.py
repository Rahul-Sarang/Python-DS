a=input("Enter a string to check palintrome or not :")
l=len(a)
for i in range(len(a)//2):
    if a[i]!=a[-(i+1)]:
        print(a ," is not a palintrome")
        break
else:
    print(a ," is a palintrome")
