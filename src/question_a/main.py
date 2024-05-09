from question_a import calculate_statistics

def main():
    numbers = []
    for i in range(5):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        numbers.append(num)

    lowest, highest, total, average = calculate_statistics(numbers)

    print("Lowest number:", lowest)
    print("Highest number:", highest)
    print("Total:", total)
    print("Average:", average)

if __name__ == "__main__":
    main()
