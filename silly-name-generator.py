#Load a list of first names
#Load a list of surnames
#Choose a first name at random
#assign the name to a variable
#Choose a surname at random

import random


firstnames = ['James', 'Robert', 'John', 'Michael', 'William', 'David', 'Patricia', 'Mary', 'Jennifer', 'Linda', 'Elizabeth']

surnames = ['Richard', 'Joseph', 'Thomas', 'Charles', 'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Mark', 'Donald']

firstname = random.choice(firstnames)
surname = random.choice(surnames)

print(firstname + " " + surname)