import random, time
import matplotlib.pyplot as plt

def counting_sort(arr):
    k = max(arr)
    C = [0] * (k + 1)

    for j in range(len(arr)):
        C[arr[j]] += 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    B = [0] * len(arr)
    for j in range(len(arr) - 1, -1, -1):
        B[C[arr[j]] - 1] = arr[j]
        C[arr[j]] -= 1

    return B

def measure_time(sort_func, input_sizes):
    times = []
    for size in input_sizes:
        data = [random.randint(1, 100) for _ in range(size)]
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
    input_sizes = [100, 500, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 7000]

    counting_sort_times = measure_time(counting_sort, input_sizes)
    plot_time_complexity(input_sizes, counting_sort_times, 'Counting Sort')

    n_times = [ (size) / 1e5 for size in input_sizes ]
    plt.plot(input_sizes, n_times, linestyle='--', color='r', label='O(n + k) Reference')

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

