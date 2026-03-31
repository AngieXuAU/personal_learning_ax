
user_in = input("This program returns the two indexes of the only pair of numbers that sum to a given target. Enter a list of numbers separated by a comma then a space: ")
nums = list(map(int, user_in.split(", ")))
target = int(input("Enter the target: "))

seen = {}

for i in range(len(nums)):
    x = target - nums[i]

    if x in seen:
        print(f"({i + 1}, {seen[x] + 1})")
        break
    else:
        seen[nums[i]] = i