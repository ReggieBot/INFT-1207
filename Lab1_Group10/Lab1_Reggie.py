# Reggie Brown
# 23/01/2024
# Lab 1 - Group 10
# Prof. Patel
# Desc: This program wll generate a random password based on user defined requirements

import random
import string

def generate_password(totalLength, numSpecial, numDigits, numLetters):
    
    # Basic validation for input
    if totalLength < 8 or totalLength > 16:
        return "Password length must be between 8 and 16 characters"
    
    # Checks that at least one category has characters
    if numLetters == 0 and numDigits == 0 and numSpecial == 0:
        return "Error: Password must contain at least one character of a type"
    
    # Checks remaining available characters after eac;h user input 
    remainingLength = totalLength - numLetters

    if remainingLength < 0:
        return (f"Error: Letters must be between 0 - {totalLength}")
    
    if numDigits < 0 or numDigits > remainingLength:
        return (f"Error: Digits must be between 0 - {remainingLength}")
    
    remainingLength = remainingLength - numDigits
    
    if numSpecial < 0 or numSpecial > remainingLength:
        return (f"Error: Special characters must be between 0 - {remainingLength}")
    
    # Assigns the possible characters for each type
    # Uses the String module to get possible characters
    letters = string.ascii_letters 
    digits = string.digits
    specialChars = string.punctuation

    # Generates the password
    password_characters = (
        random.choices(letters, k = numLetters) +
        random.choices(digits, k = numDigits) +
        random.choices(specialChars, k = numSpecial)
    )
    
    # Shuffles the password
    random.shuffle(password_characters)

    # joins the password characters into a string, and returns it
    password = ''.join(password_characters)
    return password
    
def main():
    # header
    print("Welcome to Reggie's password generator!")
    print("This program will generate a random password based on YOUR requirements!")

    # try except for input validation
    # added while loop to repromp user
    while True:
        try:
            # user input
            totalLength = int(input("\nEnter the total length of the password (8-16): "))
            numLetters = int(input("Enter the number of letters in the password: "))
            numDigits = int(input("Enter the number of digits in the password: "))
            numSpecial = int(input("Enter the number of special characters in the password: "))

            # calls the generate_password function
            password = generate_password(totalLength, numSpecial, numDigits, numLetters)

            # prints the generated password
            print(f"\nYour new randomly generated password is: {password}")

            # breaks if successful password in generated
            break 

        except ValueError:
            # error message for invalid input (non-integer)
            print("\nError: Please enter a valid integer")

# calls the main function
main()

