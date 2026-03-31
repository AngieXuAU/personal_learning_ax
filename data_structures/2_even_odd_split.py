
user_in = input("This program returns a list of numbers where all the even numbers come first, followed by all the odd numbers. Enter a list of numbers each separated by a comma and then a space: ").strip()

nums = list(map(int, user_in.split(",")))

nums_even = []
nums_odd = []


for num in nums:
    if num % 2 == 0:
        nums_even.append(num)
    else:
        nums_odd.append(num)

print(nums_even + nums_odd)