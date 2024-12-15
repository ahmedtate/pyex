import math 
from datetime import date
def calculate_age(birth : float):
    return date.today().year - birth
age = calculate_age(1990)
print(age)