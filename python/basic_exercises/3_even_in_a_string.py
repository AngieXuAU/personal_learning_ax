
text = input("Enter your string: ")

print("Original string is ", text, "\nPrinting only even index chars")

for i in range(len(text)):
    if (i) % 2 != 0:
        print(text[i])