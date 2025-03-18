from main import sort_main

def main():
    while True:
        print("\n===== DAA Algorithm Menu =====")
        print("1. Sorting Algorithms")
        print("2. Exit")

        choice = input("\nEnter your choice (1-2): ")

        if choice == "1":
            sort_main.main()  # Call sort_main's main function
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()

