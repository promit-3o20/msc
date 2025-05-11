def recursive_activity_selector(start, end, index, n):
    next_index = index + 1
    while next_index < n and start[next_index] < end[index]:
        next_index += 1

    if next_index < n:
        print(f"Selected Activity: Start = {start[next_index]}, End = {end[next_index]}")
        recursive_activity_selector(start, end, next_index, n)

def activity_selection_recursive(start, end):
    activities = sorted(zip(start, end), key=lambda x: x[1])
    start, end = zip(*activities)  
    n = len(start)

    print(f"Selected Activity: Start = {start[0]}, End = {end[0]}")
    recursive_activity_selector(start, end, 0, n)

def main():
    print("=== Activity Selection (Recursive) ===")
    n = int(input("Enter number of activities: "))
    start = []
    end = []

    print("Enter start and end times (space-separated):")
    for i in range(n):
        s, e = map(int, input(f"Activity {i+1}: ").split())
        start.append(s)
        end.append(e)
        
    print("Selected activities: ")
    activity_selection_recursive(start, end)

if __name__ == "__main__":
    main()
