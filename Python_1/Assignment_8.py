"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 8
Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.
=================================================
Input: Ask the user to enter their marks for three subjects.
Processing: Calculate the average of the marks. Determine the grade based on the average:
90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F
Output: Display the calculated grade.
"""

# Function to check if the entered grade is valid
def get_grade(subject_name):
    while True:
        try:
            grade = float(input(f"Enter grade for {subject_name}: "))
            if grade >= 0 and grade <= 100:
                return grade
            print("Grades should be between 0 and 100. Please try again.")
        except:
            print("Invalid input. Please enter a number.")

# Main program
print("\nEnter your grade for three subjects.\n")

# Get grades for each subject
math = get_grade("Math")
english = get_grade("English")
science = get_grade("Science")

# Calculate the average grades
average_grades = (math + english + science) / 3

# Determine the grade based on average
if average_grades >= 90:
    grade = "A"
elif average_grades >= 80:
    grade = "B"
elif average_grades >= 70:
    grade = "C"
elif average_grades >= 60:
    grade = "D"
else:
    grade = "F"

# Display results
print("\nYour average grade is:", round(average_grades))
print("Your grade is:", grade)