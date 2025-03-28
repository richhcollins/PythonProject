"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 10
Challenge: Implement error handling to ensure that the user enters a positive integer for the age.
==================================
Input: Prompt the user to enter their age.
Processing: Classify the age into different categories:
Under 18: Minor
18-65: Adult
Above 65: Senior citizen
Output: Display the category based on the entered age.
"""

# User input
while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            break
        print("Age must be a positive number. Try again.")
    except:
        print("Invalid input! Please enter a number.")

# Age category determination
if age < 18:
    print("You are a Minor.")
elif age <= 65:
    print("You are an Adult.")
else:
    print("You are a Senior citizen.")