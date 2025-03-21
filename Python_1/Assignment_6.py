"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Assignment 6
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.
==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.
"""

# Define exchange rate from USD to EUR
exchange_rate = 0.92

def convert_amount():

    # User input
    while True:
        try:
            amount_usd = float(input("Enter the amount in USD: "))
            if amount_usd <= 0:
                print("Please enter a positive amount.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    # Convert USD to EUR
    amount_eur = amount_usd * exchange_rate

    # Output the result
    print(f"${amount_usd:.2f} USD is equal to €{amount_eur:.2f} EUR.")

# Call the function
convert_amount()

