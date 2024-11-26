import random
import time

correct = 0 # Number of correct answers
randomnumbs=[1,2,3,4,5,6,7,8,9,10] # I used list to delete used numbers so that the numbers are unique

numb = int(input('Chose a number from 1 to 10 to revise: ')) #User chooses a number from 1 to 10
starttime = time.time() #Time of starting the program
for i in range(1,11): # Repeating the loop 10 times
    mult = random.choice(randomnumbs) # Random number from 1 to 10 for revision
    randomnumbs.remove(mult) # Deleting used numbers
    print(numb,'*',mult)
    answer = int(input('Write the answer: '))
    if answer == numb*mult:
        print('Correct!')
        correct += 1
    else:
        print('Incorrect! The answer is',numb*mult)
finishtime = time.time() #Time of finishing the program
# Checking the number of coorect answers
print('Number of correct answers:',correct)
if correct == 10:
    print('Excelent!')
elif correct == 9:
    print('Very good')
elif correct >= 7:
    print('Good')
elif correct >= 4:
    print('Average')
elif correct >= 1:
    print('You should rework this table')
else:
    print('You MUST rework this table')

print('Average time taken on every respond:',int(finishtime - starttime)/10)
