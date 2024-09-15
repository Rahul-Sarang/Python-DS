import math
numbers= list(map(int,input("Enter numbers :").split()))
total=sum(numbers)
avg=sum(numbers)/len(numbers)

variance=sum((x-avg)**2 for x in numbers)/(len(numbers)-1)

SD=math.sqrt(variance)

print("The sum of ",len(numbers), ":",total)
print("The average :",avg)
print("Thevariance :",variance)
print("The standard deviation :",SD)