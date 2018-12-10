import math
shapes = ['A', 'B', 'C', 'D', 'E']
# A = Triangle, B = Square, C = Circle, D = Rectangle, E = Trapezium
specs = ['1', '2']
# 1 = Area , 2 = Perimeter
bic = input("Please choose from options A-E: ").upper()


def triangle():
    if bic == shapes[0]:
        bic_2 = input("Pick between numbers 1 and 2: ")
        if bic_2 == specs[0]:
            length = float(input("What is your length in metres?"))
            breadth = float(input("What is your breadth in metres?"))
            area = 0.5 * length * breadth
            print("The Area of the shape is {} in metre square".format(str(area)))
        elif bic_2 == specs[1]:
            a = float(input("What is the value of the shape:"))
            b = float(input("What is the value of the shape:"))
            c = float(input("What is the value of the shape:"))
            peri = a + b + c
            print("The perimeter of the shape is {} metres".format(str(peri)))
        print("This is a Triangle!!!!!!")


def square():
    if bic == shapes[1]:
        house = input("Pick between numbers 1 and 2: ")
        if house == specs[0]:
            length = float(input("What is your length in metres?"))
            area = pow(length, 2)
            print("The area of the shape is {} in metre square".format(str(area)))
        elif house == specs[1]:
            a = float(input("What is the value of one of the sides in metres?"))
            perimeter = 4 * a
            print("The perimeter of the shape is {} metres".format(str(perimeter)))
        print("This is a Square!!!!")


def circle():
    if bic == shapes[2]:
        man = input("Pick between numbers 1 and 2: ")
        if man == specs[0]:
            radius = float(input(" Give me the radius in metres: "))
            area = (22/7) * pow(radius, 2)
            print("The area of this shape is {} metres square".format(str(area)))
        elif man == specs[1]:
            rad = float(input("Give me the radius in metres: "))
            peri = 2 * (22/7) * rad
            print("The perimeter of the shape is {} metres".format(str(peri)))
        print("This is a Circle!!!!!")


def rectangle():
    if bic == shapes[3]:
        hot = input("Pick between numbers 1 and 2: ")
        if hot == specs[0]:
            length = float(input("What is your length in metres?"))
            breadth = float(input("What is your breadth in metres?"))
            area = length * breadth
            print("The area of this shape is {} in metre square".format(str(area)))
        elif hot == specs[1]:
            length = float(input("What is your length in metres?"))
            breadth = float(input("What is your breadth in metres?"))
            perimeter = 2 * (length + breadth)
            print("The perimeter of the shape is {} metres".format(str(perimeter)))
        print("This is a Rectangle!!!!!!")


def trapezium():
    if bic == shapes[4]:
        trap = input("Pick between numbers 1 and 2: ")
        if trap == specs[0]:
            a = float(input("What is the value of the top side?"))
            b = float(input("What is the value of the base?"))
            h = float(input("What is the height?"))
            area = 0.5 * (a + b) * h
            print("The area of this shape is {} in metre square".format(str(area)))
        elif trap == specs[1]:
            a = float(input("What is the value of the top side?"))
            b = float(input("What is the value of the base?"))
            h = float(input("What is the height?"))
            c = float(input("What is the value of the slant side?"))
            peri = a + b + c + h
            print("The perimeter of this shape is {} metre".format(peri))
        print("This is a Trapezium!!!!!")


triangle()
square()
circle()
rectangle()
trapezium()
