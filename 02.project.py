

from math import pi, sin, cos, acos

print("The Great Circle Calculator")
print("===========================")

r = float(input("Enter the radius of the sphere (in km): "))

x1 = float(input("Enter longitude of point 1 (degrees): "))
y1 = float(input("Enter latitude of point 1 (degrees): "))

x2 = float(input("Enter longitude of point 2 (degrees): "))
y2 = float(input("Enter latitude of point 2 (degrees): "))

x1 = x1 * pi / 180
y1 = y1 * pi / 180
x2 = x2 * pi / 180
y2 = y2 * pi / 180

d = r * acos(
    sin(y1) * sin(y2) +
    cos(y1) * cos(y2) * cos(x1 - x2)
)

d = round(d, 2)

print("The great-circle distance is", d, "km")
