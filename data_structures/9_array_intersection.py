
# my method of "counter"
# from collections import defaultdict

# def mycounter(nums):
#     grouping = defaultdict(lambda: 0)

#     for num in nums:
#         grouping[num] += 1

#     return grouping

from collections import Counter

u1 = input("This program returns the intersection of two arrays. Enter the first list of integers, each separated by a comma and space: ")
u2 = input("Enter the second list of integers: ")

l1 = list(map(int, u1.split(", ")))
l2 = list(map(int, u2.split(", ")))

g1 = Counter(l1)
g2 = Counter(l2)

intersection = []

for val in g1:
    if val in g2:
        n = min(g1[val], g2[val])
        for i in range(n):
            intersection.append(val)


print(intersection)
