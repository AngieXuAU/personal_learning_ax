user_in = input("This program checks if an input string is palindromic, ignoring whitespaces and capitalisation. Enter a string to be checked: ").replace(" ", "").lower()

palindrome = True           # set up a bool to true

# alternative method: slicing - write the string backwards and compare
if user_in[::-1] != user_in:
    palindrome = False


print(palindrome)
