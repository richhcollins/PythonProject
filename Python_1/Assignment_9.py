"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 9
Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.
=====================================================
Input: Ask the user to enter a single character.
Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
Output: Display whether the entered character is a vowel or a consonant.
"""

# Check for vowel or consonant
while True:
    char = input("Enter a letter: ")
    if len(char) == 1 and char.isalpha():
        if char.lower() in "aeiou":
            print(f"{char} is a vowel.")
        else:
            print(f"{char} is a consonant.")
        break
    else:
        print("Invalid input! Please enter a single letter.")