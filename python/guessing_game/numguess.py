from random import randint
def ask(quest='HELLO THIS DEVELOPER WAS LAZY AND DID NOT SETUP A QUESTION FOR THIS QUESTION!'): #ask function
    if quest == '':
        print(quest, end='')
    else:
        print(quest)
    print('-', end='')
    inp = input()
    return inp #return the user's input

def play():
    run = True #start game
    while run: #game loop
        print('Starting game!')
        print('A number has been selected...')
        num = randint(lo, hi)
        wrong = True
        guesses = maxGuesses
        while wrong: #"wrong" actually doesnt make a lot of sense in this case
            guess = int(str(ask('What is your guess?')))
            print('')
            if guess == num:
                print("Great! You guessed the number!")
                wrong = False
            elif guess > num:
                print('Nope! Too high!')
                guesses -= 1
            elif guess < num:
                print('Nope! Too low!')
                guesses -= 1
            else:
                print('Sorry, what?')
                print(num)
            print('You have '+str(int(guesses))+' guesses left.')
            print('')
            if guesses <= 0: #loose
                wrong = False
                loose = True
                print('Sorry! You ran out of tries!\nTry again!')
        if loose == False: #if lost, do not print below
            print('Good job! It only took you {}/{} guesses!\n'.format(str(int(maxGuesses-guesses)),str(int(maxGuesses))))
        stop = ask('Would you like to change some options? Y/N?')
        if stop == 'y' or stop == 'yes':
            start()

hi = 100
lo = 0
maxGuesses = 10

def start():
    global hi
    global lo
    global maxGuesses

    print('''The current settings are:
    Number max = {}
    Number min = {}
    Max guesses = {}'''.format(hi,lo,maxGuesses)
    )
    op = ask('Change options? Y/N')

    if op == 'y' or op == 'yes':
        hi = ask('Number max?')
        lo = ask('Number min?')
        maxGuesses = ask('How many guesses?')
    else:#anything other than "yes" will not change any options
        print('Okay then!')

    play()
start() #start the game
