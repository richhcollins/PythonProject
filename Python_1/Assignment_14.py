"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 14
Challenge: Handle negative exponents efficiently.
====================================
Description: Develop a function named power that takes two integers, base and exponent, as input and returns base raised to the power of exponent.
"""

# Compute base raised to the power of exponent
def power(base, exponent):

    if exponent < 0:
        return "Negative exponents are not supported"
    elif exponent == 0:
        return 1  # Any number to the power of 0 is 1
    else:
        result = 1
        for _ in range(exponent):
            result *= base  # Multiply base exponent times
        return result

# Get user input
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Compute and display the result
print(f"{base} raised to the power of {exponent} is {power(base, exponent)}")
