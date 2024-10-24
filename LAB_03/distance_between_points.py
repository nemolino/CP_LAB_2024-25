from math import sqrt


def calculate_distance(x1, y1, x2, y2):
    x_diff = x2 - x1
    y_diff = y2 - y1
    return sqrt(x_diff * x_diff + y_diff * y_diff)


x1 = float(input("Insert x1 : "))
y1 = float(input("Insert y1 : "))
x2 = float(input("Insert x2 : "))
y2 = float(input("Insert y2 : "))

print("The distance between P1 and P2 is", calculate_distance(x1, y1, x2, y2))