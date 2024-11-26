# Exercice 6.2
starting_balance = float(input('Enter your starting balance: ')) #Money invested
interest_rate = float(input('Enter interest rate: ')) #Interest rate
time_needed = 0 #Years needed to double the starting balance
balance = starting_balance


while balance < starting_balance * 2: #Calculating period of doubling the investment
    money_earned = balance * interest_rate/100
    balance += money_earned
    time_needed += 1

print('You\'ll get double of',starting_balance,'in',time_needed,'years')
