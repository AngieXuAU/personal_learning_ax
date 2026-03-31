
user_in = input("This program returns a dictionary containing each word and its length. Enter a sentence: ").split()
wlen_map = {}

for word in user_in:
    wlen_map[word] = len(word)

print(wlen_map)