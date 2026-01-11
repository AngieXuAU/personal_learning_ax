
user_in_list = input("This program tells you whether any element appears twice in a set. Enter a set of elements, each separated by a comma and then a space: ").split(", ")

seen = set()

for element in user_in_list:
    if element in seen:
        print(True)
        break
    else:
        seen.add(element)

else:
    print(False)