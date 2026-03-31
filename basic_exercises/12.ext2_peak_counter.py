import sys

raw_nums = input("This program counts the peaks (numbers strictly > both its neighbours) in a list. Enter a list, with each number separated by a comma and space: ").split(", ")
nums = list(map(int, raw_nums))                         # map is useful as there is already a function (int). doesn't actually compute the value until you ask for it

peaks_dict = {}

def add_peak(num):
    if num in peaks_dict:                               # if already a peak, add 1 to the counter
        peaks_dict[num] += 1
    else:                                               # if not, add it in
        peaks_dict[num] = 1

if nums[0] > nums[1]:                                   # edge case: first number larger than second
    add_peak(nums[0])

for i in range(1, len(nums)-1):                         # loop from the 2nd to penultimate
    if nums[i] > nums[i-1] and nums[i] > nums[i+1]:     # comparison to check peak
        add_peak(nums[i])                                       

if nums[-1] > nums[-2]:                                 # edge case: last number larger than penultimate
    add_peak(nums[-1])

print(sorted(peaks_dict.items(), key=lambda item: item[1], reverse=True))       # lambda is like a one line function, the 1 means get the second thing in the key, value pair, reverse = descending

# alternate syntax for the print
from operator import itemgetter

print(sorted(peaks_dict.items(), itemgetter(1), reverse= True))
