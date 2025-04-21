import random, time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket_sort(arr):
    n = len(arr)
    if n == 0:
        return arr

    buckets = [[] for _ in range(n)]

    for value in arr:
        index = int(n * value)
        if index == n:
            index = n - 1 
        buckets[index].append(value)

    for i in range(n):
        buckets[i] = insertion_sort(buckets[i])

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

def measure_time(sort_func, input_sizes):
    times = []
    for size in input_sizes:
        data = [random.random() for _ in range(size)]
        start_time = time.time()
        sort_func(data)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def plot_time_complexity(input_sizes, times, algorithm_name):
    plt.plot(input_sizes, times, marker='o', label=algorithm_name)
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of Sorting Algorithms')
    plt.legend()
    plt.grid(True)

def main():
    input_sizes = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]

    bucket_sort_times = measure_time(bucket_sort, input_sizes)
    plot_time_complexity(input_sizes, bucket_sort_times, 'Bucket Sort')

    n_times = [ (size * 1.2) / 1e5 for size in input_sizes ] 
    plt.plot(input_sizes, n_times, linestyle='--', color='r', label='O(n) Reference')

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

