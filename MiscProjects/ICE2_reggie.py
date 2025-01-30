# Reggie Brown
# 29/01/2025
# ICE 2 
# Prof. Patel
# Desc: This program will read a set of 
# elements from the user and then prints the smallest

# Checks if the input can be converted to an int
def is_int(value):
    try:
        int(value)
        return True
    # if value cannot be converted to int, return False
    except ValueError:
        return False

# function to find smallest number in list  
def find_minimum(numbers):

    