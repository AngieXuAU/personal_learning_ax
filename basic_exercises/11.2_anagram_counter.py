
str_1 = input("This program checks if two strings are anagrams of each other. Enter the first string: ").lower().replace(" ", "")

str_2 = input("Enter the second string: ").lower().replace(" ", "")

from collections import Counter
anagrams = (Counter(str_1) == Counter(str_2))

print(anagrams)