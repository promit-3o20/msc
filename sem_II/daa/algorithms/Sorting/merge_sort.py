import random, time
import matplotlib.pyplot as plt

def my_merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + j + 1] 

    L[n1] = float('inf')
    R[n2] = float('inf')

    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def my_merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        my_merge_sort(A, p, q)
        my_merge_sort(A, q + 1, r)
        my_merge(A, p, q, r)


def measure_time(sort_func, input_sizes):
    times = []
    for size in input_sizes:
        data = [random.randint(1, 100) for _ in range(size)]
        start_time = time.time()
        sort_func(data, 0, len(data)-1)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def plot_time_complexity(input_sizes, times, algorithm_name):
    plt.plot(input_sizes, times, marker='o', label=algorithm_name)
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of Sorting Algorithms')
    plt.grid(True)

def main():
    input_sizes = [100, 500, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 7000]

    merge_sort_times = measure_time(my_merge_sort, input_sizes)
    plot_time_complexity(input_sizes, merge_sort_times, 'Merge Sort')

    nlogn_times = [ (size * (size).bit_length()) / 5e5 for size in input_sizes ]  
    
    plt.plot(input_sizes, nlogn_times, linestyle='--', color='g', label='O(n log n)')

    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()
