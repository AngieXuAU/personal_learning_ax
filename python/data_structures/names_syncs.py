
letter_vals = {"a" : "Ace", "b": 2, "c": 3, "d": 4, "e": 5, 
               "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, 
               "k": "Jack", "l": "Queen", "m": "King", "n": "Ace", "o": 2, 
               "p": 3, "q": 4, "r": 5, "s": 6, "t": 7, 
               "u": 8, "v": 9, "w": 10, "x": "Jack", "y": "Queen", 
               "z": "King"}


name = input("Enter a name: ").lower()
name = name.replace(" ", "")


for i in range(len(name) - 4):
    for j in range(i, i+5):
        print(letter_vals[name[j]], end = "\t")
    print("")

# sum = 0

# for letter in name:
#   print(letter_vals[letter])
        # sum += ((ord(letter) - 97) % 13 + 1)


# for letter in name:
#      if letter in letter_vals:
#           sum += 

# print(sum)