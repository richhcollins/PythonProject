"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 16
Challenge: Optimize the function to handle large input lists efficiently.
==============================
Description: Develop a function called     find_common_elements that takes two lists as input and returns a new list containing elements that are common to both input lists.
"""

# Goal for this program is to generate two random input lists with the desired number of items each to compare
import random

# Function to find common elements between two lists
def find_common_elements(list1, list2):

    # Convert the lists to sets for efficient operation
    set1 = set(list1)
    set2 = set(list2)

    # Perform intersection operation to find common elements
    common_elements = set1.intersection(set2)

    # Return the result as a sorted list for better readability
    return sorted(list(common_elements))

if __name__ == "__main__":

    # Specify the desired number of elements in each list
    num_items = 25  # Adjust this value for different sizes

    # Generate two random lists of the same size
    list1 = random.sample(range(1, 100), num_items)
    list2 = random.sample(range(50, 150), num_items)

    # Display the random lists
    print("Random List 1:", list1)
    print("Random List 2:", list2)

    # Call the function and print the result
    result = find_common_elements(list1, list2)
    print("\nCommon elements:", result)
