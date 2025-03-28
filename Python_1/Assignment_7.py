"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 7
Challenge: Handle cases where the user enters non-numeric input for the year and provide appropriate error messages.
===============================================
Input: Prompt the user to enter a year.
Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
Output: Display whether the entered year is a leap year or not.
"""


def leap_year(year):
    # Check leap year conditions
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def function():
    while True:
        try:
            # Prompt user for input
            user_input = input("Please enter a year: ")
            year = int(user_input)  # Attempt to convert input to integer

            # Validate that the year is not negative
            if year < 0:
                print("Error: You must enter a positive numeric year.")
                continue

            # Determine if it's a leap year and display the result
            if leap_year(year):
                print(f"{year} is a leap year!")
            else:
                print(f"{year} is not a leap year.")

            while True:
                # Ask if user wants to continue
                continue_choice = input("Do you want to check another year? (Y or N): ")
                if continue_choice in ["Y", "N"]:
                    break  # Valid input, exit loop
                else:
                    print("Error: Please answer with 'Y' or 'N'.")  # Reject, invalid input

            if continue_choice == "N":
                print("See you next time!")
                break
        except ValueError:
            # Handle alpha input
            print("Error: You must enter a valid numeric year.")

# Run the program
function()

