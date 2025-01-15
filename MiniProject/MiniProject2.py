# Ask the user up to what number they want to play

max_number = input("Enter the maximum number to play up to: ")
max_number = int(max_number)
#
# Play FizzBuzz from 1 to the chosen number
for number in range(1, max_number + 1):
    # Check if number is divisible by both 3 and 5
    
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Check if number is divisible by 3
    elif number % 3 == 0:
        print("Fizz")
    # Check if number is divisible by 5
    elif number % 5 == 0:
        print("Buzz")
    # If not divisible by 3 or 5, print the number
    else:
        print(number)
