import random

global round
global wheelValue
global player
global word
global guessingWord
global lWord

# Creating a random starter for the player
player = random.randrange(0, 2)
# print(player)
# print('----')
vowel = ['a', 'e', 'i', 'o', 'u']
finalList = ['r','l', 's', 't', 'n', 'e']
bank = [0, 0, 0]
wheel = [250, 300, 350, 400, 450, 'lose', 500, 550, 600, 'bankrupt', 650, 'lose', 700, 750, 800, 850, 900, 950, 1000,
         5000, 10000, 200, 400, 450]
round = 1
wordList = ['alligator', 'computer', 'rheumatologist']
hintList = ['An animal', 'Everyday device', 'An occupation']


def gameStart():
    print('''
    --- Welcome to Cory's Rendition of Wheel of Fortune! ---
    
          I hope that everyone is on their A - game
            with today's tough selection of words! 
            
    --------------------- Good Luck! -----------------------        
    ''')
    wordChoose()
    wheelTurn(player)


# wheelTurn function determines what will happen when a certain value is rolled on the spinWheel function.
def wheelTurn(player):
    global wheelValue
    print('''
    --------------------------------------------------------
    ''')
    play = str(input('Spin the wheel? y or n : '))
    if play == 'y':
        print('Spin!')
        spinWheel()
    elif play == 'n':
        print('Too bad!! We are spinning it anyways!')
        print('-----------------------------------------------------------')
        spinWheel()
    # check for bankrupt and lose a turn wheel spins
    if wheelValue == 'bankrupt':
        bank[player] = 0
        print('Oh no! You hit bankrupt, lose all your money and your turn.')
        nextTurn(player)
    elif wheelValue == 'lose':
        print('Oh no! You landed on lose a turn')
        nextTurn(player)
    else:
        wordGuess(wheelValue, player)


def spinWheel():
    global wheelValue
    wheelValue = wheel[random.randint(0, 23)]
    print('And the result is: ')
    print(wheelValue)


def wordChoose():
    global word
    global guessingWord
    if round == 1:
        word = wordList[0]
    if round == 2:
        word = wordList[1]
    if round == 3:
        word = wordList[2]
    guessingWord = ['_'] * len(word)
    print(word)
    # print(type(word))


def nextTurn(player):
    # print(player)
    if round == 1:
        if player == 0:
            player = 1
            input(str('Player 2, your turn! Press ENTER to continue: '))
            wheelTurn(player)
        elif player == 1:
            player = 2
            input(str('Player 3, your turn! Press ENTER to continue: '))
            wheelTurn(player)
        else:
            player = 0
            input(str('Player 1, your turn! Press ENTER to continue: '))
            wheelTurn(player)
    if round == 2:
        if player == 0:
            player = 1
            wheelTurn(player)
        if player == 1:
            player = 0
            wheelTurn(player)


def wordGuess(wheelValue, player):
    global guessingWord
    global word

    print(player)
    print(type(guessingWord))
    print('=================')
    print(guessingWord)
    print('=================')
    playerChoice = str(input('Guess a consonant, or guess the word? \'c\' for consonant, \'w\' for word : '))
    while playerChoice != 'c' and playerChoice != 'w':
        playerChoice = str(input('Invalid input, please enter in either c or w : '))
    if playerChoice == 'c':
        print('--------------------------')
        guess = str(input('Guess a consonant: '))
        print('--------------------------')
        while guess in vowel:
            print('--------------------------')
            print('Guess is a vowel, please guess again')
            print('--------------------------')
            guess = str(input('Guess a consonant: '))
            print('--------------------------')
        if guess in word:
            while guess in word:
                location = word.find(guess)
                # print(location)
                # print(type(location))
                # print(type(word))
                word = word.replace(guess, '!', 1)
                guessingWord[location] = guess
            if guessingWord.count('_') == 0:
                nextRound()
            print('------------------------------------')
            print(guess + ' is in the mystery word!')
            print('------------------------------------')

            print(guessingWord)
            bank[player] = bank[player] + wheelValue
            vowelGuess()
            nextTurn(player)
        if guess not in word:
            print('Incorrect guess')
            nextTurn(player)
    if playerChoice == 'w':
        fullWord()


def fullWord():
    guess = str(input('You are now guessing the full word, type your guess here: '))
    if round == 1 or round == 2:
        if guess in wordList:
            print('''
                -----------------------------------------------------------
                            Congrats, you guessed the word!
                         For guessing the word, you get $1000
                -----------------------------------------------------------
                ''')
            bank[player] = bank[player] + wheelValue + 1000
            nextRound()
        else:
            nextTurn(player)
    elif round == 3:
        if guess in wordList[2]:
            print('''
            -----------------------------------------------------------
                         Congrats, you have won the game!
                        For winning, you earn an extra $6900
                   I hope you enjoyed playing my Wheel of Fortune!
            -----------------------------------------------------------
            ''')
            print('Final bank account:')
            print(bank)

def vowelGuess():
    global word
    print('''
    -----------------------------------------------------------
    Would you like to buy a vowel? Buying a vowel requires $250
    -----------------------------------------------------------
    ''')
    continueGuess = str(input('         Yes or No? Type \'y\' or \'n\' : '))
    if continueGuess == 'y':
        bank[player] = bank[player] - 250
        guess = str(input('Please enter in a vowel: '))
        while guess not in vowel:
            print('Guess is a consonant, please enter in a vowel.')
            guess = str(input('Please enter in a vowel: '))
        if guess in word:
            while guess in word:
                location = word.find(guess)
                word = word.replace(guess, '!', 1)
                guessingWord[location] = guess
            print('------------------------------------')
            print(guess + ' is in the mystery word!')
            print('------------------------------------')
            print(guessingWord)
            print('')
            if guessingWord.count('_') == 0:
                nextRound()
            else:
                continueWord = str(input('Would you like to guess the full word? Type \'y\' or \'n\' : '))
                if continueWord == 'y':
                    fullWord()
                else:
                    nextTurn(player)
        else:
            print('------------------------------------')
            print('This vowel is not in the mystery word!')
            print('------------------------------------')
            nextTurn(player)
    if continueGuess == 'n':
        nextTurn(player)


def nextRound():
    global round
    if round == 1:
        round = 2
        print('''
        ------------------- Round 1 is over! -------------------
        Results after Round 1:
        ''')
        print('Player 1 bank:')
        print(bank[0])
        print('Player 2 bank:')
        print(bank[1])
        print('Player 3 bank:')
        print(bank[2])
        print('''
        -------------------------------------------------------
        ''')
        input(str('Continue to next round? Press ENTER.'))
        # Checks which player had the smallest bank, gets rid of their bank account from the bank
        if (bank[0] < bank[1]) and (bank[0] < bank[2]):
            bank.remove(bank[0])
        elif (bank[1] < bank[0]) and (bank[1] < bank[2]):
            bank.remove(bank[1])
        else:
            bank.remove(bank[2])
        print(bank)
        if bank[0] > bank[1]:
            player = 0
        else:
            player = 1
        # Head back to choose a random number, and to start back up the game.
        wordChoose()
        nextTurn(player)
    elif round == 2:
        round = 3
        if bank[0] > bank [1]:
            bank.remove(bank[1])
        else:
            bank.remove(bank[0])
            finalRound()

def finalRound():
    global word
    guesses = [''] * 4
    wordChoose()
    for i in range(len(finalList)):
        if finalList[i] in word:
            location = word.find(finalList[i])
            word = word.replace(finalList[i], '!', 1)
            guessingWord[location] = finalList[i]
    print('''
    ------------------- Welcome to the Final Round! -------------------
    
    In this round, we will give you six free letters! Alongside this,
    you will also get to choose 3 more consonants and 1 more vowel in
    the mystery word before you have one chance to guess the word.
       If you guess it right, you win! If not, then you lose :(
       
    -------------------------------------------------------------------
    ''')
    print('Here is our final mystery word!')
    print('-------------------------------')
    print(guessingWord)
    print('-------------------------------')
    for j in range(len(guesses)-1):
        guesses[j] = str(input('Please guess a consonant of your choice: '))
        print('')
    guesses[3] = str(input('Please guess a vowel of your choice: '))
    print('')
    for k in range(len(guesses)):
        while guesses[k] in word:
            if guesses[k] in word:
                location = word.find(guesses[k])
                word = word.replace(guesses[k], '!', 1)
                guessingWord[location] = guesses[k]
    print('Here is the word after adding your letters!')
    print('')
    print('-------------------------------')
    print(guessingWord)
    print('-------------------------------')
    fullWord()


gameStart()
