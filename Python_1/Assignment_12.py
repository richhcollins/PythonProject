"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 12
Challenge: Use nested loop structures to print the pattern efficiently and neatly. Allow the user to specify the character used for the pattern.
=========================================
Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.
"""

# Function to print the triangle pattern
def print_triangle(rows):
    # Outer loop: Controls the rows
    for i in range(1, rows + 1):
        # Print an asterisk 'i' times for the current row
        print('*' * i)

# Ask the user for input
while True:
    try:
        # Prompt for the number of rows
        rows = int(input("Enter the number of rows for the pattern: "))

        # Ensure the input is a positive number
        if rows <= 0:
            print("Oops! Please enter a positive integer.")
            continue  # Go back to asking the user

        # Call the function to print the triangle pattern
        print_triangle(rows)
        break  # Exit the loop after printing the pattern

    # Handle invalid numeric input
    except ValueError:
        print("Oops! That wasn't a number. Please try again.")
