
roll = {"Alice": "A", "Bob": "B", "Charlie": "A"}

leaderboard = {}

# method 1: adding together lists
for student in roll:
    leaderboard[roll[student]] = leaderboard.get(roll[student], []) + [student]

print(leaderboard)
leaderboard.clear()

# method 2: modify the existing list using .append()
for student, grade in roll.items():
    if grade not in leaderboard:
        leaderboard[grade] = []
    leaderboard[grade].append(student)

print(leaderboard)
leaderboard.clear()


# method 3
from collections import defaultdict

leaderboard = defaultdict(list)

for student, grade in roll.items():
    leaderboard[grade].append(student)

print(leaderboard)