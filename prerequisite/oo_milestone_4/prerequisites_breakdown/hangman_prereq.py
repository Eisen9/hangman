#1 Create Your own game of Hangman

class Hangman:
    def __init__(self, word): # Constructor method for the class Hangman
        self.word = word # The word to be guessed by the player 
        self.guessed = [] # The letters that have been guessed
        self.guesses = 0 # The number of guesses the player has made
        self.max_guesses = 6 # The maximum number of guesses the player can make
        self.game_over = False # Whether the game is over or not
        self.won = False # Whether the player has won or not
        self.word_guessed = [] # The word to be guessed with the letters that have been guessed filled in
        self.word_guessed = ["_"] * len(self.word) # Create a Hangman object with the word "hangman"

    def guess(self, letter): # The method that is called when the player guesses a letter 
        if self.game_over == False: # If the game is not over 
            self.guesses += 1 # Increment the number of guesses the player has made
            self.guessed.append(letter) # Add the letter to the list of guessed letters
            if letter not in self.word: # If the letter is not in the word
                print("Incorrect") # Print "Incorrect"
            else:
                print("Correct") # Otherwise print "Correct"
                self.update_word_guessed(letter) # Update the word to be guessed with the letter
            self.print_word() # Print the word to be guessed
            self.print_guessed() # Print the letters that have been guessed
            self.print_guesses() # Print the number of guesses the player has made
            self.check_win() # Check if the player has won
            self.check_loss() # Check if the player has lost
    
    def update_word_guessed(self, letter): # The method that updates the word to be guessed with the letter
        for i in range(len(self.word)): # For each letter in the word
            if letter == self.word[i]: # If the letter is the same as the letter in the word
                self.word_guessed[i] = letter # Create a Hangman object with the word "hangman"

    def print_word(self): # The method that prints the word to be guessed
        print("Word: ", end="") # Print "Word: "
        for letter in self.word_guessed: # For each letter in the word to be guessed
            print(letter, end=" ") # Print the letter
        print()


    def print_guessed(self): # The method that prints the letters that have been guessed
        print("Guessed: ", end="") # Print "Guessed: "
        for letter in self.guessed: # For each letter in the list of guessed letters
            print(letter, end=" ") # Print the letter
        print() 

    def print_guesses(self): # The method that prints the number of guesses the player has made
        print("Guesses: " + str(self.guesses) + "/" + str(self.max_guesses)) # Print the number of guesses the player has made and the maximum number of guesses the player can make

    def check_win(self): # The method that checks if the player has won the game
        if "_" not in self.word_guessed: # If there are no more underscores in the word to be guessed
            self.game_over = True # Set the game over variable to True
            self.won = True # Set the won variable to True
            print("You won!") # Create a Hangman object with the word "hangman"

    def check_loss(self): # The method that checks if the player has lost the game
        if self.guesses >= self.max_guesses: # If the number of guesses the player has made is greater than or equal to the maximum number of guesses the player can make
            self.game_over = True # Set the game over variable to True
            self.won = False # Set the won variable to False
            print("You lost!") 

    def play(self): # The method that is called when the player wants to play the game
        while self.game_over == False: # While the game is not over
            letter = input("Enter a letter: ") # Ask the player to enter a letter
            self.guess(letter) # Call the guess method with the letter the player entered

# Create a game
game = Hangman("apple") # Create a Hangman object with the word "apple"
game.play() # Call the play method
