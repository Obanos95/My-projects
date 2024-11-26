from math import pi

def circle():
    r=float(input('Enter radius: '))
    P=2*pi*r
    print(P)

circle()
while True:
    choice=input('Do you want to continue the program? To stop the program, enter "n" or "N": ').lower()
    if choice=='n':
        break
    circle()
