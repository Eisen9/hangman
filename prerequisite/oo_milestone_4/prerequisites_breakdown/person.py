# 5. Create a Class called Person

# Create a class called Person
# Define its initialiser
# It must take in a name, a date_of_birth in ISO format (YYYY-MM-DD), and a list of friends
# It should initialise attributes for each of those. Be careful, don't use a default value for friends! This will cause problems whenever you initialise a new instance of the class. To know more about, take a look at this link 
# Instantiate your class and test that it works before continuing - do this for every section going forward
# Define the __str__ magic method which returns a string representation of the person, detailing their name, DOB and number of friends
# Define the __gt__ magic method that defines how to use the greater than sign to compare the age of two people (hint: Compare the DOB of the two people)
# Create a method called add_friend, which takes in another instance of the person class and adds it to this instance's friends attribute. Assume that every relationship goes both ways: this method should append each friend to the other's list, in just one call

class Person:
    def __init__(self, name, date_of_birth, friends):
        self.name = name
        self.date_of_birth = date_of_birth
        self.friends = friends

    def __str__(self):
        return f"{self.name} is {self.date_of_birth} and has {len(self.friends)} friends"

    def __gt__(self, other):
        return self.date_of_birth > other.date_of_birth

    def add_friend(self, other):
        self.friends.append(other) # append each friend to the other's list
        other.friends.append(self) # append each friend to the other's list (in just one call)


# instantiate the Person class
person_1 = Person("John", "1990-01-01", ["Jane", "Jack"])
person_2 = Person("Jane", "1991-01-01", [])
print(person_1)