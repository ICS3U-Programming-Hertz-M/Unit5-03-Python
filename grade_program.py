#!/usr/bin/env python3

# Created by: Hertz
# Created on: May,10 2022.
# This program asks the user to enter their grade level and determines the middle percentage
# of that level
# then displays it to the user.


def calc_mark(grade):
    if grade == "4+":
        return "97.5%"
    elif grade == "4":
        return "90.5%"
    elif grade == "4-":
        return "83%"
    elif grade == "3+":
        return "78%."
    elif grade == "3":
        return "74.5%"
    elif grade == "3-":
        return "71%"
    elif grade == "2+":
        return "68%"
    elif grade == "2":
        return "64.5%"
    elif grade == "2-":
        return "61%"
    elif grade == "1+":
        return "58%"
    elif grade == "1":
        return "54.5%"
    elif grade == "1-":
        return "51%"
    elif grade == "R":
        return "less than 50"
    else:
        return "-1"


def main():
    # get user level.
    user_level = input("Enter your level : ")
    print("")

    # assigns a variable to function call, giving it a returned value.
    percentage = calc_mark(user_level)

    print("Level {} has a percentage of {}.".format(user_level, percentage))


if __name__ == "__main__":
    main()
