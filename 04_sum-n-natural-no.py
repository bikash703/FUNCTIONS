n=int(input("Enter a Number: "))
def sum(n):
    i=1
    a=0
    while(i<=n):
        a=a+i
        i=i+1
    return a
def sum_recursive(n):
    return n + sum(n-1)
f=sum(n)
print("Sum of",n, "Number is ",f)
    
    
