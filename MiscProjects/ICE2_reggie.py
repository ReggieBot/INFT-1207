# Reggie Brown
# 29/01/2025
# ICE 2 
# Prof. Patel
# Desc: This program will read a set of 
# elements from the user and then prints the smallest

# Checks if the input can be converted to an int

# function finds the smallest number in a list
def find_minimum(numbers):
    try:
        # if the list is empty, raise an error
        if len(numbers) == 0:
            raise ValueError("Error: Empty list")
        
        # set the first number in the list to the smallest
        smallest = numbers[0]

        # iterate through the list to find smallest
        for number in numbers:
            if number < smallest:
                smallest = number
        
        # returns the smallest number 
        return smallest
    
    except ValueError:
        print("Error: Empty list")
        return None
    
