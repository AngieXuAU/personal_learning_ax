
user_in = input("This program returns the first non-repeating character in a string. Enter a string: ")

all_letters = set()                     # create an empty set for all letters
unique_letters = []                     # and an empty list (to preserve order)


for i in user_in:           
    if i in all_letters:                # if it's already in the set of all letters, get rid of it from the list of uniques
        if i in unique_letters:         # don't remove it if it's not already there (will cause program to crash)
            unique_letters.remove(i)        
    else:
        all_letters.add(i)
        unique_letters.append(i)

if len(unique_letters == 0):
    print("There are no unique letters.")   # edge case: no distinct letters
else:
    print(unique_letters[0])                # print the first unique one