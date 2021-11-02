import math
class ryanmath:

    #returns surface area of the sphere
    def sphere(r):
        return 4*math.pi*(r**2)

    #returns surface area of the cylinder
    def cylinder(r,h):
        return ((2*math.pi*r*h) + (2*math.pi*r**2))

    #return area of rectangle
    def rectangle(h,l):
        return (h * l)

    #returns area of a trapezoid
    def trapezoid(b1,b2,h):
        return h*((b1+b2)*2)

    #returns area of circle
    def circle(r):
        return math.pi*(r**2)

    #returns area of triangle
    def triangle(h,b):
        return (h*b)/2




