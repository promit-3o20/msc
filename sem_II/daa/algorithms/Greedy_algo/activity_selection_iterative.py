def activity_selection(start, end):
    n = len(start)
    activities = sorted(zip(start, end), key=lambda x: x[1])

    print("\nSorted activities (by end time):")
    for i, (s, e) in enumerate(activities):
        print(f"Activity {i + 1}: Start = {s}, End = {e}")

    selected = []
    last_end_time = -1

    for i in range(n):
        s, e = activities[i]
        if s >= last_end_time:
            selected.append((s, e))
            last_end_time = e

    print("\nSelected activities:")
    for i, (s, e) in enumerate(selected):
        print(f"{i + 1}. Start = {s}, End = {e}")

    print(f"\nTotal non-overlapping activities selected: {len(selected)}")

def main():
    print("=== Activity Selection (Iterative Greedy) ===")
    n = int(input("Enter number of activities: "))

    start = []
    end = []

    print("Enter start and end times (space-separated):")
    for i in range(n):
        s, e = map(int, input(f"Activity {i+1}: ").split())
        start.append(s)
        end.append(e)

    activity_selection(start, end)

if __name__ == "__main__":
    main()
