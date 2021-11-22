import math

# enter the radius of the circle
radius_str = input ("Enter the radius: ")

# change int to str
radius_int = int (radius_str)

circum = 2*math.pi*radius_int
area = math.pi*(radius_int**2)

# calculation of the area
print (" the circumference of the circle is: ", circum, ", and the area is: ", area)
