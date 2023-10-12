#!/usr/bin/env python
# coding: utf-8
"""
# Finding characters in a string in Python

basic search terms to find the position of a character in a string:

"""
# find() - returns the first position in the string
string1 = "Python is fun!"
findthis = 'n'
print(f"using .find(), output: {string1.find(findthis)}")

# rfind() - returns the last position in the string
string1 = "Python is fun!"
findthis = 'n'
print(f"using .rfind(), output: {string1.rfind(findthis)}")

# index() - same as find(), but index() returns ValueError if the searched character
# is missing from the string
string1 = "Python is fun!"
findthis = 'n'
print(f"using .index(), output: {string1.index(findthis)}")

# for loop
string1 = 'Python is fun!'
findthis = 'n'
emptylist = []
for pos,char in enumerate(string1):
    if(char == findthis):
        emptylist.append(pos)
print(f"using a for-loop, output: {emptylist}")

# same thing with list comprehension:
string1 = 'Python is fun!'
findthis = 'n'
print(f"using list comprehension, output: {[pos for pos, char in enumerate(string1) if char == findthis]}")

"""
 # REGULAR EXPRESSIONS
 definition: regular expressions (or RegEx) are sequences of characters that form PATTERNS that we can search for.
 RegEx can be used to check if a string contains a specified search pattern.

 why do you care about RegEx? For example, if you search through all files in a folder, but want Python to return only a list of files that have a specific extension, or contain a specific word.

 Python's regular expressions are greedy by default: greedy search means that, in ambiguous situations, Python will match the longest string possible.

 The non-greedy search matches the shortest string possible.

 https://docs.python.org/3/library/re.html
"""

import re # RegEx module

# example of how RegEx work
# note that we use re.search() function below
# we imported re in cell above

mytext = 'The rain in Spain'
x = re.search("^The.*Spain$", mytext)
print(x)
"""
note that the output looks like this:
<re.Match object; span=(0, 17), match='The rain in Spain'>
see below what's happening

functions that allow us to search a string for a match:

- findall - returns a list containing all matches
- search - returns a match object if there is a match anywhere in the string
- split - returns a list where the string has been split at each match
- sub - replaces one or many matches with a string
"""

mytext = 'The rain in Spain'

# findall()
x = re.findall("^The.*Spain$", mytext)
print(f"findall result: {x}")

x = re.findall("Portugal", mytext)
print(f"findall result for missing word: {x}")

# re.search() if empty evaluates to False, so you can use it in if-statements
x = re.search("^The.*Spain$", mytext)
print(f"search result: {x}") # search returns a MATCH OBJECT, see two cells below

x = re.search("Portugal", mytext)
print(f"search result for missing word: {x}")

# split()
x = re.split("i", mytext)
print(f"split result: {x}")

x = re.split("i", mytext, 1)
print(f"split result, but split only at the first occurence: {x}")

# sub()
x = re.sub("Spain", "potato", mytext)
print(f"sub result: {x}")

x = re.sub('i', 'e', mytext, 3)
print(f"sub result with count parameter: {x}")

"""
re.finditer() returns an interator that enables you to loop over the regex matches
in the subject string
"""
mytext = 'The rain in Spain'
text_regex = 'i'

for m in re.finditer(text_regex, mytext):
    print(m)

"""
methods to match objects can give results into a variable. 
Here, match objects are contained in variable x:
"""
x = re.search("he", mytext)
print(x.span()) # returns the position (start,end) tuple of the first match occurence

print(x.string) # prints the string that was passed into the search function (mytext)

print(x.group()) # prints the part of the string where there was a match

print(x.start()) # returns the offset in the string of the start of the match
print(x.end()) # returns the offset character beyond the match

# you can use x.start() and x.end() to slice a string:
print(mytext[x.start():x.end()])

"""
additional matching parameters for re.search():
re.I or re.IGNORECASE
"""
mytext = "I am in love with potatoes!"
x = re.search('i', mytext, re.I)
print(x)

# re.S or re.DOTALL makes the dot match newlines
moretext = "I am in love with potatoes and, \ and tomatoes, \ and even broccoli!"
x = re.search('.and', moretext, re.S)
print(x)

# re.M or re.MULTILINE makes the ^ and $ match after and before line breaks in
# the subject string
moretext = "I am in love with potatoes and, \ and tomatoes, \ and even broccoli!"
x = re.search('and', moretext, re.M)
print(x)

# to specify more than one option, "or" them together using |
mytext = "I am in love with potatoes!"
x = re.search('i', mytext, re.I | re.M)
print(x)

"""
creating a regex object using re.compile()
this is useful if you want to use the same regular expression more than once
"""
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # assign the search string to a name
# the meaning of the string above is:
# raw string that contains:
# numbernumbernumber-numbernumbernumber-numbernumbernumbernumber
# or: 3 numbers - 3 numbers - 4 numbers


phone_num = 'My number is 415-555-4242.'
x = phone_num_regex.search(phone_num)

print(f'Searched in following string: {x.string}')
print(f'Phone number found: {x.group()}.')
print(f'start and end positions of first match are: {x.span()}.')
print(f'x.group() is a {type(x.group())}; x.span() is a {type(x.span())}.')


# grouping with parentheses

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
x = phone_num_regex.search('My number is 415-555-4242.')

print(f'x.group(1) = {x.group(1)}, {type(x.group(1))}')

print(f'x.group(2) = {x.group(2)}, {type(x.group(2))}')

print(f'x.group(0) = {x.group(0)}, {type(x.group(0))}')

print(f'x.group() = {x.group()}, {type(x.group())}')

print(f'x.groups() = {x.groups()}, {type(x.groups())}')

area_code, main_number = x.groups()
print(area_code)
print(main_number)

"""
re.fullmatch() and re.match()
both functions match the string with regular expression
re.match() matches only at the beginning
and re.fullmatch() tries to match at the end as well
"""
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mystring = 'My number is 415-555-4242.'
mynumber = '415-555-4242'

x = re.fullmatch(phone_num_regex, mystring)
print(x)
y = re.match(phone_num_regex, mystring)
print(y)

x = re.fullmatch(phone_num_regex, mynumber)
print(x)
y = re.match(phone_num_regex, mynumber)
print(y)

"""
## metacharacters

# [] - a set of characters - for example [a-d] means all letters in the alphabet
# between a and d (including a and d)
"""

text = "Fluffy is the fluffiest cat in the world!"
x = re.findall('[a-d]', text)
print(x)

"""
# . - any character, except newline; one dot = one character
# this is called the wildcard char
"""

text = 'hello'
x = re.findall("he..o", text) # meaning: search for he(ANY CHARACTER)(ANY CHARACTER)o
print(x)

y = re.findall("he.o", text) # meaning: search for he(ANY CHARACTER)o
print(y)

text = "potato"
z = re.findall("p....o", text)
print(z)

"""
# * - zero or more occurences of the preceding group/character
"""
text = "hello, hello, hello, how are you today?"
x = re.findall("he.*o", text) # search for a sequence that starts with he, followed by
                                # 0 or more (any!) characters, and ends with o
print(x)

"""
# matching zero or more with *
"""
bat_regex = re.compile(r'Bat(wo)*man')
a = bat_regex.search('The adventures of Batman')
print(a)
b = bat_regex.search('The adventures of Batwoman')
print(b)
c = bat_regex.search('The adventures of Batwowowowoman')
print(c)
"""
.* matches everything in greedy mode
.*? matches everything in non-greedy mode
"""
non_greedy_regex = re.compile(r'<.*?>')
x = non_greedy_regex.search('<To serve man> for dinner.>')
print(x)

greedy_regex = re.compile(r'<.*>')
y = greedy_regex.search('<To serve man> for dinner.>')
print(y)

"""
.* will match everything except a newline
pass re.DOTALL as a second argument to re.compile() to include newline
"""
no_newline_regex = re.compile('.*')
no_newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

newline_regex = re.compile('.*', re.DOTALL)
newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

"""
^ - starts with - the beginning of individual string
"""
text = 'hello, world!'
x = re.findall("^hello", text) # check if the string starts with "hello"
print(x)

"""
$ - ends with - the end of individual string
"""
text = 'hello, world!'
x = re.findall("world!$", text) # check if the string ends with "world!"
print(x)

"""
combine ^ and $ for full string match
"""
text = 'hello, world'
x = re.findall("^world$", text)
print(x)

text = 'world'
y = re.findall("^world$", text)
print(y)

"""
+ - one or more occurence of the preceding group/character
"""
text = "hello, world"
x = re.findall("he.+o", text)
print(x)

bat_regex = re.compile(r'Bat(wo)+man')
a = bat_regex.search('The Adventures of Batwoman')
print(a)

b = bat_regex.search('The Adventures of Batwowowowoman')
print(b)

c = bat_regex.search('The Adventures of Batman')
print(c)

"""
? - zero or one (any) character (but not two, not three, etc.)
"""
text = "hello, world"
x = re.findall("hel?o", text)
print(x)

# ? also lets you perform optional matching:
text2 = "The adventures of Batman"
y = re.search(r'Bat(wo)?man', text2)
print(y)

text3 = "The adventures of Batwoman"
z = re.search(r'Bat(wo)?man', text3)
print(z)



"""
{n} - exactly the specified (n) number of occurences
"""
text = "hello, world"
x = re.findall("he.{2}o", text) # exactly 2 characters, any character (because .)
print(x)

ha_regex = re.compile(r'(Ha){3}')
a = ha_regex.search('HaHaHa')
print(a)

b = ha_regex.search('Ha')
print(b)

"""
{n,} - n or more of the preceding group
"""
text = "helllllllo, world"
x = re.findall("hel{3,}o", text) # here preceding group/character is l
print(x)


"""
{,m} - 0 to m of the preceding group.
"""
text = "helllllllo, world"
x = re.findall("hel{,3}o", text) # here preceding group/character is l
print(x)

y = re.findall("wo{,3}rld", text)
print(y)

"""
{n,m} - at least n and at most m of the preceding p: GREEDY SEARCH
"""
text = "helllllllo, world"
x = re.findall("hel{2,4}o", text) # here preceding group/character is l
print(x)

text = "helllo, world"
x = re.findall("hel{2,4}o", text) # here preceding group/character is l
print(x)

"""
{n,m}? or *? or +? - performs a non-greedy match of the preceding p.
"""
# greedy search:
greedy_ha_regex = re.compile(r'(Ha){3,5}')
x = greedy_ha_regex.search('HaHaHaHaHa')
print(x)

# non-greedy search:
non_greedy_ha_regex = re.compile(r'(Ha){3,5}?')
y = non_greedy_ha_regex.search('HaHaHaHaHa')
print(y)

"""
 | - check if the string contains either|or
"""
text = "hello, you are my favorite potato."
x = re.search(r"hello|potato", text)
print(x)

text2 = "potato, you are my favorite hello"
y = re.search("potato|hello", text2)
print(y)

"""
you can also use pipe | to match one of several patterns as part of your regex:
"""
text = "Batmobile lost a wheel"
x = re.search(r'Bat(man|mobile|copter|bat)', text)
print(x)

x.group(0)


"""
To make your regex case-insensitive,
you can pass re.IGNORECASE or re.I as a second argument to re.compile():
"""
robocop = re.compile(r'robocop', re.I)

robocop.search('Robocop is part man, part machine, all cop.').group()
robocop.search('ROBOCOP protects the innocent.').group()
robocop.search('Al, why does your programming book talk about robocop so much?').group()

"""
\ - signals a special sequence! see special sequences below
# special sequences

\A - returns a match if the specified characters are at the beginning of the string
"""

text = "That's what I do: I drink, and I know things."
x = re.findall('\ATha', text)
print(x)

y = re.findall('\AKnow', text)
print(y)

"""
\b - returns a match where the specified characters are at the beginning or at the end
of a word; the 'r' at the beginning makes sure the string is being treated as "raw" string
raw string means that escape sequences are not parsed
for example, \n means a newline character, but r'\n\ means a backslash and n
"""
text = "That's what I do: I drink, and I know things."
x = re.findall(r"\bwh", text) # at the beginning
print(x)

y = re.findall(r"ow\b", text) # at the end of string
print(y)


"""
\B - Returns a match where the specified characters are present,
but NOT at the beginning (or at the end) of a word
"""
text = "That's what I do: I drink, and I know things."
x = re.findall(r"\Brin", text) # at the beginning
print(x)

y = re.findall(r"rin\B", text) # at the end of string
print(y)

"""
\d - returns a match where the string contains digits (from 0-9)
"""
text = "And I would roll 500 miles"
x = re.findall("\d", text)
print(x)

"""
\D - returns a match where the string DOES NOT contain digits
"""
text = "And I would roll 500 miles"
x = re.findall("\D", text)
print(x)

"""
\s - Returns a match where the string contains a white space character
\S - Returns a match where the string DOES NOT contain a white space character
"""
text = "That's what I do: I drink, and I know things."
x = re.findall("\s", text)
print(x)

y = re.findall("\S", text)
print(y)

"""
\w - Returns a match where the string contains any word characters
word characters: characters from a to Z, digits from 0-9, and the underscore _ character
\W - Returns a match where the string DOES NOT
"""
text = "That's what I do: I drink, and I know things."
x = re.findall("\w", text)
print(x)

y = re.findall("\W", text)
print(y)

"""
\Z - returns a match if the specified characters are at the end of the string
"""
text = "That's what I do: I drink, and I know things."
x = re.findall("things.\Z", text)
print(x)

"""
# sets
a set is a set of characters inside a pair of [ ] with a special meaning
"""

# [abc] - a match when one of the specified characters (a, b, or c) is present
text = "That's what I do: I drink, and I know things."
x = re.findall("[ghi]", text)
print(x)


# [a-d] - a match for any alphabetically ordered letters between a-d, including capitals
text = "That's what I do: I drink, and I know things."
x = re.findall("[g-j]", text)
print(x)

# [^abc] - returns a match for any character except a, b, and c

text = "That's what I do: I drink, and I know things."
x = re.findall("[^ghj]", text)
print(x)

# [0123] - returns a match where any of the specified digits are present
text = "And I would roll 500 miles"
x = re.findall("[015]", text)
print(x)

# [0-9] - returns a match for any digit between 0 and 9

text = "And I would roll 500 miles"
x = re.findall("[0-4]", text)
print(x)


# [0-5][0-9] - returns a match for any two-digit number from 00 to 59

text = "And I would roll 500 miles"
x = re.findall("[0-5][0-5]", text)
print(x)

# [a-zA-Z] - returns a match for any character alphabetically between a and z lower OR upper case

text = "And I would roll 500 miles"
x = re.findall("[a-zA-Z]", text)
print(x)


# [+] - return any match for any + character in the string
text = "And I would roll 500 miles + more"
x = re.findall("[+]", text)
print(x)

# we can also use + to repeat iterations, for example:

y = re.findall("[l]+", text)
print(y)

"""
# managing complex regexes
"""
# incomprehensible:

email_regex = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))')

mydata = "Aleksandra Kaszowska, email: kaszowska@es.aau.dk"
x = re.search(email_regex, mydata)
print(x)

# easy to read:

email_regex = emailRegex = re.compile(r'''(
     [a-zA-Z0-9._%+-]+               # username
      @                              # @ symbol
     [a-zA-Z0-9.-]+                  # domian name
     (\.[a-zA-Z]{2,4})               # dot-something
     )''', re.VERBOSE) # pass re.VERBOSE to the second argument of re.compile()

mydata = "Aleksandra Kaszowska, email: kaszowska@es.aau.dk"
x = re.search(email_regex, mydata)
print(x)

