
user_in = input("This program returns only number missing from the list of [0, n]. Enter the list, with each distinct number separated by a space: ")

given = sorted(list(map(int, user_in.split())))

# complete = list()

# for num in range(given[-1]):
#     complete.append(num+1)

# i = 0
# found = False

# while found == False:
#     if given[i] != complete[i]:
#         print(f"The missing number is {complete[i]}. ")
#         found = True
#     else:
#         i += 1

# better method: turn the given list into a set, and then use a loop to check for every number that should be there. if you reach one that should be there but isn't, print it out and stop the code

n = len(given)
given_set = set(given)

for num in range(n+1):
    if num not in given_set:
        print(f"The missing number is {num}.\n")
        break

# genius method: find the expected sum using the sum of an AP formula. Subtract the sum from the expected sum to find the missing number