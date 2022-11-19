n= int(input("enter the number: "))
n1=0
n2=1
fn=0

if n<=2:
    print(n-1)

for i in range (n-2):
    fn= n1+n2
    n1=n2
    n2=fn
print("Non-Recursive",fn)


def fibo_recursive(n):
    if n<=2:
        return n-1
    else: 
        return fibo_recursive(n-1)+ fibo_recursive(n-2)
print("Recursive",fibo_recursive(n))