#!/usr/bin/env python
# coding: utf-8


# Each instance created from the Dog class will store a name and an age, and
# we’ll give each dog the ability to sit() and roll_over():

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
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
        """print statement explaining dog's hunting experience in years."""
        print(f"This dog has {self.hunting_experience} years of hunting experience.")


my_hunting_dog = HuntingDog('Rocket', '3')
my_hunting_dog.describe_experience()

