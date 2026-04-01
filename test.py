def calculate_total(items):
    total = 0
    for item in items:
        total += item
        print(f"Added {item}, total is now {total}")
    return total

numbers = [10, 20, 30]
result = calculate_total(numbers)
print(f"Final Result: {result}")