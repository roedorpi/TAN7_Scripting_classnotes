#!/usr/bin/env python
# coding: utf-8

"""
OBJECT-ORIENTED PROGRAMMING

what is object-oriented programming? It is a method of structuring a program by grouping related properties and behaviors into individual objects.

Python is an object-oriented language: this means that, at its very core, Python stores all information in classes and objects. Except for control flow, everything in Python is an object.

In this lesson, we are taking a peek under the hood. Understanding OOP will help you see the world as a programmer does. It'll help you know your code, not just what's happening line by line, but also the bigger concepts behind it.

important concepts:

classes: a class is a blueprint for creating an object. When you write (or: define) a class, you define the general behavior that a whole category of objects can have; a function that is part of a class is called a method.

objects: an object is an individual representation of a class. When you create individual objects from the class, each object is automatically equipped with the general behavior; you can then give each object whatever unique traits you desire.

An object could represent a dog with properties like a name and age, and behaviors such as sitting or rolling over. An object could also represent an email with properties like a recipient list, subject, and body, and behaviors like adding attachments or sending. Object-oriented programming is an approach for modeling concrete things and the relations between those things. OOP models those things as software objects that have some data associated with them, and can perform certain functions.

instantiation: making an object from a class; we say "to instantiate an object". That object then is called an instance of a class.

"""
# Each instance created from the Dog class will store a name and an age, and
# we’ll give each dog the ability to sit() and roll_over():

class Dog:
    """constructor"""
    # global attributes
    legs = 4
    species = "Canine"

    def __init__(self, name='NoName', age=0):
        # instance attributes
        self.name = name
        self.age = age

    def print_info():
        # functions accessible only by the class
        print("This is a class for making dogs")

    def how_many_legs(self):
        # use self to access global attributes
        print(f"{self.species}s have {self.legs} legs.")

    def sit(self):
        # Simulate a dog sitting in response to a command.
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        # Simulate rolling over in response to a command.
        print(f"{self.name} rolled over!")


# %%

# making an instance from a class:
my_dog = Dog('Hotdog', 6)

# accessing attributes:
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# calling methods:
my_dog.sit()

# %%
# ### creating multiple instances:


my_dog = Dog('Hotdog', 6)
your_dog = Dog('ScoobyDoo', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.\n")

my_dog.sit()
your_dog.roll_over()


# %%
# ## inheritance


# we are creating a child class called HuntingDog.
# HuntingDog is a child class to Dog (defined previously)

class HuntingDog(Dog):
    """Represents aspects and skills of a dog specific to hunting dogs."""

    def __init__(self, name, age):
        """initialize attributes of the parent class"""
        super().__init__(name, age)


# testing if inheritance is working correctly:
# instantiate child class
my_hunting_dog = HuntingDog('Rocket', '3')
print(f"My dog's name is {my_hunting_dog.name}.")
print(f"My dog is {my_hunting_dog.age} years old.")

my_hunting_dog.sit()


# %%

class HuntingDog(Dog):
    """Represents aspects and skills of a dog specific to hunting dogs."""
    def __init__(self, name, age):
        """First, initialize attributes of the parent class.
        Second, initialize attributes specific to hunting dog."""
        super().__init__(name, age)
        self.hunting_experience = 0

    def describe_experience(self):
        """print statement explaining dog's hunting experience in years.
        This is a getter funtion that returns instance parameter values"""
        print(f"This dog has {self.hunting_experience} years of hunting experience.")

    def set_experince(self, experience):
        """This is a setter function changing instance parameter values."""
        self.hunting_experience += experience
        print(f"This dog has now {self.hunting_experience} years of hunting experience.")
    def roll_over(self):
        """this function changes the roll_over function defined in the parent class"""
        print(f"{self.name} has been rolling over for {self.hunting_experience} years!!")
    def __call__(self):
        """ make the instances of the class callable, so they can be used as functions"""
        print(f"{self.name} go get the bird!")


my_hunting_dog = HuntingDog('Rocket', '3')
my_hunting_dog.describe_experience()
my_hunting_dog.set_experince(4)
my_hunting_dog.roll_over()
my_hunting_dog()

