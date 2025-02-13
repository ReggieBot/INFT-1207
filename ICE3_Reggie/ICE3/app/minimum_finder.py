# Reggie Brown
# 29/01/2025
# ICE 2 
# Prof. Patel
# Desc: This program will read a set of 
# elements from the user and then prints the smallest
# Github: https://github.com/ReggieBot/INFT-1207/tree/main/MiscProjects

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
    
    # if the list is empty, print an error message
    except ValueError:
        print("Error: Empty list")
        return None
    
# main program
# try:
#      # get the list of numbers from the user
#      print("Enter numbers separated by spaces: ")
#      user_input = input()

#      # checks if the user input is empty
#      if user_input.strip() == "":
#          raise ValueError("Error: Empty input")

#      # split the user input into a list of separate numbers
#      input_values = user_input.split()

#      # list to store valid numbers (integers)
#      valid_numbers = []

#      # iterate through the list of numbers to check if they are integers
#      for num in input_values:
#          try: 
#              valid_numbers.append(int(num))
#          except ValueError:
#              raise ValueError(f"Error: {num} is not an integer")
        
#          # Call the find_minimum function to find the smallest number
#      minimum = find_minimum(valid_numbers)
#      if minimum != None:
#          print(f"The smallest number is: {minimum}")

# except ValueError:
#     print("Error: Invalid input")