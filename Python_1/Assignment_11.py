"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 11
Challenge: Use a loop structure to generate the Collatz sequence until it reaches 1. Handle cases where the user enters a non-numeric input.
=================================
Description: Write a program that generates the Collatz sequence for a given positive integer entered by the user.
The Collatz sequence is generated iteratively by repeatedly applying the following rules:
If the current number is even, divide it by 2.
If the current number is odd, multiply it by 3 and add 1.
"""

# Define a function to generate the Collatz sequence
def collatz_sequence(n):
    while n != 1:
        print(n, end=" -> ")  # Print the current number
        # Apply Collatz rules based on whether n is even or odd
        if n % 2 == 0:  # If the number is even
            n //= 2  # Divide it by 2
        else:  # If the number is odd
            n = 3 * n + 1  # Multiply by 3 and add 1
    print(1)  # Print the last number (1)

# Loop until the user enters valid input
while True:
    try:
        # Ask the user to enter a positive integer
        user_input = input("Enter a positive integer: ")
        number = int(user_input)  # Convert input to an integer

        # Check if the input is a positive number
        if number <= 0:
            print("Please enter a positive integer.")  # Prompt for valid input
        else:
            collatz_sequence(number)  # Generate Collatz sequence
            break  # Exit the loop once valid input is processed
    except ValueError:
        print("Invalid input. Please enter a numeric value.")  # Handle non-numeric input

