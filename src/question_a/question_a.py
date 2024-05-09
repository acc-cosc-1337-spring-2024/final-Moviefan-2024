def calculate_statistics(numbers):
    if len(numbers) != 5:
        raise ValueError("Input should contain exactly 5 numbers")

    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return lowest, highest, total, average
