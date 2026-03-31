
report = open("secret_report.txt", "r")

message = report.read()
message2 = report.read()

print(f"First: {message}\nSecond: {message2}")