
anagrams = False

# shortcut method: sort them and if they are anagrams they should be the exact same

str_1 = sorted(input("This program checks if two strings are anagrams of each other. Enter the first string: ").lower().replace(" ", ""))

str_2 = sorted(input("Enter the second string: ").lower().replace(" ", ""))

print(str_1 == str_2)
