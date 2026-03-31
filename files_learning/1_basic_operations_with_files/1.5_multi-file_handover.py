
data = open("source_data.csv", "r")
backup = open("backup_data.csv", "w")

audit = open("audit_trail.txt", "a")

audit.close()
backup.close()
data.close()