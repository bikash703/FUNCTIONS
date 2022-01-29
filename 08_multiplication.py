n=int(input("Enter a Number: "))
def mul(n):
    for i in range(1,11):
        print(str(n) + "*" + str(i) + "=" + str(n*i))#return dont work this time

a=mul(n)
print("Multiplication Table of ",a,"is ",a)