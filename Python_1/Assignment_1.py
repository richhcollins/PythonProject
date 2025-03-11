'''
Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 1
Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.
=============================
Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
Output: Display the calculated simple interest.
'''

# Input section
principal = float(input("Enter the principal amount (dollars): "))
rate = float(input("Enter the interest rate (percentage): "))
time = float(input("Enter the time period (years): "))

# Processing section
simple_interest = (principal * rate * time) / 100

# Output section
# print("The calculated simple interest is: ", simple_interest)
print("The simple interest is: \033[91m{:.2f}\033[0m".format(simple_interest))