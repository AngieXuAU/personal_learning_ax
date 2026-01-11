
def flip_parenthesis(backwards):
    forwards = ""
    for c in backwards:
        if c == ")":
            forwards += "("
        elif c == "]":
            forwards += "["
        else:
            forwards += "{"
    return forwards[::-1]

user_in = input("This program determines whether a user input string of nested parentheses is valid. Enter the parenthesis you want to check: ").strip()

l = len(user_in)
if l % 2 != 0:
    print("These parenthesis are not valid.")
else:
    p1 = user_in[:l//2]
    p2 = flip_parenthesis(user_in[l//2:])
    print("These parenthesis are valid." if p1 == p2 else "These parenthesis are not valid.")

