"""
Exercises session 04.

Make a program that can read questions from a text file, present these questions to a user and save responses into a csv
file.

The program has to:
    1. run until it receives the instructions from the user to stop.
    2. avoid crashing if the question or response file are not found or can't be opened
    3. register and answer and response time for each answer
    4. after the questionnaire is compleat it should print the average score (or calculate a result) for the individual
    as well as the average for all respondents in the answer file.

"""
# Hint: Start with the SUS_evaluation.py script for inspiration.
# Hint: use try -- execpt conditionals to avoid program crashes in file operations.
# Hint: open question file in read mode and csv file in append mode.
# Hint: for response time look at the time and datetime libraries.

## we need to include some extra functionality through libraries.
import time  # to get the current time in seconds since 1,Jan,1970
import csv   # functionality for csv files
import sys   # operating system, used to terminate program in case of error
import os.path as path  # operating systems file commands used to check if a file exists.

## load questions from file. The file I am opening is a csv file but I am reading it like a normal text files. Remember
# csv files are just text files with a specific structure.
try:
    quest_file = open('SUS_EN_DK.csv', mode="r", newline="\n") # the new line character is used in the file.
except FileNotFoundError:
    print('The file specified does not exist.')
    sys.exit(0)  # this is from the sys library used to terminate the program.
else:
    sus = quest_file.readlines() # read the entire file as a list of strings, one string for each line.
    sus = sus[1:] # the first line in the file are the headers, so we eliminate them.
    quest_file.close() # once you are done reading close the file.

## open the response file
# First we check if the file exists:
if path.isfile('SUS_responses.csv'): # using the isfile method from the os.path library if the file exists set a flag.
    resp_file_exists = True
else:
    resp_file_exists = False
# try to open or create the file
try:
    resp_file = open('SUS_responses.csv', mode='a', newline="")
except: # if the open command fails... for whatever reason.
    print('Could not create or open the response file... exiting the program')
    sys.exit(0)  # stop program execution and exit the program
else: # the file was opened correctly so we initialize the csv writer from the csv library
    # here we are also giving the fieldnames for the csv file, each row of a csv.DicWriter is a dictionary with keys
    # given in the parameter fieldnames.
    resp_file_writer = csv.DictWriter(resp_file, delimiter=";", fieldnames=['id', 'question', 'rating', 'resp_time'])
    if not resp_file_exists: # if this is the first time the file is opened write the headers for the csv file.
        resp_file_writer.writerow({'id': 'Subject ID', 'question': 'SUS question', 'rating': 'Rating',
                                   'resp_time': 'Response Time'})
##
print("System usability scale.")
print("This program allows you to evaluate a system using the 10 questions from the SUS.\n"
      "You should indicate how much you agree or disagree with each statement with a number between 1 and 5, \n "
      "where 1 is strongly disagree and 5 is strongly agree, and 3 is neutral. ")

while True: # keep the program running until the user enters "no"
    name = input('What is your name? ')

    for question in sus: # loop through the list of questions
        quest = question.split(';') # each line contains an english and a danish version of the statement.
        tstart = time.time() # start the timer for the response time using the time library
        try:    # collect the answer
            answer = int(input(quest[1]+' :'))
        except ValueError: # it cannot convert the string to a number...
            print('You must enter a number not a character, start again')
            break # stops the for loop and goes out to the while loop.
        else:
            if answer > 5 or answer < 1: # check that the values given are valid.
                print('You must enter a number between 1 and 5, start again')
                break  # stop the for loop...
            tstop = time.time() # get the time of the answer
            # write the name, the statement, the answer and the response time in seconds.
            resp_file_writer.writerow({'id': name, 'question': quest[1], 'rating': answer, 'resp_time': tstop - tstart})
    # we have finished the list of statements, should there be more respondents?
    if input('More subjects (yes/no)?').strip().lower() == 'no':
        break
# we are finished collecting data, close response file
resp_file.close()

# goodbye message.
print("Thanks for participating!")

# now lets process the data that we gathered
print("Processing the data now: ")
# lets open the response file for reading
try:
    respf = open('SUS_responses.csv', mode="r")
except FileNotFoundError:
    print('The file specified does not exist.')
    sys.exit(0)
else:
    results = respf.readlines() # read all lines.
    results = results[1:] # the first line in the file are the headers, so we eliminate them.
    respf.close() # close the file, we don't need it anymore.

# initialize necessary variables.
EveQ = 0 # sum of even statements
OddQ = 0 # sum of odd statements
used_time = 0.0 # sum of used time
ScaleSteps = 5 # number of steps in answer scale
Answers = {} # dictionary to gather the answers
allratings = [] # list of individual results
alltimes = [] # list of individual response times

# loop through the results. Here I am purposely using an index that starts with one. This is so that the odd and even
# questions are treated properly. This is because every 10 statements we change to a new subject, so to avoid changin
# to the next subject in the first iteration of the loop (0%10 == 0).
for i in range(1, len(results)+1):
    values = results[i-1].split(';') # get results from first line
    used_time += float(values[3]) # add the time used
    if i % 2 == 0: # even statements are negative, so we invert the skale. 1 becomes 4 and 5 becomes 0
        EveQ += ScaleSteps - int(values[2])
    else: # odd statements are positive, subtract one from values so results go from 0 to 4.
        OddQ += int(values[2]) - 1
    if i % 10 == 0: # when we reach the 10th statement we prepare for a new subject, calculate the result and reset
        # temporary variables.
        # save the answers in the Answers dictionary using subject name as the key.
        Answers[values[0]] = [(EveQ + OddQ)/((ScaleSteps-1)*10)*100, used_time] # SUS rating and time used
        allratings.append(Answers[values[0]][0]) # save the results from all subjects in a list
        alltimes.append(Answers[values[0]][1]) # save the times from all subjects in a list
        # reset temporary variables used for adding up the results.
        EveQ = 0
        OddQ = 0
        used_time = 0
# Add the average results to the answers as a new entry with the key Average.
Answers['Average'] = [sum(allratings)/len(allratings), sum(alltimes)/len(alltimes)]

# print the results obtained.
print(Answers)

# Checking the results... if you answer all 10 statements 1, 3 or 5 then the results should be 50.
# if you answer all odd statements with 5 and all even statements with 1 then the results should be 100.
# if you answer all odd statements with 1 and all even statements with 5 then the results should be 0.
