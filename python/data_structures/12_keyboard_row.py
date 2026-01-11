
s1 = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
s2 = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
s3 = {"z", "x", "c", "v", "b", "n", "m"}

word_list = input("This program determines which of the given words is able to be typed using leters of only one row on a QWERTY keyboard. Enter a list of words, each separated by a space: ").split(" ")

for raw_word in word_list:
    word = raw_word.lower()
    if set(word).issubset(s1) or set(word).issubset(s2) or set(word).issubset(s3):
        print(word)