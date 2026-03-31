
data = open("data.txt", "r")

chunk = data.read(6)
print(chunk)

data.close()