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
    
    # Checks remaining available characters after eac;h user input 
    remainingLength = totalLength - numLetters

    if remainingLength < 0:
        return (f"Error: Letters must be between 0 - {totalLength}")
    
