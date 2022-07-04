# Function
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


# Main routine
response = num_checker("How much do you want to play with?", 0, 10)

print("You are playing with ${}, continue with the game.\n".format(response))
