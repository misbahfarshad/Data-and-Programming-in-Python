# PPHA 30535
# Spring 2023
# Homework 2

# marshad
# misbahfarshad

# Due date: Sunday April 9th before midnight
# Write your answers in the space between the questions, and commit/push only 
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put 
# thought into your work.

#############

# Question 1: Write a function that takes two numbers as arguments, then
# sums them together.  If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small".  Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 4), (0, 0), (-15, -100), (5, 4)]

def goldilocks_func(a, b): 
    total = a + b
    if total > 10:
        return ("big")
    elif total == 10: 
        return("just right")
    elif total < 10: 
        return ("small")

results_list = [goldilocks_func(a, b) for a, b in start_list]
print(results_list)  


# Question 2: The following code is fully-functional, but uses a global
# variable and a local variable.  Re-write it to work the same, but using an
# argument and a local variable.  Use no more than two lines of comments to
# explain why this new way is preferable to the old way.
a = 10
def my_func():
    b = 30
    return a + b
x = my_func()

#rewrite 
def my_func(a=10):
    b = 30
    return a + b
x = my_func()

#We prefer using local variables in our functions over global variables because 
#they are easier to change. If we change a global variable we might unkonwingly affect too much. 

# Question 3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*).  It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else warn the user 
# and exit.  

#Your function should also have a keyword argument named 
# "special_chars" that defaults to True.  If the function is called with the 
# keyword argument set to False instead, then the random values chosen should
# not include special characters.  

#Create a second similar keyword argument 
# for numbers. Use one of the two libraries below.
#use ifelse, special characters = True 

import random  
import string

def password_generator(length, special_chars=True, numbers=True):
    if length < 8 or length > 16:
        print("Password length must be between 8 and 16 characters")
        return None

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if numbers else ""
    special_chars = "!@#$%^&*" if special_chars else ""
    
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars
    password = ''.join(random.choice(all_chars) for i in range(length))
    
    return password

password_length = random.randint(8, 16)
password = password_generator(password_length)

print(password)

  
# Question 4: Create a class that requires four arguments when an instance
# is created: one for the person's name, one for which COVID vaccine they
# have had, one for how many doses they've had, and one for whether they've
# ever had COVID.  Then create instances for four people:
#
# Aaron, Moderna, 3, False
# Ashu, Pfizer, 2, False
# Alison, none, 0, True
# Asma, Pfizer, 1, True
#
# Write two methods for this class, and one function:

# The first method named "get_record", which prints out a one-sentence summary
# of a specified person's records (e.g. Ashu has two doses of Phizer and...)
#
# The second method named "same_shot", which takes as an argument another person's
# record instance, and then prints whether or not the two people have the
# same kind of vaccine or not.
#
# A function named "all_data", which takes a container holding any number of these 
# instances and returns a simple list of all of their data 
# (e.g. [name, vaccine, doses, covid], [...])

class Vaxx_records:
    def __init__(self, name, vaccine, doses, covid):
        self.name = name
        self.vaccine = vaccine
        self.doses = doses
        self.covid = covid
    def get_record(self):
        if self.doses == 0:
            print(f"{self.name} has not received any vaccine")
        elif self.doses == 1:
            print(f"{self.name} has received 1 dose of {self.vaccine}")
        else:
            print(f"{self.name} has received {self.doses} doses of {self.vaccine}")
    def same_shot(self, other):
        if self.vaccine == other.vaccine:
            print(f"{self.name} and {other.name} have received the same vaccine ({self.vaccine})")
        else:
            print(f"{self.name} and {other.name} have received different vaccines ({self.vaccine} and {other.vaccine})")

def all_data(vaxx_records):
    data = []
    for record in vaxx_records:
        data.append([record.name, record.vaccine, record.doses, record.covid])
    return data

Record1 = Vaxx_records("Aaron", "Moderna", 3, False)
Record2 = Vaxx_records("Ashu", "Pfizer", 2, False)
Record3 = Vaxx_records("Alison", "none", 0, True)
Record4 = Vaxx_records("Asma", "Pfizer", 1, True)

Record1.get_record()  
Record2.get_record() 
Record3.get_record()  
Record4.get_record() 

Record2.same_shot(Record4)
Record3.same_shot(Record1)
 
vaxx_records = [Record1, Record2, Record3, Record4]
print(all_data(vaxx_records))


      

             

