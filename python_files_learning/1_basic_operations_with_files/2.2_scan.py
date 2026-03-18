
configuration = open("config.txt", "r")

line1 = configuration.readline()
line2 = configuration.readline()
line3 = configuration.readline()

print(line1 + line2 + line3)

configuration.close()