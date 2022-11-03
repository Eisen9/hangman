# hangman
Tasks implemented as prompted. Find in `milestone_2.py`, `milestone_3.py`, `milestone_4.py` and `milestone_5.py`.

*Note: comments (where appropriate) are provided for the details of implementaion in each of the milestone files.*

--------------------------------------------------------------------------------
## Milestones Explained

### Milestone 1
Note that there is no file named `milestone_1.py` in this repository, this is becuase milestone 1 is concerned with setting up the GitHub repository -- no conding tasks invloved.

---------
### Milestone 2
#### Task 1
 This file will contain the code for the first milestone (`milestone_2.py`). In Python, Lists are used to store multiple data in a single variable. In this task, we are creating a list of words; assigning this list to a variable; printing out the vale of the variable to the screen.

#### Task 2
Using the random module. The random module is one of Python's built-in modules. It has a choice method which returns a random item from a given sequence.

#### Task 3
In this task, we are required to take user input. As we now know, the print() function in Python displays output on the screen. Conversely, Python has an input() function that takes input from the screen. Note that the input function returns the user input in form of a string.

#### Task 4
Usually, when taking input from users, it is best to validate that the input makes sense. For example, we may want to ensure that only a single letter is entered and that only alphabetical characters are provided by the user. To do this, we create conditional checks that must be passed before the input can be accepted.

---------
### Milestone 3
Check if the guessed character is in the word.
#### Task 1
Check if the user input is an alphabet and that the length of the input is 1 character.

Inside a while loop that has a condition of `True`, take the user input and assign it to a variable.
If the user input is alphabet and one character, exit the loop, otherwise, prompt the user to satisfy the conditions (alpha and single character).

#### Task 2
Consider the user input that we took from the user in Task 1, then create a varaible that holds a value of *secret word*. If the guess of the user contains a character that is included in the secret word, we print that character and notify the user that they had guessed it right. Otherwise, we print the gussed character and notfiy the user that they had guessed it wrong.

#### Task 3
Two functions are created in this task: `check_guess` and `ask_for_input`.
Consider what we did in Task 2, this time, we want to wrap our code from Task 2 inside a fuction called `check_guess` which takes the guess (user input) as an argument. This function also converts the user input to a lower case upon receiving it.

The `ask_for_input` function asks the user for a letter. 
If the letter is not a single alphabetical character, it asks the user to enter a single alphabetical character.
If the letter is already guessed, it asks the user to enter a different letter.
If the letter is valid, it calls the check_guess method.

---------
### Milestone 4
In this milestone, we create a Hangman class. Details of the class:

 '''
    Hangman is a game where the user has to guess a word by guessing the letters in the word.
    The game is over when the number of lives is 0 or the number of letters left to guess is 0.

    Parameters:
        @param word_list: a list of words to choose from
        @param num_lives: the number of lives the user has; default is 5

    Attributes:
        word: the word to guess
        word_guessed: the word with the letters guessed
        num_letters: the number of letters left to guess
        num_lives: the number of lives left
        word_list: the list of words to choose from
        list_of_guesses: the list of letters guessed

    Methods:
        check_guess: checks if the guess is in the word and updates the word_guessed.

        ask_for_input: asks the user for a letter and calls the check_guess method.

    '''

---------
### Milestone 5
This milestone is a continuation of milestone_4 with the addidtion of the following function:
`play_game`. Details of function:
This function plays the game.
    if the number of lives is 0, that means that the has lost the game.
    if the number of lettters is greater than 0, keep asking the user for the input
    if the number of lives is not 0 and the number of letters is not greater than 0, that means that the user has won the game.

    Parameters:
        @param word_list: a list of words to choose from






