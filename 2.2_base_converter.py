"""
    Write a function which converts a given number into a representation with another base. The function gets the vale and the base as arguments and returns s String with code in the given base
Replace digits in the new representation which are larger than 9 by capital letters 'A', 'B', ... before printing the new representation.
Write a main program which
calls a self-defined function which asks the user to enter a  base value in range 2..34  and returns it
this value should be assigned to a variable base
calls a self-defined function which asks the user to enter a positive integer as value
this value should be assigned to a variable n 
calls the newly defined function to convert n into a representation with the given base.
print the resulting String

Hints:

You need to define a function for reading values also (see lecture).
The values of the letters A-F are:  10 ~ A, 11~ B, 12~ C, 13~ D, 14~ E, 15 ~ F, ..
The Unicodes or ASCII-codes of the capital letters are increasing number:  ord('A') = 65, ord('B') = 66,.. . You can use this to calculate the letter instead of having a switch-statement!
"""

def get_base():
    """Prompts the user for a base vlaue between 2 and 34 and returns it."""
    while True:
        try: 
            base = int(input("Enter a base vlaue (between 2 and 34): "))
            if 2 <= base <= 34:
                return base
            else:
                print("Base must be between 2 and 34. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_positive_integer():
    """Prompts the user for a positive integer and returns it."""
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n >= 0:
                return n
            else:
                print("Please enter a non-negative integer")
        except ValueError:
            print("Invalid Input. Please enter an integer")

def convert_to_base(value,base):
    """
    Converts the given number to a representaiton in the given base.
    Returns the results as a string
    """
    if value == 0:
        return "0"
    digits = ""
    while value > 0:
        remainder = value % base
        if remainder >= 10:
            # Converts numbers greater than 9 to letters
            digits = chr(ord('A') + (remainder - 10)) + digits
        else:
            digits = str(remainder) + digits
        value //= base

    return digits

# main program

def main():
    print("Welcome to the base conversion program!")

    # get base value
    base = get_base()
    # get positive integer value
    n = get_positive_integer()
    # convert the number to the specifies base
    result = convert_to_base(n, base)
    # print result
    print(f"The representation of {n} in base {base} is: {result}")

# run main
if __name__ == "__main__":
    main()