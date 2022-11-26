import math
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def mod(x,y):
    return x%y
def pow(x,y):
    return x**y
def sqrt(x):
    return x
def degree_converter(x):
    return x
def radian_converter(x):
    return x
print("select operation")
print("1. addition (+)")
print("2. subtraction (-)")
print("3. multiplication (*)")
print("4. division (/)")
print("5. mod (%)")
print("6. exponent (**)")
print("7. square root (math.sqrt)")
print("8. sin value")
print("9. cos value")
print("10. tan value")
print("11. degree converter")
print("12. radian converter")
print("13. end calculation")
while True:
    choice=input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13)")
    if choice in ('1','2','3','4','5','6'):
        num1=float(input("Enter 1st number:"))
        num2=float(input("Enter 2nd number:"))
    if choice=='1':
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice=='2':
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif choice=='3':
        print(num1,"*",num2,"=",multiply(num1,num2))
    elif choice=='4':
        print(num1,"/",num2,"=",divide(num1,num2))
    elif choice=='5':
        print(num1,"%",num2,"=",mod(num1,num2))
    elif choice=='6':
        print(num1,"**",num2,"=",pow(num1,num2))
    if choice in ('7','8','9','10','11','12'):
        num1=float(input("Enter number:"))
    if choice=='7':
        print("square root of",num1,"=",math.sqrt(num1))
    elif choice=='8':
        print("sin of",num1,"=",math.sin(num1))
    elif choice=='9':
        print("cos of",num1,"=",math.cos(num1))
    elif choice=='10':
        print("tan of",num1,"=",math.tan(num1))
    elif choice=='11':
        print("The degree value of",num1,"radian =",math.degrees(num1))
    elif choice=='12':
        print("The radian value of",num1,"degree =",math.radians(num1))
    if choice in ('13'):
        print("Thank you")
        break
