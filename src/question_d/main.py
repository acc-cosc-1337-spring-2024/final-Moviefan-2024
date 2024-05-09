# main.py
from question_d import create_multiplication_table, display_multiplication_table

def main():
    while True:
        print("Multiplication Table:")
        table = create_multiplication_table()
        display_multiplication_table(table)
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
#add import