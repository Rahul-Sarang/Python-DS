# find fqy of each character in a string

text=input("Enter a string :")
#l=text.split()

d=dict()
for i in text:# l
    d[i]=d.get(i,0)+1
    
print(d)