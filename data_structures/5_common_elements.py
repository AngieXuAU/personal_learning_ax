
l1 = input("This program prints out any elements that appear in both set 1 and set 2. Enter the first list of elements, each separated by a comma and then a space: ").split(", ")
l2 = input("Enter the second list of elements: ").split(", ")

set1 = set(l1)
set2 = set(l2)

duplicates = list(set1 & set2)

print(duplicates)
