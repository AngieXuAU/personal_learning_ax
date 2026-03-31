
running_sum = []                # start the list

raw_nums = input("This program returns a running sum of a list of numbers. Enter a list of numbers separated by a comma and space: ").split(", ")

running_sum.append(int(raw_nums[0]))                                    # start the running sum with the first number

for i in range(1, len(raw_nums)):
    running_sum.append(int(raw_nums[i]) + int(running_sum[i-1]))        # append the sum with its previous term + the next term of the raw numbers

print(running_sum)