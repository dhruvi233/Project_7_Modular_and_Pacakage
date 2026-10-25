"""Functions for calculating the area of a circle."""
import math
def circle_area(radius):
    """Calculate the area of a circle using pi * radius squared."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius **2
if __name__ == "__main__":
    radius =  float(input("Enter the radius of the circle:"))
    try:
        area = circle_area(radius)
        print(f"Area of the circle:{area:2f}")
    except ValueError as error:
        print("Error:", error)
        
