import math

y=float(input('Enter y: '))
f=float(input('Enter f: '))

result=(1-((1+(2*y)/(y-1)-f**2-math.sqrt((1+(2*y)/(y-1)-f**2)**2-4*f**2*((2*y)/(y-1)-1))))/(2*f**2*((2*y)/(y-1)-1)))**(y/(y-1))

print('P/Pt =',result)
