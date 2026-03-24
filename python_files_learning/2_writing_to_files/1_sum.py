
outputs = []

sum = 0


with open("numbers.txt", "r") as numbers:
    
    while True:
        temp = numbers.readline()

        if temp == "":
            break
        else:
            temp = int(temp)
            sum += temp
        
    # print(sum)

    
    # note about being Pythonic: after opening the file,
        # for line in numbers:
            # sum += int(line) works perfectly fine !

            
with open("numbers.txt", "a") as numbers:
    numbers.write(f"Total: {sum}\n")