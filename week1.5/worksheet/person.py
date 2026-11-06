# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    def __init__(self, name, birth):
            """
            Creates and initializes the fields name and birth of a person.
            """

            if not isinstance(name, str):
                  raise TypeError("Name must be a string.")
            
            if name == "":
                  raise ValueError("Name cannot be an empty string.")
            
            if not isinstance(birth, date):
                  raise TypeError("Birth must be a date.")

            self.name = name
            self.birth = birth
                  
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
          """
          Return the uppercased initial letters of each part of a person’s name, joined together into a single string.
          """
          parts = self.name.split()
          initials = ""

          for part in parts:
                initials += part[0].upper()

          return initials

    def is_birthday(self):
          """
          Checks if today is the person's birthday
          """

          today = date.today()

          return today.day == self.birth.day and today.month == self.birth.month

