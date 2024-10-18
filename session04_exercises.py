"""
Exercises session 04.

Make a program that can read questions from a text file, present these questions to a user and save responses into a csv
file.

The program has to:
    1. run until it receives the instructions from the user to stop.
    2. avoid crashing if the question or response file are not found or can't be opened
    3. register and answer and response time for each answer
    4. after the questionnaire is complet it should print the average score (or calculate a result) for the individual
    as well as the average for all respondents in the answer file.

"""
# Hint: Start with the SUS_evaluation.py script for inspiration.
# Hint: use try -- execpt conditionals to avoid program crashes in file operations.
# Hint: open question file in read mode and csv file in append mode.
# Hint: for response time look at the time and datetime libraries.

# we need to include some extra functionality through libraries.
import time  # to get the current time in seconds since 1,Jan,1970
import csv   # functionality for csv files
import sys   # operating system, used to terminate program in case of error
import os.path as path  # operating systems file commands used to check if a file exists.

##
# Checking the results... if you answer all 10 statements 1, 3 or 5 then the results should be 50.
# if you answer all odd statements with 5 and all even statements with 1 then the results should be 100.
# if you answer all odd statements with 1 and all even statements with 5 then the results should be 0.
