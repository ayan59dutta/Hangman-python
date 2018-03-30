#!/usr/bin/env python3

# Hangman game

import random

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
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    displayWord = ''
    for letter in secretWord:
        if letter not in lettersGuessed:
            displayWord += '_'
        else:
            displayWord += letter
    return displayWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ''
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in lettersGuessed:
            availableLetters += letter 
    return availableLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, the player is informed of how many 
      letters the secretWord contains.

    * Player is asked to supply one guess (i.e. letter) per round.

    * The player receives feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each round, the player is shown the
      partially guessed word so far, as well as letters that the 
      player has not yet guessed.

    * A player is allowed 8 guesses and is reminded of how many
      guesses are left after each round. Guessing the same letter
      does not take away a chance.

    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    print('-------------')
    noGuessesLeft = 8
    lettersGuessed = []
    while noGuessesLeft > 0:
        print('You have '+str(noGuessesLeft)+' guesses left')
        availableLetters = getAvailableLetters(lettersGuessed)
        print('Available letters: '+ availableLetters)
        guess = (input('Please guess a letter: ')).lower()
        if guess in availableLetters:
            lettersGuessed.append(guess)
            word = getGuessedWord(secretWord, lettersGuessed)
            if guess in secretWord:
                print('Good guess: '+word)
            else:
                print('Oops! That letter is not in my word: ' + word)
                noGuessesLeft -= 1
        else:
            print("Oops! You've already guessed that letter: " + word)
        print('-------------')
        if '_' in word:
            continue
        else:
            break
    if noGuessesLeft == 0:
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
    else:
        print('Congratulations, you won!')

if __name__ == '__main__':
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
