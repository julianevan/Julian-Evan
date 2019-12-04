"""
Replace the contents of this module docstring with your own details
Name: Julian Evan
Date started: 28/11/2019
GitHub URL:
"""
from operator import itemgetter
import csv
def main():
    number_detector = 0
    watched_counter = 0
    film_counter = 0
    FILM_LIST= []
    """..."""
    print("Movies To Watch 1.0 - by Julian")
    file = open("movies.csv",'r')
    file = file.readlines()
    FILM_LIST = FILM_LIST + file
    for i in range(1, (len(FILM_LIST) + 1)):
        content_split = FILM_LIST[i - 1].split(",")
        FILM_LIST[i - 1] = content_split
        FILM_LIST[i - 1][1] = int(FILM_LIST[i - 1][1])
    FILM_LIST.sort(key=itemgetter(1))
    print(len(FILM_LIST), "movies loaded")
    while True:
        choice = str(input("Menu: \n"
          "L - List movies \n"
          "A - Add new movie \n"
          "W - Watch new movie \n"
          "Q - Quit"))
        if choice.upper() == "L":
            for i in range(1,(len(FILM_LIST))+1):
                if FILM_LIST[i-1][3] == "w":
                    print(i, "* {:<34}-{:>7}({})".format(FILM_LIST[i-1][0],FILM_LIST[i-1][1],FILM_LIST[i-1][2]))
                else:
                    print(i ,"  {:<34}-{:>7}({})".format(FILM_LIST[i-1][0],FILM_LIST[i-1][1],FILM_LIST[i-1][2]))
        elif choice.upper() == "A":
            title = str(input("Title:"))
            try:
                year_released = int(input("Year:"))
            except ValueError or year_released < 0:
                print("Invalid input, please enter a number")
            try:
                genre = str(input("Category:"))
            except genre.isnumeric():
                print("Invalid input, please enter a category of a movie")
            new_film = ("{},{},{},u".format(title,year_released,genre))
            with open("movies.csv",'a') as file:
                file.write(new_film)
            print(title,"(",genre, "from", year_released,") added to movie list")

        elif choice.upper() == "W":
            for num in range(1, len(FILM_LIST) + 1):
                if FILM_LIST[num - 1][3] == "w":
                    film_counter += 1
            if film_counter == len(FILM_LIST):
                print("All films watched!")
            else:
                while True:
                    film_choice = int(input("Please enter a number for a film to be watched"))
                    if FILM_LIST[film_choice-1][3] == "w":
                        print("You have already watched the film")
                    else:
                        FILM_LIST[film_choice-1][3] = "w"
                        
                        print(FILM_LIST[film_choice-1][0], "from", FILM_LIST[film_choice-1][1], "watched")
        elif choice.upper() == "Q":
            file = open("movies.csv",'r')
            file = file.readlines()
            FILM_LIST = file
            print(len(FILM_LIST),"movies saved to movies.csv")
            print("Have a nice day :)")
            quit()
        else:
            choice = str(input("Menu: \n"
                      "L - List movies \n"
                      "A - Add new movie \n"
                      "W - Watch new movie \n"
                      "Q - Quit"))
main()




if __name__ == '__main__':
    main()
