import random
import time
import matplotlib.pyplot as plt

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

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

    insertion_sort_times = measure_time(insertion_sort, input_sizes)
    plot_time_complexity(input_sizes, insertion_sort_times, 'Insertion Sort')

    n_squared_times = [ (size**2) / 1e7 for size in input_sizes ]  
    plt.plot(input_sizes, n_squared_times, linestyle='--', label='O(n^2)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

