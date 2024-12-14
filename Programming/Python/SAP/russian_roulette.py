import os
import random

rand=[1,2,3,4,5,6]

while len(rand)!=0:
    shooot=input('Press Enter to shoot')
    shot=random.choice(rand)
    if shot == 3:
        print('you dead')
    rand.remove(shot)
