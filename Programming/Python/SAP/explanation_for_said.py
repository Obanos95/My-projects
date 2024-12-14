# Explanation of lists
'''ls = ['13', 13, 12.6, 15, 'Salam', 40.23]
print(len(ls[0]))'''

# Generators
'''a=[x for x in range(1,12)]
print(a)'''

# Functions
'''def said():
    print('Hello')
    print('Hello')

said()
said()
said()'''

# Return
'''def main(n):
    n += 1
    print(n)
n = 10
m = main(n)
print(main(n),m)'''

#Said tests
'''months=['January','February','March','Aprel','May','June','Jule','August','September','Octember','November','December']
i = months.index(input('Write your month').capitalize())
if i in (0,2,4,6,7,9,11):
    print(months[i],'has 31 days')
elif i==1:
    ask=input('is it leap year? y/n').capitalize()
    if ask=='y':
        print('Febuary has 29 days')
    else:
        print('Febuary has 28 days')
else:
    print(months[i],'has 30 days')'''

#Leap yer
'''a = int(input())
if (a%4 == 0 or a%100 == 0) and a%400 != 0:
    print('Leap')
else:
    print('Not leap')'''

#Index ex7
'''def index(sequence,character):
    global list
    list=[]
    count=-1
    for i in sequence:
        count+=1
        if i == character:
            list.append(count)
    return list  
a=input('write string')
b=input('character')    
index(a,b)
print(list)'''