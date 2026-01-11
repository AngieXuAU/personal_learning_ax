
# feedback & notes
# - use while True: and break when you find the answer
# use the built in function sum() to make it easier
def convert_to_digits(num):
    digit_list = list()

    while num >= 10:
        x = num % 10
        num //= 10
        digit_list.append(int(x)**2)
    
    digit_list.append(int(num)**2)
    return digit_list[::-1]

def sum_digits(digits):
    sum = 0
    for num in digits:
        sum += num
    return sum

number = int(input("Enter a number determine whether it is a happy number: "))

seen = set()
happiness_determined = False

while happiness_determined == False:
    number = sum_digits(convert_to_digits(number))
    print(number)
    if number in seen:
        print("This is an unhappy number.")
        happiness_determined = True
    elif number == 1:
        print("This is a happy number!")
        happiness_determined = True
    else:
        seen.add(number)

