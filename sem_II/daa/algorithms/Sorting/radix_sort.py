import random, time
import matplotlib.pyplot as plt

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output

def radix_sort(arr):
    if len(arr) == 0:
        return arr

    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr

def measure_time(sort_func, input_sizes):
    times = []
    for size in input_sizes:
        data = [random.randint(1, 1000000) for _ in range(size)]
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

    radix_sort_times = measure_time(radix_sort, input_sizes)
    plot_time_complexity(input_sizes, radix_sort_times, 'Radix Sort')

    n_times = [ (size * 6) / 1e5 for size in input_sizes ]  
    plt.plot(input_sizes, n_times, linestyle='--', color='m', label='O(d·n) Reference')

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

