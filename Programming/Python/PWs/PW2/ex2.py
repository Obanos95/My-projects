import random #The library to choose random number

def machinesgame(): #Machine chooses a number
    randnum = random.randint(1,9999) #Declaring random number
    guess = 0 #User's guess
    numoftries = 0 #Number of tries by user
    while guess != randnum: #The game code
        guess = int(input('Try to guess the number: '))
        if guess < randnum:
            print('The proposed number is smaller than the number to be found')
            numoftries += 1
        elif guess > randnum:
            print('The proposed number is bigger than the number to be found')
            numoftries += 1
        else:
            print('You guessed the number!')
            print(f'Number of tries:{numoftries}')
def usersgame(): #User chooses a number
    machguess = 0 #Machine's guess
    numoftries = 0 #Number of tries by machine
    ll = 1 #Lower limit of the random choice
    ul = 9999 #Upper limit of the random choice
    abandon = False
    bigorsmall = None
    while bigorsmall != '=':
        if ll >= ul: #Check for cheating
            print('You are cheating')
            actualnumber = int(input('What was your number? ')) 
            if actualnumber > ul:
                print('You put > instead of < somewhere')
            else:
                print('You put < instead of > somewhere')
            break
        machguess = random.randint(ll,ul)
        print(machguess)
        bigorsmall = input('Is the proposed number Bigger or Smaller than the number to be found? Or is the number Found?[>/</=]. If you want to abandon the game enter [0]').lower() #User should input if the chosen by machine number is bigger or smaller of the number choosen by the user
        # Giving the machine new limit
        if bigorsmall == '0':
            confirm = input('Are you sure you want to abandon the game? [y/n]')
            if confirm == 'y':
                print('Game abandoned')
                abandon = True
                break
        if bigorsmall == '>':
            ul = machguess
            numoftries += 1
        elif bigorsmall == '<':
            ll = machguess
            numoftries += 1
        elif bigorsmall == '=':
            print('The machine won!')
            print(f'Number of tries:{numoftries}')
    return abandon
continuegame = None #This line is needed to declare "continuegame" variable so that code doesn't break
while continuegame != 'n':
    machineoruser = input('Choose if you want the machine to Choose the number or to Guess[C/G]').lower()
    if machineoruser == 'c':
        machinesgame()
    else:
        abandoned_game = usersgame() #The program will always return either True or False
        if abandoned_game == True:
            break
    continuegame = input('Do you want to play again?[y/n]: ').lower()
