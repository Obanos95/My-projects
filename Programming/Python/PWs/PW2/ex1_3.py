import random #The library to choose random number

def machinesgame(): #Machine chooses a number
    randnum = random.randint(1,999) #Declaring random number
    guess = 0 #User's guess
    numoftries = 0 #Number of tries by user
    while guess != randnum: #The game code
        guess = int(input('Try to guess the number: '))
        if guess < randnum:
            print('The number is bigger')
            numoftries += 1
        elif guess > randnum:
            print('The number is smaller')
            numoftries += 1
        else:
            print('You guessed the number!')
            print(f'Number of tries:{numoftries}')
def usersgame(): #User chooses a number
    number = int(input('Choose a number for machine to guess: '))
    machguess = 0 #Machine's guess
    numoftries = 0 #Number of tries by machine
    ll = 1 #Lower limit of the random choice
    ul = 999 #Upper limit of the random choice
    while machguess != number:
        machguess = random.randint(ll,ul)
        print(machguess)
        bigorsmall = input('Is your number Bigger or Smaller than the guessed one? Or is the number Found?[b/s/f]').lower() #User should input if the chosen by machine number is bigger or smaller of the number choosen by the user
        # Giving the machine new limit
        if bigorsmall == 'b':
            ll = machguess
            numoftries += 1
        elif bigorsmall == 's':
            ul = machguess
            numoftries += 1
        elif bigorsmall == 'f':
            print('The machine won!')
            print(f'Number of tries:{numoftries}')

continuegame = None #This line is needed to declare "continuegame" variable so that code doesn't break
while continuegame != 'n':
    machineoruser = input('Choose if you want the machine to Choose the number or to Guess[C/G]').lower()
    if machineoruser == 'c':
        machinesgame()
    else:
        usersgame()
    continuegame = input('Do you want to play again?[y/n]: ').lower()
