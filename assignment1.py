"""
Replace the contents of this module docstring with your own details
Name: Julian Evan
Date started: 28/11/2019
GitHub URL:
"""


def main():
    """..."""
    print("Movies To Watch 1.0 - by Julian")
    file = open("movies.csv",'r')
    print("5 movies loaded")
    choice = str(input("Menu: \n"
          "L - List movies \n"
          "A - Add new movie \n"
          "W - Watch new movie \n"
          "Q - Quit"))
    choice.upper()
    if choice == "L":
        while i > 5:
            for line in file:
                if 
                print("{:<10s}")

    elif choice == "A":
    elif choice == "W":
    elif choice == "Q":
    else:
        print("Invalid input")
        choice = str(input("Menu: \n"
                           "L - List movies \n"
                           "A - Add new movie \n"
                           "W - Watch new movie \n"
                           "Q - Quit"))

if __name__ == '__main__':
    main()
