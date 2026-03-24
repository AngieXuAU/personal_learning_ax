
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
<<<<<<< HEAD
    numbers.write(f"Total: {sum}\n")
=======
    numbers.write(f"Total: {sum}\n")
>>>>>>> 9707b988e2d7c3585508196b20f617648b8ee6f1
