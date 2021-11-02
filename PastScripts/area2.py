import math

def rectangle():
    print("you pick a Rectagle")
    height = float(input("What is the height:  "))
    length = float(input("What is the length:  "))
    return height * length

def trapezoid():
    print("you pick a Trapezoid")
    base1=float(input("What is the Top Base:  "))
    base2=float(input("What is the Bottom Base:  "))
    height=float(input("What is the height:  "))
    return height*((base1+base2)*2)

def circle():
    print("you pick a Circle")
    radius=float(input("What is the radius of the circle:  "))
    pie=math.radians(180)
    return pie*(radius**2)

def triangle():
    print("you pick a Triangle")
    height=float(input("What is the height of the triangle:  "))
    base=float(input("What is the base of the triangle:  "))
    return (height*base)/2

print("Find the area of these shapes")
shape = input("R for rectangle, T for Trapezoid, c for circle, A for triangle:  ")

if shape.lower() == "r":
    area = rectangle()
elif shape.lower() == "t":
    area = trapezoid()
elif shape.lower() == "c":
    area = circle()
elif shape.lower() == "a":
    area = triangle()
else:
    print("You did not pick a shape")
    exit()

print(f"The area is:  {area}")