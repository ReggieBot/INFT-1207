# Reggie Brown
# In class exercise 1
# Professor Patel
# 15/01/25
# reggie.brown@dcmail.ca
# https://github.com/ReggieBot/INFT-1207/MiscProjects/ICE1_reggie.py

movies = [
("Eternal Sunshine of the Spotless Mind", 20000000),
("Memento", 9000000),
("Requiem for a Dream", 4500000),
("Pirates of the Caribbean: On Stranger Tides", 379000000),
("Avengers: Age of Ultron", 365000000),
("Avengers: Endgame", 356000000),
("Incredibles 2", 200000000)
]

numberOfMovies = int(input("How many movies would you like to add to the list? "))

# gets user input for new movies including name/budget, and appends them
for movieCount in range(numberOfMovies):
    name = input("Enter name of the new movie ")
    budget = float(input("Enter the budget of the new movie: "))
    movies.append((name, budget))

# calculates the average budget of all movies 
for movie in movies:
    budgetTotal = budgetTotal + movie[1]
averageBudget = budgetTotal / len(movies)

print(f"The average budget of the movies is {averageBudget:,.2f}")

# finds what movies are over average budget

highBudgetMovies = 0
for movie in movies:
    if movie[1] > averageBudget:
        budgetDifference = movie[1] - averageBudget
        # print the movie and exceeded budget to terminal
        print(f"{movie[0]} cost = ${movie [1]}")
        print(f"This exceeded the average budget by: ${budgetDifference}")
        highBudgetMovies + highBudgetMovies + 1