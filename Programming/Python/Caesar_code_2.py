# Caesar cipher 2.0
word = input('Enter the word: ').upper()
k=int(input('Enter coefficient: '))
newword=''
for i in word:
    w_o=ord(i)
    if w_o+k>90:
        newword+=chr(w_o+k-90+64)
    else:
        newword+=chr(w_o+k)

print(newword)
