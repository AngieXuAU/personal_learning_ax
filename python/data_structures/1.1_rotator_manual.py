
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_nums = []

k = int(input("This program shifts rotates the items of a list right by k times. Enter an integer k: "))

shift = k % len(nums)

for i in range(-1, -shift-1, -1):
    new_nums.append(nums[i])
new_nums.reverse()

for j in range(len(nums) - shift):
    new_nums.append(nums[j])

print(new_nums)

# more efficient to do new index = (old index + k) % length