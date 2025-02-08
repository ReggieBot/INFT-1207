# INFT-1207
# LAB 2 - Test Case Design
# 07/02/25
# Reggie Brown | reggie.brown@dcmail.ca
# Wren Bailey | wren.bailey@dcmail.ca
# This program allows a user to add, search, and view their current reading list

import csv


#def add_book():

# function to add book to the csv


#def list_books():

# function to get all books from csv and display to user

def search_books():

    # method to search for book from title
    searching_title = input("\nPlease enter the title of the book you'd like to search for: ")
    # remove whitespace
    searching_title.strip()

    try:
        file = open("books.csv", "r")
        reader = csv.reader(file)

        # for loop to check if searching_title matches book title (first index)
        # Strips and lowercases both variables to account for different cases
        book_found = False
        for row in reader:
            if row and row[0].strip().lower() == searching_title.lower():
                print("-- Book Details --")
                print("Title: ", row[0])
                print("Author: ", row[1])
                print("Year: ", row[2])
                book_found = True
                
        # close the csv file
        file.close()

        if book_found == False:
            print ("\nCould  not find that book")

    except FileNotFoundError:
        print("\nNo books added!")


def main():

    # Infinite while loop to keep the program menu running. Exit clause is triggered when user chooses to exit program
    while True:
        print("-- Welcome To Your Personal Reading List --")
        print("1. Add book")
        print("2. List all of your books")
        print("3. Search for book")
        print("4. Exit program")

        user_choice = input("\nPlease select an option (1-4): ")

        if user_choice == "1":
            add_book()
        elif user_choice == "2":
            list_books()
        elif user_choice == "3":
            search_books()
        elif user_choice == "4":
            print("Exiting Program.")
            break
        else:
            print("Error. Please select a number from 1-4")


if __name__ == '__main__':
    main()
