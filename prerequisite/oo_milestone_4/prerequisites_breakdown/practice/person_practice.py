# Practice
class Person:
    def __init__(self, name, date_of_birth, friends):
        self.name = name
        self.date_of_birth = date_of_birth
        self.friends = friends
    
    def __str__(self):
        return f"{self.name}, {self.date_of_birth}, {len(self.friends)}"

    def __gt__(self, other):
        return self.date_of_birth > other.date_of_birth

    def add_friend(self, other):
        self.friends.append(other)
        other.friends.append(self)


# file path: 
# prerequisite/oo_milestone_4/prerequisites_breakdown/practice/person_practice.py