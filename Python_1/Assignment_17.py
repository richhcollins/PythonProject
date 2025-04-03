"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 17
Challenge: Ensure that the function works correctly with tuples of different lengths.
=============================================
Description: Create a function called     concat_tuples that takes two tuples as input and returns a new tuple containing all elements from both input tuples.
"""

"""
Goal for this program is to take two input tuples and return a new tuple containing all elements from both tuples, 
in the order they are provided.
"""

import random
import string

# Function to concatenate two tuples
def concat_tuples(input_tuple1, input_tuple2):

    # Use the + operator to concatenate the tuples
    concatenated_tuple = input_tuple1 + input_tuple2
    return concatenated_tuple

# Example usage with random input tuples of the same length
if __name__ == "__main__":
    # Specify the number of items in each tuple
    num_items = 6

    # Generate a random tuple of numbers
    tuple1 = tuple(random.randint(1, 100) for _ in range(num_items))

    # Generate a random tuple of letters
    tuple2 = tuple(random.choice(string.ascii_letters) for _ in range(num_items))

    # Display the random tuples
    print("Random Tuple 1 (Numbers):", tuple1)
    print("Random Tuple 2 (Letters):", tuple2)

    # Call the function and print the result
    result = concat_tuples(tuple1, tuple2)
    print("\nConcatenated Tuple:", result)
