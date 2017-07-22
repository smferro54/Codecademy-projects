#Moves the location of the first letter and adds ay at the end. Useful to remember string commands. 

pyg = 'ay'
original = input('Enter a word:')
while not (len(original) > 0 and original.isalpha()):
    original = input('Try again:')
word = original.lower()
first = word[0]
new_word = word[1:len(word)] + first + pyg
print(new_word)