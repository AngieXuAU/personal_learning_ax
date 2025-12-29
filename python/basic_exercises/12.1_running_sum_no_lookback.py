
running_sum = []
total = 0

# take input
raw_nums = input("This program returns a running sum of a list of numbers. Enter a list of numbers separated by a comma and space: ").split(", ")


for i in range(len(raw_nums)):          # loop through the list
    total += int(raw_nums[i])           # add all the items in the list to the total
    running_sum.append(total)           # add the total to the running sum

print(running_sum)