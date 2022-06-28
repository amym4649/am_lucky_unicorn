show_instructions = ""

while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    # If they say yes, output 'programme continue'
    if show_instructions == "yes":
        print("Programme continue")

    elif show_instructions == "y":
        print("Programme continue")

    # If they say no, output 'display instructions'
    elif show_instructions == "no":
        print("Display instructions")

    elif show_instructions == "n":
        print("Display instructions")

    else:
        print("Please input either 'yes' or 'no'.")


