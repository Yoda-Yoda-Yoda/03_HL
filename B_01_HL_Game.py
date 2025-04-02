import math
import random


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
end_game = "no"
game_history = []

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


if num_rounds == "":
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

    print()
    print(rounds_heading)
    print()
    secret = random.randint(low_num, high_num)
    guesses_allowed = calc_guesses(low_num, high_num)
    guesses_used = 0
    already_guessed = []

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:
        print(f"The secret number is {secret}")

        if guesses_used == guesses_allowed - 1:
            print(
                "💣💣💣 Careful - You only have one bomb left to explode to find the hidden number in the mountain or you will die☠️💀☠️")

        guess = int_check("Guess: ", low_num, high_num, "xxx")

        if guess == "xxx":
            end_game = "yes"
            break

        if guess in already_guessed:
            print(f"You've already guessed {guess}. You've *still* used "
                  f"{guesses_used} / {guesses_allowed} guesses ")
            continue

        else:
            already_guessed.append(guess)

        guesses_used += 1

        if guesses_used == guesses_allowed and guess == secret:
            feedback = "🍀🍀🍀Yay you didn't die on your last Guess🍀🍀🍀"

        elif guesses_used == guesses_allowed and guess != secret:
            break

        elif guess < secret:
            feedback = f"❄️❄️❄️Too low, please try a higher number❄️❄️❄️. You've used {guesses_used} / {guesses_allowed}"

        elif guess > secret:
            feedback = f"🔥🔥🔥You picked a number TOO high🔥🔥🔥. You've used {guesses_used} / {guesses_allowed}"

        else:
            feedback = f"😀😀😀Well done!!! You Guessed the secret Number😀😀😀. You've used {guesses_used} / {guesses_allowed}"
            game_history.append(f"Round {rounds_played + 1} - 😃😃😃 Well Done. You guessed the secret number which was {secret} and you got it in {guesses_used} / {guesses_allowed }😃😃😃")
        # history_item = f"Round:  {rounds_played + 1}  -  {feedback}"
        print(feedback)
        # game_history.append(history_item)

    if end_game == "yes":
        break

    if guess != secret:
        print("💀💀💀 You have Died 💀💀💀")
        game_history.append(f"Round {rounds_played + 1} - ❗❗❗You have used all of you BOMBS❗❗❗, you failed to guess the secret number which was {secret}!")

    rounds_played += 1


    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game History / statistics area
if rounds_played > 0:

    see_history = yes_no("Do you want to see your game history?  ")

    if see_history.lower() == "yes" or see_history.lower() == "y":
        print("🎮🎮🎮 Game History 🎮🎮🎮")

        for item in game_history:
                print(item)

        print()
        print("Thanks for playing")

else:
    # print a statement if that user selected infinite mode and didn't play any rounds!!!
    print("🐔🐤🐥🐔 Oops! You chickens out and didn’t play any rounds🐔🐤🐥🐔 ")


