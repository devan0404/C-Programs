'''
sentence = input("Enter a sentence: ").lower()
found = True

for char in "abcdefghijklmnopqrstuvwxyz":
    if char not in sentence:
        found = False
        break

if found:
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.") 
    '''
