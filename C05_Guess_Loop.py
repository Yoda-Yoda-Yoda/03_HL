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


# Guessing Loop

secret = 7

low_num = 0
high_num = 10
guesses_allowed = 5

guesses_used = 0
already_guessed = []

guess = ""
while guess != secret and guesses_used < guesses_allowed:

    if guesses_used == guesses_allowed - 1:
        print("💣💣💣 Careful - You only have one bomb left to explode to find the hidden number in the mountain or you will die☠️💀☠️")

    guess = int_check("Guess: ", low_num, high_num)

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

    print(feedback)



if guess != secret and guesses_used == guesses_allowed:
    print("💀💀💀 You have Died 💀💀💀")
