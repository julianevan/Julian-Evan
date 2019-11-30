"""
Replace the contents of this module docstring with your own details
Name: Julian Evan
Date started: 28/11/2019
GitHub URL:
"""
from operator import itemgetter
def main():
    FILM_DICTIONARY = []
    """..."""
    print("Movies To Watch 1.0 - by Julian")
    file = open("movies.csv",'r')
    print("5 movies loaded")
    while True:
        choice = str(input("Menu: \n"
          "L - List movies \n"
          "A - Add new movie \n"
          "W - Watch new movie \n"
          "Q - Quit"))
        choice.upper()
        if choice == "L":
            for i in range(1,6):
                film = file.readlines()
                FILM_DICTIONARY = FILM_DICTIONARY + film
                FILM_DICTIONARY.sort(key=itemgetter(1))
                print(i,FILM_DICTIONARY[i-1][0],FILM_DICTIONARY[i-1][1],FILM_DICTIONARY[i-1][2],FILM_DICTIONARY[i-1][3])
        if choice == "A":
            while True:
                title = str(input("Title:"))
                year_released = int(input("Year:"))
                genre = str(input("Category:"))
                print(title, genre, "from", year_released, "added to movie list")
        if choice == "W":
            while True:
                num_of_choice= int(input("Enter the number of a movie to be watched"))
                if num_of_choice == "1":
                elif num_of_choice == "2":
                elif num_of_choice == "3":
                elif num_of_choice == "4":
                elif num_of_choice == "5":
                else:
                    print("Invalid input. ")



if __name__ == '__main__':
    main()
