import math


def int_check(question, low=None, high=None, exit_code=None):

    if low is None and high is None:
        error = "Please enter an integer"

    elif low is not None and high is None:
        error = (f"Please enter an integer the is "
                 f"more than / equal to {low}")

    else:
        error = (f"Please enter an integer the "
                 f"is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            if low is not None and response < low:
                print(error)

            elif high is not None and response > high:
                print(error)

            else:
                return response


        except ValueError:
            print(error)


def yes_no(question):
    """checks user response to a question is yes/no (y/n), returns 'yes' or 'no'"""
    while True:



        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":

            return "no"
        else:
            print("enter yes/no")


def instructions():
    """PRINTS INSTRUCTIONS"""

    print('''
**** Instructions ****

To begin, choose the number of rounds and either customise 
the game parameters or go with the default game (where the 
secret number will be between 1 and 100).

Then choose how many rounds you'd like to play <enter> for 
infinite mode.

Your goal is to try to guess the secret number without 
running out of guesses.

Good Luck!!!
    ''')


def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0


print()
print("⬆️⬆️⬆️ Welcome to the Higher Lower Game ⬇️⬇️⬇️")
print()

want_instructions = yes_no("Do you want to read the instruction ").lower()

#display the instructions
if want_instructions == "yes":
    instructions()
# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode:  ",
                       low=1, exit_code="")


if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5



low_num = int_check("Low Number?  ")
high_num = int_check("High Number?  ", low=low_num+1)
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️Round {rounds_played + 1} (Infinite Mode)♾️♾️♾️"

    else:
        rounds_heading = f"\n📀💿📀 Rounds {rounds_played + 1} of {num_rounds}💿📀💿"

    print(rounds_heading)
    user_choice = input("Chose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1


    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game History / statistics area
