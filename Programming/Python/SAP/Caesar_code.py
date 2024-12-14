# Task 4
word = input('Enter the word: ').upper()
k = int(input('Enter your coefficient: '))
ciphered_word = ''
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in word:
    ind = letters.index(i)
    if ind + k > len(letters):
        ind = ind - len(letters)
    ciphered_word += letters[ind + k]

print(ciphered_word)
