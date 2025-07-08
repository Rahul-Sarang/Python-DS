#find repeat items in tuple

a=(2,3,4,3,6,3,7,8,1,1,1,7,7)
l=[]
for i in a:
    if a.count(i)>1 and l.count(i)==0:
        l.append(i)
        print(i,"has to be repeated")