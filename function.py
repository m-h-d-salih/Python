def hlo(name):
    return 'helllo '+name
print(hlo("salih"))


#recusrion
def recursion(n):
    if n<=1:
        return n
    else:
        return n+recursion(n-1)
print(recursion(5))

#lambda function or anonymous function
l=lambda x:x*x
print(l(10))
a=[1,2,3,4,5]
def even(x):
    if(x%2==0):
        return x
f=filter(even,a)
print(list(f))
odd=filter(lambda x:x%2==1,a)
print(list(odd))