import math 
def calculate_circle_area(radius: float):
    return radius * radius * math.pi
    

print("welcome to the circle area calculator!")
# Get the radius from the user 
r = float(input("entrer the raduis of the circle:"))
area = calculate_circle_area(r)
print("the area is",area)