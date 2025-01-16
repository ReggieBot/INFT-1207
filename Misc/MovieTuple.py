movies = [("The Room", "Tommy Wiseau", "2003", "6,000,000")]

title = input("enter the movie title: ")
director = input("enter the movie director: ")
year = input("enter year the movie was made: ")
budget = input("enter the budget of the movie: ")

new_movie = (title, director, year, budget)
print(f"Title is {new_movie[0]} and it was released in {new_movie[2]}")
movies.append(new_movie)

