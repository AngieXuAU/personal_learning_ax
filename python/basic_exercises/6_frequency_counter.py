
frequency_dict = {

}

user_str = input("This program counts the number of time each character appears in a string. \nEnter a string: ")

for i in user_str:
    if i in frequency_dict:
        frequency_dict[i] += 1
    else:
        frequency_dict[i] = 1
    

print(frequency_dict)