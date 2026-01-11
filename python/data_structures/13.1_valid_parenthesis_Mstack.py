
open = {"{", "[", "("}

close = {"}": "{", "]": "[", ")": "("}

user_in = input("This program determines whether a user input string of nested parentheses is valid. Enter the parenthesis you want to check: ").strip()

stack = []

for c in user_in:
    if c in open:
        stack.append(c)
    elif close[c] == stack[-1]:
        stack.pop()
    else:
        print("Parentheses invalid.")
        break

print("Parentheses valid." if len(stack) == 0 else "Parentheses invalid.")

# note that this logic breaks if the user enters a closing bracket first. Check if it's in the closing brackets first.
# MOST IMPORTANT LINE

# stack.pop() != close_brackets[c]
#       - compares the thing it just popped with the matching open parentheses of the closing bracket it is examining