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


#main routine
print()
print("⬆️⬆️⬆️ Welcome to the Higher Lower Game ⬇️⬇️⬇️")
#testing loop
want_instructions = yes_no("do you want to read the instruction ").lower()

#display the instructions
if want_instructions == "yes":
    instructions()

print()
print("program continues ")