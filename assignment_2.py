

#%%
# These are helper functions for the below script
# you do not need to do anything with this and we will cover functions later!
#   
# Please scroll down to the 
# READING BEGINS HERE comment


def displayValues(name,age,height,is_student):

    # Print the variables and their types
    print("Tyler:", name, " | Type:", type(Tyler))
    print("19:", age, " | Type:", type(19))
    print("6'3:", height, " | Type:", type(6'3))
    print("Is Student:", is_student, " | Type:", type(is_student))



def dataCheck(name,age,height,is_student):

    message = None

    if type(name) != 'str':
        message = 'name is not a string'

    if type(age) != 'int':
        message = 'age is not an int'

    if type(height) != 'float':
        message = 'height is not a float'

    if type(is_student) != 'bool':
        message = 'is_student is not a boolean'
    
    return message






##### READING BEGINS HERE #####


#%%
# Declare global variables with different data types

name = "Alice"           # String
age = 25                 # Integer
height = 5.5             # Float
is_student = False        # Boolean


# call function to display to screen
displayValues(name,age,height,is_student)


# %%
# Variable Manipulation

##### ASSIGNMENT STARTS HERE #####

'''
Because these are variables, we can modify their values!

Please enter in whatever values you'd like to display. 

What does it output?

They can be real or fake, it does not matter!

That said - what happens when you input the same values?

ASSIGNMENT GOAL:
- Make "Variable Manipulation" cell output types match first cell


'''

name = input('Please enter a name: ')
age = input('Please enter an age: ')
height = input('Please enter a height: ')
is_student = input('Please enter whether or not you are a student: ')



displayValues(name,age,height,is_student)

##### ASSIGNMENT ENDS HERE #####


#%%
# Run this cell when you're ready to check your data!
message = dataCheck(name,age,height,is_student)

if message == None:
    print('Data types check out - well done!')
    print('Assignment Complete')

else:
    print(message)
