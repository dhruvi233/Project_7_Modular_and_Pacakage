"""Functions for calculationg the area of a triangle."""

def triangle_area(base, height):
    """Calculate triangle area using (base * height) / 2."""
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative.")

    return (base * height) / 2


if __name__ == "__main__":
    try:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))

        area = triangle_area(base, height)
        print(f"Area of the triangle: {area:.2f}")

    except ValueError as error:
        print("Error:", error)
