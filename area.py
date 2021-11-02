import math
print("Find the are these shapes")
shape = input("R for rectangle, T for Trapezoid, c for circle, A for triangle:  ")

if shape.lower() == "r":
    print("you pick a Rectagle")
    height=float(input("What is the height:  "))
    length=float(input("What is the length:  "))
    area=height*length
    print(f"The area is {area}")
elif shape.lower() == "t":
    print("you pick a Trapezoid")
    base1=float(input("What is the Top Base:  "))
    base2=float(input("What is the Bottom Base:  "))
    height=float(input("What is the height:  "))
    area=height*((base1+base2)*2)
    print(f"The area is {area}")
elif shape.lower() == "c":
    print("you pick a Circle")
    radius=float(input("What is the radius:  "))
    pie=math.radians(180)
    area=pie*(radius**2)
    print(f"The area is {area}")
elif shape.lower() == "a":
    print("you pick a Triangle")
    height=float(input("What is the height:  "))
    base=float(input("What is the base:  "))
    area=(height*base)/2
    print(f"The area is {area}")
else:
    print("You did not pick a shape")
