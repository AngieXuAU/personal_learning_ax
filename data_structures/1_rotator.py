

nums = input("Enter a list of numbers each separated by a comma and then a space: ").split(", ")

shift = int(input("How many places would you like to shift the list? "))


nums_new = nums[-shift:] + nums[:-shift]

print(nums_new)