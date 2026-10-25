"""Custom module for string-related utility functions."""


def clean_text(text):
    """Remove extra spaces from the beginning and end."""
    return text.strip()


def word_count(text):
    """Count the words in a string."""
    return len(text.split())


def reverse_text(text):
    """Return the text in reverse order."""
    return text[::-1]


def is_palindrome(text):
    """Check whether text is a palindrome, ignoring spaces and case."""
    cleaned = "".join(text.lower().split())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    sample = input("Enter some text: ")

    print("Cleaned text:", clean_text(sample))
    print("Word count:", word_count(sample))
    print("Reversed text:", reverse_text(sample))
    print("Is palindrome:", is_palindrome(sample))