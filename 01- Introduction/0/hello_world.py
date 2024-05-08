# A simple version with a comment
print("Hello, World!")  # This line prints "Hello, World!" to the console


# Using a function with a docstring
def say_hello():
    """
    This function prints "Hello, World!" to the console.
    """
    print("Hello, World!")


say_hello()


# Using a class with a method comment
class Greeter:
    def greet(self):
        # This method prints "Hello, World!" when called
        print("Hello, World!")


greeter = Greeter()
greeter.greet()

# String formatting with a variable and a comment
name = "World"
print(f"Hello, {name}!")  # Using an f-string for formatted output

# Using a lambda function with a comment
greet = lambda: "Hello, World!"  # A lambda function that returns "Hello, World!"
print(greet())

# Multi-line printing with triple quotes
print("""
Hello, 
World!
""")  # Prints "Hello, World!" on two separate lines
