import random #The library to choose random number

continuegame = None #This line is needed to declare "continuegame" variable so that code doesn't break
while continuegame != 'n':
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
    continuegame = input('Do you want to play again?[y/n]: ').lower()
