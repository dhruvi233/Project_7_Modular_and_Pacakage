"""Functions for calculating the area of a rectangle."""


def rectangle_area(length, width):
    """Calculate the area using length multiplied by width."""
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")

    return length * width


if __name__ == "__main__":
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))

        area = rectangle_area(length, width)
        print(f"Area of the rectangle: {area:.2f}")

    except ValueError as error:
        print("Error:", error)
