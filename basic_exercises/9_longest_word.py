
sentence = input("This program returns the longest word in a sentence (if same length, the first): ").strip(",.?!").split()

# my method: keep track of the longest word
# longest = ""

# for word in sentence:
#     if len(word) > len(longest):
#         longest = word


# alternate method: using the max function with a key

print(max(sentence, key = len))
