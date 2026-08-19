import random
import os

class Hangman:

    def __init__(self, userid: str = 'subj01', num_guesses: int = 8):
        self.userid = userid
        self.num_guesses = num_guesses
        self.output_string = []
        self.randomWord = ''

    def draw_hangman(self):
        # method to draw hangman
        graphics = ['''_____\n|/  |\n|   O\n|  /|\\\n|  / \\\n|''',
                    '''_____\n|/  |\n|   O\n|  /|\\\n|  / \\\n|''',
                    '''_____\n|/  |\n|   O\n|  /|\\\n|  /\n|''',
                    '''_____\n|/  |\n|   O\n|  /|\\\n|\n|''',
                    '''_____\n|/  |\n|   O\n|  /|\n|\n|''',
                    '''_____\n|/  |\n|   O\n|   |\n|\n|''',
                    '''_____\n|/  |\n|   O\n|\n|\n|''',
                    '''_____\n|/  |\n|\n|\n|\n|''',
                    '']
        print(graphics[self.num_guesses])

    def pick_random_word(self):
        # This function picks a random word from the SOWPODS dictionary.
        # open the sowpods dictionary as a text file in readable format
        curdir = os.getcwd()
        filename = os.path.join(curdir, "sowpods.txt")
        with open(filename, 'r') as f:
            words = f.readlines()

        # generate a random index
        # -1 because len(words) is not a valid index into the list `words`
        index = random.randint(0, len(words) - 1)

        # print out the word at that index
        # the .strip() function removes all trailing spaces before and after the word
        word = words[index].strip()
        #return word
        self.randomWord = word
    def ask_user_for_next_letter(self):
        letter = input("Guess your letter: ")
        return letter.strip().upper()

    def generate_word_string(self, letters_guessed):
        output = []
        for letter in self.randomWord:
            if letter in letters_guessed:
                output.append(letter.upper())
            else:
                output.append("_")

        # creates a string from the members of the list by using whitespace as a separator
        self.output_string = " ".join(output)

    def guessed_incorrectly(self):
        self.num_guesses -= 1
