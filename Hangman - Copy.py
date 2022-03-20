import random

hangman_sequences = [''' 
   +-----+
         |            
         |           
         |           
       =====''', '''           
   +-----+
   o     |            
         |           
         |           
       =====''', ''' 
   +-----+
   o     |            
   |     |           
         |           
       =====''', '''
   +-----+
   o     |            
   |\    |           
         |           
       =====''', '''   
   +-----+
   o     |            
  /|\    |           
         |           
       =====''', '''                
   +-----+
   o     |            
  /|\    |           
    \     |           
       =====''', '''                   
   +-----+
   o     |            
  /|\    |          
  / \    |           
       =====''']

words = (''' london paris dubai istanbul delhi mumbai tokyo rome 
            mecca prague shenzhen seoul amsterdam miami vegas barcelona
            berlin moscow kiev venice madrid orlando toronto sydney
            beijing munich budapest dublin dubai stockholm chicago 
            atlanta dallas lagos bangkok milan lisbon vienna ''').split()

def get_random_word(words): # Returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(words) - 1)
    return words[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(hangman_sequences[len(missedLetters)])
    print()

    print('Missed letters list:', end='')
    for letter in missedLetters:
        print(letter, end='')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replace blanks with correct words.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Show the secret word with spaces between each letter.
        print(letter, end='')
    print()

def getGuess(alreadyGuessed): # Returns the letter the player guessed, makes sure single letter entered.
    while True:
        print('Guess a letter -->')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Are you stupid? Enter a LETTER")
        else:
            return guess

def playAgain(): # Play again...?
    print('Do you want to play again? (yes/no)')
    return input().lower().startswith("y")

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = get_random_word(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(hangman_sequences) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' +
                  str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guess, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask if the want to play again, only if done
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = get_random_word(words)
        else:
            break

