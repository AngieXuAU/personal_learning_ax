vowels = {"a", "e", "i", "o", "u"}

s = input("This program removes all the vowels from a string. Enter a string: ")

for char in s:
    if char.lower() in vowels:
        s = s.replace(char, "")

print(s)