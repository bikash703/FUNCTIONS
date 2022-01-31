num1=int(input("Enter 1st Number: \n"))
num2=int(input("Enter 2nd Number: \n"))
num3=int(input("Enter 3rd Number: \n"))

def Greatest(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

gt=Greatest(num1,num2,num3)
print("Greatest Number is " + str(gt))  

    