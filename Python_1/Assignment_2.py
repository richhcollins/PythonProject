'''
Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.
=================================
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
Output: Display the calculated area of the rectangle.
'''

# Define variables with conditions
def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("\033[91mSorry! You need to enter a positive number.\033[0m")
            else:
                return value
        except ValueError:
            print("\033[91mSorry, input denied! Please enter a positive number (not a letter or special character).\033[0m")

# Positive number input in feet
length = get_number("Please enter the rectangle length (in feet): ")
width = get_number("Please enter the rectangle width (in feet): ")

# Rectangle area calculation
area = length * width

# Display results in blue
print("The rectangle area is (in square feet): \033[94m{:.0f}\033[0m".format(area))