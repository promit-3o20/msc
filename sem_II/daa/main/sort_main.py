from lib.MySort import MySort 

def main():
    while True:
        try:
            # Take input from user
            arr = list(map(int, input("\nEnter numbers separated by spaces: ").split()))

            # Sorting options
            sort_methods = {
                "1": ("Bubble Sort", MySort.myBubbleSort),
                "2": ("Merge Sort", MySort.myMergeSort),
                "3": ("Quick Sort", MySort.myQuickSort),
                "0": ("Exit", None)
            }

            # Display menu
            while True:
                print("\nChoose a sorting algorithm:")
                for key, (name, _) in sort_methods.items():
                    print(f"{key}. {name}")

                choice = input("\nEnter choice (0-3): ")

                if choice == "0":
                    print("Exiting program. Goodbye!")
                    return

                if choice in sort_methods and choice != "0":
                    sort_name, sort_function = sort_methods[choice]
                    sorted_arr = sort_function(arr.copy())  # Sort a copy of the array
                    print(f"\n{sort_name} Result: {sorted_arr}")
                else:
                    print("Invalid choice! Please enter a number between 0-3.")

        except ValueError:
            print("Invalid input! Please enter only numbers separated by spaces.")

if __name__ == "__main__":
    main()

