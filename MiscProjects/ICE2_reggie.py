# Reggie Brown
# 29/01/2025
# ICE 2 
# Prof. Patel
# Desc: This program will read a set of 
# elements from the user and then prints the smallest

# Checks if the input can be converted to an int

# Function finds the smallest number in a list
def find_minimum(numbers):
    try:
        # if the list is empty, raise an error
        if len(numbers) == 0:
            raise ValueError("Error: Empty list")
        
        # set
