#assignment pre_7
print("<<<<<<<<<Arithmetic operation>>>>>>>>>>")
print("1.Addition:")
print("2.Subtraction:")
print("3.Multiplication:",)
print("4.Division:")

def add(a,b):
    return a+b
def sub(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
select = int(input("Enter your choice number(1 to 4): "))
a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))
if select == 1:
    print("Addition is :",a+b)
elif select == 2:
    print("Subtraction is :",a-b)
elif select == 3:
    print("Multiplication is :",a*b)
elif select == 4:
    print("Division is :",a/b)
else:
    print("Invalid choice")