#Simple example to show debugging in Visual Studio.
def fibb(n):
    a,b,c=1,1,1
    if n<=2:
        return 1
    for i in range(1, n-1):
        c = a + b
        a=b
        b=c
    return c

n = input()
print fibb(n)