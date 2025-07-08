def Test(arg1, **kwargs):
    print('The arg1 is', arg1)
    print(kwargs)

Test(10)
Test(10, Agra='Taj Mahal', Delhi='Red Fort')


def Test(arg1, **kwargs):
    print('The arg1 is', arg1)
    for k, v in kwargs.items():
        print(v, 'belongs to', k)

Test(10, Agra='Taj Mahal', Delhi='Red Fort')



