# 4. Create a Vector class

# Ask for help in understanding this.
# Create a class called Vector
# Define its initialiser so that it takes in a list of numbers as an argument
# Create an instance of the vector
# Define the __repr__ magic method to define what is printed when we print the object
# Define how you add two vector objects together
# Define how you index an item in a vector
# Define how to compare whether it is greater than another vector using a greater than (>) sign (use Pythagoras theorem). Use the method you defined in the question above


class Vector:
    def __init__(self, numbers): 
        self.numbers = numbers 

    def __repr__(self): # magic method
        return f"{self.numbers}" # define what is printed when we print the object

    def __add__(self, other): 
        '''
        other: another vector object
        '''
        return Vector([self.numbers[i] + other.numbers[i] for i in range(len(self.numbers))]) # create an instance of the vector class

    def __getitem__(self, index): 
        return self.numbers[index] # index an item in a vector

    def __gt__(self, other):
        return sum([i**2 for i in self.numbers]) > sum([i**2 for i in other.numbers]) # compare whether it is greater than another vector using a greater than (>) sign (use Pythagoras theorem)

# create an instance of the vector class
vector_1 = Vector([1, 2, 3])
print(f"{vector_1}, is the vector, {vector_1.__gt__(Vector([1, 2, 3]))}, is the comparison of the vector to another vector")