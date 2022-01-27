x=int(input("Enter a side of square:"))
area=lambda x:x*x
print("Area of square:{0}".format(area(x)))
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the bredth of rectangle:"))
area=lambda l,b:l*b
print("Area of rectangle:{0}".format(area(l,b)))
b=int(input("Enter the bredth of triangle:"))
h=int(input("Enter the height of triangle:"))
area=lambda b,h:0.5*b*h
print("Area of triangle:{0}".format(area(b,h)))