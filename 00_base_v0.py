"""
Base component for the game 'lucky_unicorn'
v0 - skeleton script

author - Amy Macpherson
CC AM 2022
"""

# import libraries below this line **********


# all functions below this line ********
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If they say no, output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please input either 'yes' or 'no'.")


def instructions():
    print("* * * How to play * * *")
    print()
    print("These are the rules")
    print()
    return ""


def num_checker(question, low, high):

    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            if low < response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


# main routine below this line *********
played_before = yes_no("Have you played the game before? ")

print()

print("You chose {}".format(played_before))

print()

if played_before == "no":
    instructions()

# Ask how much they want to play with
response = num_checker("How much do you want to play with?", 0, 10)

print()

print("You are playing with ${}, continue with the game.\n".format(response))


