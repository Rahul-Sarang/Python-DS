def Test(arg1,*vartuple):
    "This is test"
    print("Output is:",arg1)
    
    for i in vartuple:
        print(i)
    return

Test(20)
Test(20,30,5)
Test(10,'anil',20,[1,2,3,4])