show_instructions = ""

while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    # If they say yes, output 'programme continue'
    # Use 'or' statement to combine
    if show_instructions == "yes" or show_instructions == "y":
        print("Programme continue")

    # If they say no, output 'display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("Display instructions")

    else:
        print("Please input either 'yes' or 'no'.")


