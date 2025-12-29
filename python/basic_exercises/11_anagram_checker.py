
anagrams = True

str_1 = input("This program checks if two strings are anagrams of each other. Enter the first string: ").lower().replace(" ", "")

dict_a = {}


# original method: string --> dictionary to compare frequencies

# add the first string to a dictionary with the letters as keys and with their frequencies
for i in str_1:
    if i in dict_a:
        dict_a[i] += 1
    else:
        dict_a[i] = 1


str_2 = input("Enter the second string: ").lower().replace(" ", "")

# loop through the second string

if len(str_1) != len(str_2):
    anagrams = False
else:                                           
    for j in str_2:
        if j not in dict_a:                     # if letter not present, it's not an anagram 
            anagrams = False
            break                               # potential improvement: check if the dict_a[j] value is already 0 - that means there's already too many letters in str_2 --> fail!
        else:                                   # subtract 1 from the frequency of the letter
            dict_a[j] -= 1

    for k in dict_a:                            # loop through the dictionary
        if dict_a[k] != 0:
            anagrams = False                    # if anagram: the value should be 0 bc added and subtracted same number of times
            break


# improved method: collections

print(anagrams)

