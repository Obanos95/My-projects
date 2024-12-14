numdict = {1:'One', 2:'Two', 3:'Three'}
numb = int(input('Enter the number you want to convert to word: '))
print(numdict[numb])

langdict = {'my':'mon','red':'rouge','pen':'stylo'}
sent = 'My red pen'.lower()
print(sent.capitalize())
sentls = sent.split()
for i in range(len(sentls)):
    sentls[i] = langdict[sentls[i]]
print((' '.join(sentls)).capitalize())
