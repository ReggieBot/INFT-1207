# Get employee information from user
name = input("Enter employee name: ")
wage = input("Enter hourly wage: $")
hours = input("Enter hours worked this week: ")

# Process the name - remove extra spaces and convert to title case
clean_name = name.strip().title()

# Convert wage and hours to floating point numbers

wage_float = float(wage)
hours_float = float(hours)

# Calculate total earnings
total_earnings = wage_float * hours_float

# Display results
print("\nEmployee Payment Summary")
print("Name:", clean_name)
print("Hourly Wage: ${:.2f}".format(wage_float))
print("Hours Worked: {:.2f}".format(hours_float))
print("Total Earnings: ${:.2f}".format(total_earnings))
