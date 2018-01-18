# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    result = True
    for char in secretWord:
        if char not in lettersGuessed:
            result = False
            break
    return result


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = [x for x in secretWord]
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            if i == 0:
                result[i] = '_ '
            elif i == len(secretWord)-1:
                result[i] = ' _'
            else:
                result[i] = ' _ '
    return ''.join(result)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    chars = [x for x in string.ascii_lowercase]
    if chars:
        for char in lettersGuessed:
            if char in chars:
                chars.remove(char)
    return ''.join(chars)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    numOfGuesses = 8
    print('Welcome to the game, Hangman!\nI am thinking of a word that is {} letters long'.format(len(secretWord)))
    while numOfGuesses != 0:
        print('_'*12+"\n")
        print("You have {0} guesses left.\nAvailable Letters: {1}".format(numOfGuesses, getAvailableLetters(lettersGuessed)))
        userInput = input("Please guess a letter: ")

        if userInput in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        elif userInput in secretWord:
            lettersGuessed.append(userInput)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed):
                print('_'*12+"\n")
                print("Congratulations, you won!")
                break
        else:
            lettersGuessed.append(userInput)
            numOfGuesses = numOfGuesses - 1
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
    if numOfGuesses == 0:
        print('_'*12+"\n")
        print("Sorry, you ran out of guesses. The word was " + secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)