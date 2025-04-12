import random, time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)


def my_quick_sort(arr, p, r):
    if p < r:
        q = my_partition(arr, p, r)
        my_quick_sort(arr, p, q - 1)
        my_quick_sort(arr, q + 1, r)

def my_partition(arr, p, r):
    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1

def measure_time(sort_func, input_sizes):
    times = []
    for size in input_sizes:
        data = [random.randint(1, 100) for _ in range(size)]
        start_time = time.time()
        sort_func(data, 0, len(data) - 1)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def measure_worst_time(sort_func, input_sizes):
    times = []
    for size in input_sizes:
        data = list(range(1,size))
        start_time = time.time()
        sort_func(data, 0, len(data) - 1)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def plot_time_complexity(input_sizes, times, algorithm_name, title):
    plt.plot(input_sizes, times, marker='o', label=algorithm_name)
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title(title)
    plt.grid(True)
    plt.legend()

def main():
    input_sizes = [100, 500, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 7000]
    quick_sort_times = measure_time(my_quick_sort, input_sizes)
    plot_time_complexity(input_sizes, quick_sort_times, 'Quick Sort (Random Inputs)', 'Quick Sort - Average or Best Case')

    nlogn_times = [ (size * (size).bit_length()) / 5e5 for size in input_sizes ]
    plt.plot(input_sizes, nlogn_times, linestyle='--', color='g', label='O(n log n) Reference')
    plt.legend()
    plt.show()

    quick_sort_worst_times = measure_worst_time(my_quick_sort, input_sizes)
    plot_time_complexity(input_sizes, quick_sort_worst_times, 'Quick Sort (Sorted Inputs)', 'Quick Sort - Worst Case')
    n_squared_times = [ (size**2) / 1e7 for size in input_sizes ]
    plt.plot(input_sizes, n_squared_times, linestyle='--', color='r', label='O(n^2) Reference')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
