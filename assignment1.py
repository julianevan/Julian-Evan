"""
Replace the contents of this module docstring with your own details
Name: Julian Evan
Date started: 28/11/2019
GitHub URL:
"""
from operator import itemgetter


def main():
    watched_counter = 0
    watched_movies = 0
    unwatched_movies = 0
    FILM_LIST = []
    authentication_list = []
    """..."""
    print("Movies To Watch 1.0 - by Julian")
    file1 = open("movies.csv", 'r')
    file1 = file1.readlines()
    FILM_LIST = FILM_LIST + file1
    authentication_list = authentication_list + file1
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
    print(len(FILM_LIST), "movies loaded")
    while True:
        file1 = open('movies.csv', 'r')
        choice = str(input("Menu: \n"
                           "L - List movies \n"
                           "A - Add new movie \n"
                           "W - Watch new movie \n"
                           "Q - Quit"))
        if choice.upper() == "L":
            file = open('movies.csv', 'r')
            file = file.readlines()
            FILM_LIST = []
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
                if FILM_LIST[i - 1][3] == 'w':
                    print(i, " {:<34}-{:>5}({})".format(FILM_LIST[i - 1][0], FILM_LIST[i - 1][1], FILM_LIST[i - 1][2]))
                    watched_movies += 1
                    lines = ("{}{}{}{}\n".format(FILM_LIST[i - 1][0], FILM_LIST[i - 1][1], FILM_LIST[i - 1][2],
                                             FILM_LIST[i - 1][3]))
                    authentication_list.append(lines)
                else:
                    print(i, "*{:<34}-{:>5}({})".format(FILM_LIST[i - 1][0], FILM_LIST[i - 1][1], FILM_LIST[i - 1][2]))
                    unwatched_movies += 1
                    lines = ("{}{}{}{}\n".format(FILM_LIST[i - 1][0], FILM_LIST[i - 1][1], FILM_LIST[i - 1][2],
                                             FILM_LIST[i - 1][3]))
                    authentication_list.append(lines)
            print(watched_movies, "movies watched,", unwatched_movies, "movies still to watch")
            watched_movies = 0
            unwatched_movies = 0
            file1.close()
        elif choice.upper() == "A":
            title = str(input("Title:"))
            try:
                year_released = int(input("Year:"))
            except ValueError or year_released < 0:
                print("Invalid input, please enter a number which is positive")
            try:
                genre = str(input("Category:"))
            except genre.isnumeric():
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
                if FILM_LIST[num - 1][3] == "w":
                    watched_counter += 1
                    if watched_counter == len(FILM_LIST):
                        print("All films watched!")
            else:
                film_choice = int(input("Please enter a number for a film to be watched"))
                if FILM_LIST[int(film_choice) - 1][3] == "w":
                    print("You have already watched the film")
                else:
                    FILM_LIST[film_choice - 1][3] = "w"
                    file = open("movies.csv", 'w+')
                    for i in range(1, (len(FILM_LIST)) + 1):
                        FILM_LIST.sort(key=itemgetter(1))
                        if FILM_LIST[i - 1] == FILM_LIST[film_choice - 1]:
                            file_replacement = (
                                "{},{},{},w".format(FILM_LIST[film_choice - 1][0], FILM_LIST[film_choice - 1][1],
                                                    FILM_LIST[film_choice - 1][2]))
                            with open("movies.csv", 'a+') as file:
                                file.write(file_replacement)
                                authentication_list.append(file_replacement)
                        else:
                            file = open("movies.csv", "a+")
                            file_line = file.readlines()
                            with open("movies.csv", 'a+') as file:
                                line = ("{},{},{},{}".format(FILM_LIST[i - 1][0], FILM_LIST[i - 1][1],
                                                             FILM_LIST[i - 1][2], FILM_LIST[i - 1][3]))
                                file.write(line)
                                authentication_list.append(line)
                    print(FILM_LIST[film_choice - 1][0], "from", FILM_LIST[film_choice - 1][1], "watched")
                    file.close()
        elif choice.upper() == "Q":
            file4 = open('movies.csv', 'r')
            file4 = file4.readlines()
            authentication_list = []
            authentication_list = authentication_list + file4
            for i in range(1, (len(FILM_LIST) + 1)):
                content_split = authentication_list[i - 1].split(",")
                authentication_list[i - 1] = content_split
            file4 = open("movies.csv", 'w+')
            with open("movies.csv", 'a+') as file4:
                for i in range(1, (len(FILM_LIST)) + 1):
                    lines = ("{},{},{},{}".format(authentication_list[i - 1][0], authentication_list[i - 1][1],
                                                  authentication_list[i - 1][2], authentication_list[i - 1][3]))
                    file4.write(lines)
            print(len(FILM_LIST), "movies saved to movies.csv")
            print("Have a nice day :)")
            file4.close()
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
