def fact_num(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
        
    return fact

n=int(input("Enter a number to find factorial :"))
result=fact_num(n)
print(f"Factorial of number {n} is : {result}")