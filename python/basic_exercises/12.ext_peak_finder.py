import sys

raw_nums = input("This program finds the first peak (number strictly > both its neighbours) in a list. Enter a list, with each number separated by a comma and space: ").split(", ")

nums = list(map(int, raw_nums))                         # map is useful as there is already a function (int). doesn't actually compute the value until you ask for it

if nums[0] > nums[1]:
    print(nums[0])
    sys.exit()

for i in range(1, len(nums)-1):                         # loop from the 2nd to penultimate
    if nums[i] > nums[i-1] and nums[i] > nums[i+1]:     # comparison to check peak
        print(nums[i])                                  # spit it out 
        sys.exit()    

if nums[-1] > nums[-2]:
    print(nums[-1])
