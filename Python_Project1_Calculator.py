def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "Error! Division by zero."
    else:
        return x/y
def mod(x,y):
    if y==0:
        return "Error! Division by zero."
    else:
        return x%y
def floordiv(x,y):
    if y==0:
        return "Error! Division by zero."
    else:
        return x//y
while True:
    print("Select operation.")
    print("1.Addition")
    print("3.Multiplication")
    print("2.Subtraction")
    print("4.Division")
    print("5.Modulus")
    print("6.Floor Division")
    print("7.Exit")
    choice=int(input("Enter choice(1-6):"))
    if choice <=6:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
    if choice == 1:
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice == 2:
        print(num1,"-",num2,"=",sub(num1,num2))
    elif choice == 3:
        print(num1,"*",num2,"=",mul(num1,num2))
    elif choice == 4:
        print(num1,"/",num2,"=",div(num1,num2))
    elif choice == 5:
        print(num1,"%",num2,"=",mod(num1,num2))
    elif choice == 6:
        print(num1,"//",num2,"=",floordiv(num1,num2))
    elif choice == 7:
        print("Exiting the program.")
        break
    else:
        print("Invalid input")