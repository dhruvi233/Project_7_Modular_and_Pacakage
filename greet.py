"""A custom module  for greeting users."""

def get_greeting(name="User"):
    """Return a welcome message."""
    return f"Welcome to the Multi-Utility Toolkit, {name}!"


if __name__ == "__main__":
    user_name = input("Enter your name: ").strip()

    if not user_name:
        user_name = "User"

    print(get_greeting(user_name))