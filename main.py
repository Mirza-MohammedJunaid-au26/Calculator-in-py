def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    return x/y

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choose = int(input("Choose : "))

if choose == 1:
    ans = add(num1,num2)
    print("Addition is :",ans)
elif choose == 2:
    ans = subtract(num1,num2)
    print("Subtratction is :",ans)
elif choose == 3:
    ans = multiply(num1,num2)
    print("Multiplication is :",ans)
elif choose == 4:
    ans = division(num1,num2)
    print("Division is :",ans)
else :
    print("!!!Enter A Valid Number!!!")