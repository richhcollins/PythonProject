"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 5
Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.
=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.
"""

# User input
hours = input("Enter time duration in hours: ")

# Processing with conditions
try:
    hours = float(hours)
    if hours < 0:
        print("\033[1;31mTime duration cannot be negative.\033[0m")
    else:
        print(f"\033[1;32mTime duration: {hours * 60:.0f} minutes or {hours * 3600:.0f} seconds\033[0m")
except ValueError:
    print("\033[1;31mInvalid input. Please enter a number.\033[0m")


