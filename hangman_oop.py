from hangman import Hangman

hm = Hangman('Subj02', 8)

WORD = hm.pick_random_word()

# creates a set containing the letters of WORD
letters_to_guess = set(WORD)

# creates an empty set
correct_letters_guessed = set()
incorrect_letters_guessed = set()

print("Welcome to Hangman!")
while (len(letters_to_guess) > 0) and hm.num_guesses > 0:
    guess = hm.ask_user_for_next_letter()
    # check if we already guessed that
    # letter
    if guess in correct_letters_guessed or guess in incorrect_letters_guessed:
            # print out a message
        print("You already guessed that letter.")
        continue

    # if the guess was correct
    if guess in letters_to_guess:
        # update the letters_to_guess
        letters_to_guess.remove(guess)
        # update the correct letters guessed
        correct_letters_guessed.add(guess)
    else:
        incorrect_letters_guessed.add(guess)
        # only update the number of guesses
        # if you guess incorrectly
        hm.guessed_incorrectly()

    word_string = hm.generate_word_string(WORD, correct_letters_guessed)
    print(word_string)
    print("You have {} guesses left".format(hm.num_guesses))
    hm.draw_hangman()

# tell the user whether they have won or lost
if hm.num_guesses > 0:
    print("Congratulations! You correctly guessed the word {}".format(WORD))
else:
    print("Sorry, you lost! Your word was {}".format(WORD))
