# functions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

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


# Main routine
played_before = yes_no("Have you played the game before? ")

print("You chose {}".format(played_before))
print()

if played_before == "no":
    instructions()

print("Continue")



