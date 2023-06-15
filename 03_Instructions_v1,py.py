

# Functions go here...
def yes_no(question):...


def instructions():...


# Main Routine goes here...
show_instructions = yes_no("Have you played the game before")

if show_instructions == "yes":
    instructions()
else:
    print("Program Continues")