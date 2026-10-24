#assignment pre_2
print("1.Area of circle")
print("2.Area of triangle")
print("3.Area of square")
print("4.Area of rectangle")
print("5.simple interest")
select = int(input("Enter your choice number: "))
if select == 1:
    r = float(input("Enter the radius of the circle: "))
    area = 3.14 * r * r
    print("The area of the circle is ", area)
elif select == 2:
    b = float(input("Enter the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    triangle = (0.5 * b * h)
    print("The area of the triangle is ", triangle)
elif select == 3:
    s = float(input("Enter the base of the Square: "))
    area = s * s
    print("The area of the Square is ", area)
elif select == 4:
    l = float(input("Enter the length of the rectangle: "))
    bre = float(input("Enter the breadth of the rectangle: "))
    print("The area of the rectangle is ", l * bre)
elif select == 5:
    p = float(input("Enter the principal of the amount: "))
    r = float(input("Enter the rate of the interest: "))
    n = float(input("Enter the time in years: "))
    interest = (p * r * n) / 100
    print("The simple interest is ", interest)
else:
    print("Invalid input")