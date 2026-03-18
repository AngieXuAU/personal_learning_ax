
configuration = open("config.txt", "r")

header = configuration.readline()

body = configuration.readlines()

print(header, body)

configuration.close()