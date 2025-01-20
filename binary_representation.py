"""Let the user enter a positive int number (including 0)
(ensure that a positive value (>=0) has been entered!)
Store the base 2 in a variable called new_base›
Compute the representation of the number in base new_base (see slide 110) and print the new representation.
The binary digits should be in the correct order!
What happens if you change new_base to another value, e.g.
new_base = 7 or
new_base = 1 or
new_base = 0 ?
Answer this question in the comment field.
Hinweis:
In this task, you exercise:

binary representation of unsigned numbers
control structures"""

# asks the user to enter a positive int
while True:
    try: 
        number = int(input("Enter a positive integer (including 0): "))
        if number >= 0:
            break
        else: 
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# stores the base
new_base = 2

# computes the representatino in the given base

if new_base > 1:
    result = ""
    quotient = number
    while quotient > 0:
        remainder = quotient % new_base
        result = str(remainder) + result
        quotient //= new_base
    result = result if result else "0"
    print(f"The represenation of {number} in base {new_base} is: {result}")
else:
    print("Invaliud base! The base must be greater than 1.")


"""
new_base = 7:
The number is converted into its base 7 representation (digits range from 0 to 6).
For example, 100 in base 7 is 202.

new_base = 1:
This is invalid because base 1 does not exist in standard number systems.

new_base = 0:
This is invalid as a base cannot be zero. The program will not compute a representation 
and will display an error message ("Invalid base! The base must be greater than 1").
"""