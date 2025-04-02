"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 13
Challenge: Use a loop structure to compare characters from both ends of the string to determine whether it is a palindrome.
===================================
Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
"""

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Normalize the string by converting it to lowercase and removing spaces
    s = s.lower().replace(" ", "")

    # Use two pointers: one starting at the beginning and the other at the end
    left = 0
    right = len(s) - 1

    # Loop to compare characters from both ends
    while left < right:
        if s[left] != s[right]:  # If characters don't match, it's not a palindrome
            return False
        left += 1  # Move the left pointer to the right
        right -= 1  # Move the right pointer to the left

    # If all characters matched, it's a palindrome
    return True

# Prompt the user to enter a string
user_input = input("Enter a string to check if it is a palindrome: ")

# Check the string and display the result
if is_palindrome(user_input):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")
