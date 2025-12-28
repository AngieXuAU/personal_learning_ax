
user_in = input("This program outputs the 2nd largest number entered. Enter a list of numbers separated by a comma and space: ").split(", ")

# my original method

# numbers = []                    # created an empty list

# for i in user_in:
#     numbers.append(int(i))      # added all the strings as integers to the empty list

# numbers.sort()                  # sort and print the list
# print(numbers[-2])

# cleaner syntax alternative

numbers = sorted(set(int(i) for i in user_in))      # int(i) casts string into integer, set turns it into a set and sorted sorts the set and spits out a list
print(numbers[-2])