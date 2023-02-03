# Python Libraries

# Libraries are reusable chunks of code that are imported- tend to be premade methods and functions
# Base libraries are libraries that are in built, they still have to be imported though
#Import whole library
#import random
# When importing a whole library, need to specify what package from the library in your code
#print(random.random())

# Import a specific method from the library
from random import random


print(random()) # Output = Random float

import math

num_float = 23.66

print(math.ceil(num_float))
print((math.floor(num_float)))
print(math.pi)