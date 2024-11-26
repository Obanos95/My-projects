import random #The library to choose random number

continuegame = None #This line is needed to declare "continuegame" variable so that code doesn't break
while continuegame != 'n':
    number = int(input('Choose a number for machine to guess: '))
    machguess = 0 #Machine's guess
    numoftries = 0 #Number of tries by machine
    ll = 1 #Lower limit of the random choice
    ul = 999 #Upper limit of the random choice
    while machguess != number:
        machguess = random.randint(ll,ul)
        print(machguess)
        bigorsmall = input('Is the proposed number Bigger or Smaller than the number to be found? Or is the number Found?[B/S/F]').lower() #User should input if the chosen by machine number is bigger or smaller of the number choosen by the user
        # Giving the machine new limit
        if bigorsmall == 'b':
            ul = machguess
            numoftries += 1
        elif bigorsmall == 's':
            ll = machguess
            numoftries += 1
        elif bigorsmall == 'f':
            print('The machine won!')
            print(f'Number of tries:{numoftries}')
    continuegame = input('Do you want to play again?[y/n]: ').lower()
        
