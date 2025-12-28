
def remove_chars(word, n):
    new_word = word[n: len(word)+1]
    
    return new_word


original = input("This program removes letters from a string.\nEnter a string: ")
letters_removed = int(input("How many letters would you liked removed: "))

print(remove_chars(original, letters_removed))

print(original[letters_removed: len(original)+1])