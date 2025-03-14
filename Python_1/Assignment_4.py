'''Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 4
Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.
============================================
Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points.
'''

# Collect the coordinates of two points
x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))

# Calculate the distance of two coordinates
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Display results
print(" ")
print(f"The distance between the coordinates of [(x1={x1:.0f},y1={y1:.0f}) & (x2={x2:.0f},y2={y2:.0f})] = {distance:.2f}")
