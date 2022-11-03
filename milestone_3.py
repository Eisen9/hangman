import random
# Task 1
while True:
    guess = input("Guess a letter: ")
    if guess.isalpha() and len(guess) == 1:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

####################################################################################################
# Task 2

secret_word = "apple"
if guess in secret_word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")


####################################################################################################
# Task 3

def check_guess(guess):
    '''
    This function checks if the letter guessed is in the secret word.
    If the letter is in the secret word, it prints "Good guess! {guess} is in the word."
    If the letter is not in the secret word, it prints "Sorry, {guess} is not in the word. Try again."
    '''
    guess.lower()
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    '''
    This function asks the user for a letter. 
    If the letter is not a single alphabetical character, it asks the user to enter a single alphabetical character.
    If the letter is already guessed, it asks the user to enter a different letter.
    If the letter is valid, it calls the check_guess method.

    '''
    while True:
        guess = input("Guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)


ask_for_input()