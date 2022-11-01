import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        self.guess = guess.lower()
        if self.guess in self.word:
            print(f"Good guess {self.guess} is in the word")
            for letter in self.word: # loop through each letter in the word
                if letter == guess: # check if the letter is equal to the guess
                    self.word_guessed = letter # replace the "_" with letter in the word_guessed
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

        # append the guess to the list_of_guesses
        self.list_of_guesses(guess)

    
    def ask_for_input(self):
        while True:
            guess = input("Guess the letter: ")
            if guess.isalpha() != 1: 
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # handle the logic here
                self.check_guess(guess)
                self.list_of_guesses.append(guess) # add the guess to the list of guesses
                break 


# create an instance of the object Hangman and call the ask_for_input method to test.

hangman_1 = Hangman("apple")
hangman_1.ask_for_input()
