
user_in = input("This program removes duplicates in a list without changing its order. Enter a list of words separated by a comma and a space: ").split(", ")
# unique_set = []                     # create an empty list
# seen = set()

# # list and set method
# for word in user_in:                # loop through the words on the list
#     if word not in seen:            # check membership with an extra set
#         unique_set.append(word)     # add word if not already in set, and also add to set (faster as it is a *hash table lookup*)
#         seen.add(word)              

# dictionary method
unique_list = list(dict.fromkeys(user_in, ))

print(unique_list) 
