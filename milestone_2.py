import random
word_list = ['apple', 'orange', 'kiwi', 'pineapple', 'cherry']
# print(word_list)

word = random.choice(word_list)
# print(word)
############################################################
# TASK 4

guess = input("Enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

############################################################
# TASK 5
# upload to GitHub