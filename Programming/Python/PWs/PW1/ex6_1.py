# Exercice 6.1
starting_balance = float(input('Enter your starting balance: ')) #Money invested
interest_rate = float(input('Enter interest rate: ')) #Interest rate
investment_period = int(input('Enter investment period: ')) #Investment period
balance = starting_balance

for i in range(1,investment_period + 1): #Calculating interest
    money_earned = balance * interest_rate/100
    balance += money_earned

print('Final balance:', balance)
print('Money earned:', balance - starting_balance)
