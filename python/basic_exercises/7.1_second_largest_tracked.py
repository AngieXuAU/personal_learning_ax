
# this method just keeps track of the largest and second largest numbers and iterates through the list

user_in = input("This program outputs the 2nd largest number entered. Enter a list of numbers separated by a comma and space: ").split(", ")

largest = second = float("-inf")

for i in user_in:
    j = int(i)
    if j > largest:
        second = largest
        largest = j
    elif j > second and j < largest:
        second = j

print(second)