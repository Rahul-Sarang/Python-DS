#separate integer and string from list

a=["rhl",21,7,45,"my"]
ls=[]
li=[]
for i in a:
    if isinstance(i,str):
        ls.append(i)
    if isinstance(i,int):
        li.append(i)
print(a)
print(ls)
print(li)
        