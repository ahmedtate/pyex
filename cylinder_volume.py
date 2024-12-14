import math
def calculate_cylinder_volume (radius : float, height : float):
    return radius**2 * math.pi * height


volume = calculate_cylinder_volume(9,7)
print(volume)