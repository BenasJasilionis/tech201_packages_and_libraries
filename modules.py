# Modules- piece of software that delivers some sort of functionality
# Difference between module and library- module is referencing a file, libraries are multiple files and folders
import os
import math, datetime, sys

working_directory = os.getcwd()
print(working_directory)

def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.name())


print(datetime.date.today())  # Output = 2023-02-03 ( 3rd of feb)

print((sys.path))             # Output = shows where you are in your machine , double brackets not neccessary, just best practice to show that module doesn't take arguments, but that it still does do something

print(math.remainder(1, 5))

# Methods and libraries allow you to do things in one line of code, whereas normally it would take much more code
# When you are building a program, it's really important to think whether you need to make a class/object or simply a function. You may not even need to make a function yourself if there is a module that does whar you are looking for already.

# Built in functions

# print()
# len()
# type()