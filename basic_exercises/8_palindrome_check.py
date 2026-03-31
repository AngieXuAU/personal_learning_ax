
user_in = input("This program checks if an input string is palindromic, ignoring whitespaces and capitalisation. Enter a string to be checked: ").replace(" ", "").lower()

palindrome = True           # set up a bool to true

l = len(user_in)

# # original mathematical logic:
# if l % 2 == 1:
#     l -= 1                  # odd string length case

# l /= 2                      # iterate for half the string (from the front and back)


# integer division:
for j in range(l // 2):       # integer division cuts down on maths
    if user_in[j] != user_in[-(j+1)]:
        palindrome = False
        break

print(palindrome)