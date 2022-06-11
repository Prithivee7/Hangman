import random

"""
Reads the file which has words separated by a space and returns the file as a string
"""


def loadWords():
    with open("words.txt", 'r') as G:
        textfile = G.read()
    return textfile


"""
Converts the dictionary into a string and returns the random word
"""


def chooseWord():
    textfile = loadWords()
    sl = textfile.split()
    return(random.choice(sl))


""" 
secretWord , a string which is guessed by the user
lettersGuessed , list containing the letters which are guessed so far

if the word is currently guessed , it returns True else False
"""


def isWordGuessed(secretWord, lettersGuessed):

    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True


"""
secretWord , a string which is guessed by the user
lettersGuessed , list containing the letters which are guessed so far

returns the output string after filling , it is a combination of letters and underscore. Underscore represents the letters which haven't  been guessed
"""


def getGuessedWord(secretWord, lettersGuessed):

    l = len(secretWord)
    s = ["_ "]*l
    for i in range(l):
        if secretWord[i] in lettersGuessed:
            pos = i
            for j in range(l):
                if(pos == j):
                    s[pos] = secretWord[i]+" "
    return("".join(s))


"""
secretWord , a string which is guessed by the user
lettersGuessed , list containing the letters which are guessed so far
returns the string by deleting the guessed letter
alph="abcdefghijklmnopqrstuvwxyz"
"""


def getAvailableLetters(lettersGuessed):

    alph = "abcdefghijklmnopqrstuvwxyz"
    r = ""
    for i in alph:
        if i not in lettersGuessed:
            r = r+i
    return(r)


"""
secretWord , a string which is guessed by the user
Number of guesses allowed=8
A loop to iterate 8 times.
If the Guess is correct number of guesses needs to be the same. If the guess is wrong the no of gueesses need to be decremented by 1
I fthe number of guiesses is exhausted it comes out of the loop. If the secretWord is guessed it prints congrats and comes ouit of the loop
"""


def hangman(secretWord):

    numguess = 8
    lettersGuessed = []
    print()
    print("Welcome to the game hangman")
    print(f"I am thinking of a word that is {len(secretWord)} words long")
    print("------------------------")
    while(True):
        print("you have", numguess, " guesses left")
        print("Available Letters:", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        if(len(guess) != 1):
            print("Please enter only one letter")
        elif(guess not in "abcdefghijklmnopqrstuvwxyz"):
            print("Please Enter only lowercase Alphabets")
        else:
            guessInLowerCase = guess.lower()
            if(guessInLowerCase in secretWord and guessInLowerCase not in lettersGuessed):
                lettersGuessed.append(guessInLowerCase)
                print("Good Guess:", getGuessedWord(
                    secretWord, lettersGuessed))
            elif(guessInLowerCase in lettersGuessed):
                print(f"Oops!! {guessInLowerCase} has been guessed before", getGuessedWord(
                    secretWord, lettersGuessed))
            else:
                print(f"Oops {guessInLowerCase} is not in my word",
                      getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(guessInLowerCase)
                numguess = numguess-1
                print("_______________")
            if(isWordGuessed(secretWord, lettersGuessed) == True):
                print("Congratulations u have won!!")
                break
            if(numguess == 0):
                print(f"Sorry u ran out of guesses.the word is {secretWord}")
                break


secretWord = chooseWord()
hangman(secretWord)
