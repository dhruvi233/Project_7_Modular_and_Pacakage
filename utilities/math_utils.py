"""Custom module for mathematical utility functions."""

import math


def factorial(number):
    """Calculate the factorial of a non-negative integer."""
    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError("Please enter a whole number.")

    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    return math.factorial(number)


def compound_amount(principal, rate, years):
    """Calculate compound amount using annual compounding."""
    if principal < 0:
        raise ValueError("Principal cannot be negative.")

    if rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    if years < 0:
        raise ValueError("Years cannot be negative.")

    return principal * (1 + rate / 100) ** years


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def kilometers_to_miles(kilometers):
    """Convert kilometers to miles."""
    if kilometers < 0:
        raise ValueError("Distance cannot be negative.")

    return kilometers * 0.621371
