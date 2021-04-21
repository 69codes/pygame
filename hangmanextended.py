# this an hangman exercise. i hope it is good, i have tremendous help from a book
import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    0   |
        |
        |
       ===''', '''
    +---+
    0   |
    |   |
        |
       ===''', '''
    +---+
    0   |
   /|   |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
   /    |
       ===''', '''
    +---+
    0   |
   /|\  |
   / \  |
       ===''']
words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split()
         'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid septagon octagon chevron pentagon'.split()
         'Fruits':'apple orange lemon lime pear watermelon banana'.split()
         'Animals':'bat bear beaver cat leech goat frog fish python rat rabbit shark lion leech sheep strinker'.split()
    }

def getRandomWord(wordDict):
    #this function returnd a random string from teh passed list
    wordKey = random.choice(list(wordDict.keys()))

    # First, randomly select a key from the dictionary
    wordIndex = random.randint(0, len(wordDict[wordkey]) - 1)

    return [wordDict[wordkey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:',  end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #replace blanks with correct letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with blanks between
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')

        elif guess in alreadyGuessed:
            print('You have already guessed that letter choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER!!')

        else:
            return guess

def playAgain():
    # this function returns true if the player wants to play again
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # let the player enter a letter.

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # check if the player has won

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes!! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        #chexk if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('you have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses,the word was "' + secretWord + '"')
            gameIsDone = True
            # ask the player if he want to play again
            if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord = getRandomWord(words)
                else:
                    break
