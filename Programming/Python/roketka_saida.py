import random
import time

coef = random.randint(2,5)
curcoef = 0
while curcoef != coef:
    print('Currect coefficient =', curcoef)
    choice = input('Stop the rocket?[y/n] ')
    if choice == 'y':
        print('Your coef is', curcoef)
        print('Max coef was', coef)
        break
    else:
        curcoef += 1
else:
    print('You lost!')
