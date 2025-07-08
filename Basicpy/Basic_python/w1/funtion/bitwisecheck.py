def checkevenodd(num):
    if num&1 ==0:
        return "Even"
    else:
        return "Odd"
num=int(input("Enter the number :"))
result=checkevenodd(num)


print(f"The number {num} is {result}")
#formatted string literal(f-string),(f"{}")