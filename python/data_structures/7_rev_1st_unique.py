
user_in = input("This program returns the first unique character in a given string. Enter a string: ")

in_list = [c for c in user_in]

seen = set()

for c in user_in:
    if c in seen:
        while c in in_list:             # works but is very slow, better to just track how many times each character appears and print the first one that appears once
            in_list.remove(c)
    else:
        seen.add(c)

if len(in_list) < 1:
    print(-1)
else:
    print(in_list[0])
