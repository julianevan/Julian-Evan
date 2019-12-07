"""
Replace the contents of this module docstring with your own details
Name: Julian Evan
Date started: 28/11/2019
GitHub URL:
"""
from operator import itemgetter
def main():
    watched_counter = 0 #(Choice W) To count how much movies have been watched
    watched_movies = 0 #(CHOICE L) Watched movies counter
    unwatched_movies = 0 #(CHOICE L) Unwatched movies counter
    FILM_LIST = [] #Empty list for films
    """..."""
    print("Movies To Watch 1.0 - by Julian")
    file1 = open("movies.csv", 'r')
    file1 = file1.readlines()
    FILM_LIST = FILM_LIST + file1 #to add file1 to FILM_LIST
    for i in range(1, (len(FILM_LIST) + 1)):
        content_split = FILM_LIST[i - 1].split(",") #splitting content from comma delimiter
        FILM_LIST[i - 1] = content_split
        FILM_LIST[i - 1][1] = int(FILM_LIST[i - 1][1])
    FILM_LIST.sort(key=itemgetter(1)) #sorting list by year
    for x in FILM_LIST: #removing \n
        if x[3] == "w\n":
            x[3] = "w"
        elif x[3] == "u\n":
            x[3] = "u"
    print(len(FILM_LIST), "movies loaded")
    while True:
        file = open('movies.csv','r')
        file = file.readlines()
        FILM_LIST = []
        FILM_LIST = file
        for i in range(1, (len(FILM_LIST) + 1)):
            content_split = FILM_LIST[i - 1].split(",")  # splitting content from comma delimiter
            FILM_LIST[i - 1] = content_split
            FILM_LIST[i - 1][1] = int(FILM_LIST[i - 1][1])
        FILM_LIST.sort(key=itemgetter(1))  # sorting list by year
        for x in FILM_LIST:  # removing \n
            if x[3] == "w\n":
                x[3] = "w"
            elif x[3] == "u\n":
                x[3] = "u"
        choice = str(input("Menu: \n"
                           "L - List movies \n"
                           "A - Add new movie \n"
                           "W - Watch new movie \n"
                           "Q - Quit"))
        if choice.upper() == "L":
            file = open('movies.csv', 'r')
            file = file.readlines()
            FILM_LIST = [] #emptying the film_list
            FILM_LIST = FILM_LIST + file
            for i in range(1, (len(FILM_LIST) + 1)):
                content_split = FILM_LIST[i - 1].split(",")
                FILM_LIST[i - 1] = content_split
                FILM_LIST[i - 1][1] = int(FILM_LIST[i - 1][1])
            FILM_LIST.sort(key=itemgetter(1))
            for x in FILM_LIST:
                if x[3] == "w\n":
                    x[3] = "w"
                elif x[3] == "u\n":
                    x[3] = "u"
            for i in range(1, (len(FILM_LIST) + 1)):
                if FILM_LIST[i - 1][3] == 'w': #if the fourth element is w
                    print(i, " {:<34}-{:>5}({})".format(FILM_LIST[i - 1][0], FILM_LIST[i - 1][1], FILM_LIST[i - 1][2]))
                    watched_movies += 1
                else: #if the fourth element is u
                    print(i, "*{:<34}-{:>5}({})".format(FILM_LIST[i - 1][0], FILM_LIST[i - 1][1], FILM_LIST[i - 1][2]))
                    unwatched_movies += 1
            print(watched_movies, "movies watched,", unwatched_movies, "movies still to watch")
            watched_movies = 0 #reset the counter
            unwatched_movies = 0
        elif choice.upper() == "A":
            title = str(input("Title:"))
            try:
                year_released = int(input("Year:"))
            except ValueError or year_released < 0: #if ValueError occurs or year_released is negative
                print("Invalid input, please enter a number which is positive")
            try:
                genre = str(input("Category:"))
            except genre.isnumeric(): #if there is a number
                print("Invalid input, please enter a category of a movie")
            new_film = ("{},{},{},u\n".format(title, year_released, genre))
            with open("movies.csv", 'a+') as file:
                file.write(new_film)
                print(title, "(", genre, "from", year_released, ") added to movie list")
            file = open("movies.csv",'r+')
            file = file.readlines()
            FILM_LIST = []
            FILM_LIST = FILM_LIST + file
            for i in range(1, (len(FILM_LIST) + 1)):
                content_split = FILM_LIST[i - 1].split(",")
                FILM_LIST[i - 1] = content_split
        elif choice.upper() == "W":
            for num in range(1, len(FILM_LIST) + 1):
                if FILM_LIST[num - 1][3] == "w": #add 1 to watch_counter if fourth element is w
                    watched_counter += 1
                    if watched_counter == len(FILM_LIST): #if watched_counter equals length of authentication_list
                        print("All films watched!")
            else:
                film_choice = int(input("Please enter a number for a film to be watched"))
                if FILM_LIST[int(film_choice) - 1][3] == "w": #if the fourth element is w
                    print("You have already watched the film")
                else:
                    FILM_LIST[film_choice - 1][3] = "w" #change the fourth element to w
                    file = open("movies.csv", 'w+') #overwrite the csv file
                    for i in range(1, (len(FILM_LIST)) + 1):
                        if FILM_LIST[i - 1][0] == FILM_LIST[film_choice - 1][0]: #if the counter suits the film_choice
                            file_replacement = (
                                "{},{},{},w\n".format(FILM_LIST[film_choice - 1][0], FILM_LIST[film_choice - 1][1],
                                                      FILM_LIST[film_choice - 1][2]))
                            with open("movies.csv", 'a+') as file:
                                file.write(file_replacement)
                            FILM_LIST.append(file_replacement)
                        else:
                            with open("movies.csv", 'a+') as file:
                                line = ("{},{},{},{}\n".format(FILM_LIST[i - 1][0],FILM_LIST[i - 1][1],
                                                             FILM_LIST[i - 1][2], FILM_LIST[i - 1][3]))
                                file.write(line)
                            FILM_LIST.append(line)
                    print(FILM_LIST[film_choice - 1][0], "from", FILM_LIST[film_choice - 1][1], "watched")
                    file.close()
        elif choice.upper() == "Q":
            file4 = open('movies.csv', 'r')
            file4 = file4.readlines()
            FILM_LIST = []
            FILM_LIST = FILM_LIST + file4
            print(len(FILM_LIST), "movies saved to movies.csv")
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