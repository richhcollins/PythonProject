"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 15
Challenge: Optimize the function to handle large input numbers efficiently.
=====================================================
Description: Develop a function called is_prime that takes a positive integer as input and returns True if it is a prime number, and False otherwise
"""

# Import math module
import math

def is_prime(n):
    if n < 2:  # Numbers less than 2 are not prime
        return False
    if n in (2, 3):  # 2 and 3 are prime numbers
        return True
    if n % 2 == 0 or n % 3 == 0:  # Avoid even numbers and multiples of 3
        return False

    # Check divisibility using 6k ± 1 optimization
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

while True:  # Loop until a valid input is provided
    try:
        # Get user input and convert to integer
        number = int(input("Enter a positive integer: "))
        if number > 0:  # Check if the input is a positive integer
            # Print results
            print(f"True: {number} is a prime number" if is_prime(number) else f"False: {number} is not a prime number")
            break  # Exit loop once valid input is processed
        else:
            print("The number must be positive. Please try again.")
    except ValueError:  # Error handling for non-numeric input
        print("Invalid input. Please enter a numeric value.")
