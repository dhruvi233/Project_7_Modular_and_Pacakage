"""Multi-Utility Toolkit - Project 7: Modular and Packager."""

import datetime
import time
import math
import random
import uuid
import string
import importlib

from utilities import file_utils, math_utils
from shapes import circle_area, rectangle_area
from geometry import triangle_area
from greet import get_greeting
from helper import show_separator, pause_message, show_return_message


def read_int(prompt, minimum=None, maximum=None):
    """Read and validate an integer."""
    while True:
        try:
            value = int(input(prompt).strip())

            if minimum is not None and value < minimum:
                print(f"Enter a number greater than or equal to {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Enter a number less than or equal to {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt, minimum=None):
    """Read and validate a number."""
    while True:
        try:
            value = float(input(prompt).strip())

            if not math.isfinite(value):
                print("Please enter a finite number.")
                continue

            if minimum is not None and value < minimum:
                print(f"Enter a number greater than or equal to {minimum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def datetime_menu():
    """Menu for date and time operations."""
    while True:
        show_separator()
        print("DATETIME AND TIME OPERATIONS")
        print("1. Current date and time")
        print("2. Difference between two dates")
        print("3. Custom date formatting")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Back to main menu")

        choice = read_int("Enter your choice: ", 1, 6)

        if choice == 1:
            now = datetime.datetime.now()
            print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == 2:
            try:
                first = datetime.date.fromisoformat(
                    input("Enter first date (YYYY-MM-DD): ").strip()
                )
                second = datetime.date.fromisoformat(
                    input("Enter second date (YYYY-MM-DD): ").strip()
                )
                difference = abs((second - first).days)
                print(f"Difference: {difference} days")
            except ValueError:
                print("Invalid date. Use YYYY-MM-DD.")

        elif choice == 3:
            now = datetime.datetime.now()
            print("Formatted date:", now.strftime("%A, %d %B %Y at %I:%M %p"))

        elif choice == 4:
            input("Press Enter to start the stopwatch.")
            start = time.perf_counter()
            input("Press Enter to stop the stopwatch.")
            elapsed = time.perf_counter() - start
            print(f"Elapsed time: {elapsed:.2f} seconds")

        elif choice == 5:
            seconds = read_int("Enter countdown seconds (0-3600): ", 0, 3600)
            while seconds > 0:
                print(f"Time remaining: {seconds} seconds")
                time.sleep(1)
                seconds -= 1
            print("Countdown complete!")

        else:
            return

        pause_message()


def math_menu():
    """Menu for mathematical operations."""
    while True:
        show_separator()
        print("MATHEMATICAL OPERATIONS")
        print("1. Factorial")
        print("2. Compound interest")
        print("3. Trigonometry (degrees)")
        print("4. Logarithm")
        print("5. Circle area")
        print("6. Rectangle area")
        print("7. Triangle area")
        print("8. Temperature conversion (Celsius to Fahrenheit)")
        print("9. Distance conversion (kilometres to miles)")
        print("10. Back to main menu")

        choice = read_int("Enter your choice: ", 1, 10)

        try:
            if choice == 1:
                number = read_int("Enter a non-negative integer: ", 0)
                print("Factorial:", math_utils.factorial(number))

            elif choice == 2:
                principal = read_float("Enter principal amount: ", 0)
                rate = read_float("Enter annual interest rate (%): ", 0)
                years = read_float("Enter time in years: ", 0)
                amount = math_utils.compound_amount(principal, rate, years)
                print(f"Final amount: {amount:.2f}")
                print(f"Compound interest: {amount - principal:.2f}")

            elif choice == 3:
                degrees = read_float("Enter angle in degrees: ")
                radians = math.radians(degrees)
                print(f"sin({degrees}) = {math.sin(radians):.4f}")
                print(f"cos({degrees}) = {math.cos(radians):.4f}")
                print(f"tan({degrees}) = {math.tan(radians):.4f}")

            elif choice == 4:
                number = read_float("Enter a positive number: ", 0)
                if number == 0:
                    print("Logarithm is defined only for positive numbers.")
                else:
                    print("Natural logarithm:", math.log(number))
                    print("Base-10 logarithm:", math.log10(number))

            elif choice == 5:
                radius = read_float("Enter circle radius: ", 0)
                print(f"Circle area: {circle_area(radius):.2f}")

            elif choice == 6:
                length = read_float("Enter rectangle length: ", 0)
                width = read_float("Enter rectangle width: ", 0)
                print(f"Rectangle area: {rectangle_area(length, width):.2f}")

            elif choice == 7:
                base = read_float("Enter triangle base: ", 0)
                height = read_float("Enter triangle height: ", 0)
                print(f"Triangle area: {triangle_area(base, height):.2f}")

            elif choice == 8:
                celsius = read_float("Enter temperature in Celsius: ")
                print(
                    f"Fahrenheit: "
                    f"{math_utils.celsius_to_fahrenheit(celsius):.2f}"
                )

            elif choice == 9:
                kilometres = read_float("Enter distance in kilometres: ", 0)
                print(
                    f"Miles: "
                    f"{math_utils.kilometers_to_miles(kilometres):.2f}"
                )

            else:
                return

        except (ValueError, OverflowError) as error:
            print("Could not complete calculation:", error)

        pause_message()


def random_menu():
    """Menu for random data generation."""
    while True:
        show_separator()
        print("RANDOM DATA GENERATION")
        print("1. Generate random integer")
        print("2. Generate random list")
        print("3. Generate random password")
        print("4. Generate six-digit OTP")
        print("5. Random sample from a list")
        print("6. Dice simulation")
        print("7. Back to main menu")

        choice = read_int("Enter your choice: ", 1, 7)

        if choice == 1:
            low = read_int("Enter minimum integer: ")
            high = read_int("Enter maximum integer: ")
            if low > high:
                print("Minimum cannot be greater than maximum.")
            else:
                print("Random number:", random.randint(low, high))

        elif choice == 2:
            count = read_int("How many numbers? ", 1, 100)
            low = read_int("Enter minimum value: ")
            high = read_int("Enter maximum value: ")
            if low > high:
                print("Minimum cannot be greater than maximum.")
            else:
                print("Random list:", [
                    random.randint(low, high) for _ in range(count)
                ])

        elif choice == 3:
            length = read_int("Password length (4-64): ", 4, 64)
            characters = string.ascii_letters + string.digits + "!@#$%&*?"
            password = "".join(
                random.SystemRandom().choice(characters)
                for _ in range(length)
            )
            print("Generated password:", password)

        elif choice == 4:
            print("Generated OTP:", random.randint(100000, 999999))

        elif choice == 5:
            items = [
                item.strip()
                for item in input("Enter items separated by commas: ").split(",")
                if item.strip()
            ]
            if not items:
                print("Please enter at least one item.")
            else:
                count = read_int(
                    f"How many items to sample (1-{len(items)})? ",
                    1,
                    len(items),
                )
                print("Random sample:", random.sample(items, count))

        elif choice == 6:
            print("Dice result:", random.randint(1, 6))

        else:
            return

        pause_message()


def file_menu():
    """Menu for custom file operations."""
    while True:
        show_separator()
        print("FILE OPERATIONS")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read a file")
        print("4. Append to a file")
        print("5. Back to main menu")

        choice = read_int("Enter your choice: ", 1, 5)

        if choice == 5:
            return

        filename = input("Enter file name (e.g. example.txt): ").strip()

        try:
            if choice == 1:
                file_utils.create_file(filename)
                print("File created successfully.")

            elif choice == 2:
                content = input("Enter text to write: ")
                file_utils.write_file(filename, content)
                print("Text written successfully.")

            elif choice == 3:
                print("\nFile contents:")
                print(file_utils.read_file(filename))

            elif choice == 4:
                content = input("Enter text to append: ")
                file_utils.append_file(filename, content)
                print("Text appended successfully.")

        except (OSError, ValueError) as error:
            print("File operation failed:", error)

        pause_message()


def explore_modules():
    """Explore attributes of built-in and custom modules using dir()."""
    modules = {
        "datetime": datetime,
        "time": time,
        "math": math,
        "random": random,
        "uuid": uuid,
        "file_utils": file_utils,
        "math_utils": math_utils,
    }

    name = input(
        "Module name (datetime/time/math/random/uuid/file_utils/math_utils): "
    ).strip()

    module = modules.get(name)

    if module is None:
        try:
            module = importlib.import_module(name)
        except ImportError:
            print("Module not found. Please enter a valid importable module.")
            return

    print(f"\nAttributes in module '{name}':")
    print(dir(module))


def main():
    """Run the Multi-Utility Toolkit."""
    print(get_greeting())
    pause_message()

    while True:
        show_separator()
        print("MULTI-UTILITY TOOLKIT")
        print("1. Datetime and time operations")
        print("2. Mathematical operations")
        print("3. Random data generation")
        print("4. Generate unique identifier (UUID)")
        print("5. File operations")
        print("6. Explore module attributes (dir())")
        print("7. Exit")

        choice = read_int("Enter your choice: ", 1, 7)

        if choice == 1:
            datetime_menu()
        elif choice == 2:
            math_menu()
        elif choice == 3:
            random_menu()
        elif choice == 4:
            print("Generated UUID4:", uuid.uuid4())
            pause_message()
        elif choice == 5:
            file_menu()
        elif choice == 6:
            explore_modules()
            pause_message()
        elif choice == 7:
            show_separator()
            print("Thank you for using the Multi-Utility Toolkit!")
            show_separator()
            break

        show_return_message()


if __name__ == "__main__":
    main()