
from collections import Counter

u1 = input("This program returns the intersection of two arrays. Enter the first list of integers, each separated by a comma and space: ")
u2 = input("Enter the second list of integers: ")

l1 = list(map(int, u1.split(", "))).sort()
l2 = list(map(int, u2.split(", "))).sort()

intersection = []

i, j = 0

while i < len(l1) and j < len(l2):
    if l1[i] == l2[j]:
        intersection.append(l1[i])
        i +=1
        j +=1
    elif l1[i] < l2[j]:
        i +=1
    else:
        j +=1

print(intersection)
    