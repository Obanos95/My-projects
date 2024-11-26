#CS_1 PW1 Exercise 3
#Correct version of the program with explanations in the comments
def main():
    print('start')
    x = 0 #"x == 0;"   There should be no ';' and should be one '=' (syntax error)
    while x < 3: #"while x < 3"  There should be ':' after 'x < 3' (syntax error)
        print(x)
        if x == 1: #"if x = 1"  There should be '==' after 'x' and ':' after 1 (syntax error)
            print('1')
        x += 1 #This line was not inside "while x < 3". This program was infinite. I've put another tab before this line so that "x" can change and the program has an endpoint (semantic error)
    print('end')#"print(end)"  There should be quotes before and after "end" or else it's considered as a variable which does not exist, it showed name error (syntax error)

main() #"main"  There should be parentheses after "main" because we call the function, it will just not work

