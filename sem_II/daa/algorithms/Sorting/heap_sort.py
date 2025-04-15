import time, random
import matplotlib.pyplot as plt

def max_heapify(arr, heap_size, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < heap_size and arr[l] > arr[largest]:
        largest = l
    if r < heap_size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, heap_size, largest)

def build_max_heap(arr):
    heap_size = len(arr)
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(arr, heap_size, i)

def my_heap_sort(arr):
   n = len(arr)
   build_max_heap(arr)
   for i in range(n - 1, 0, -1):
       arr[0], arr[i] = arr[i], arr[0]
       max_heapify(arr, i, 0)   
       
def measure_time(sort_func, input_sizes):
    times = []
    for size in input_sizes:
        data = [random.randint(1, 100) for _ in range(size)]
        start_time = time.time()
        sort_func(data)
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

    heap_sort_times = measure_time(my_heap_sort, input_sizes)
    plot_time_complexity(input_sizes, heap_sort_times, 'Heap Sort', 'Time Complexity of Sorting Algorithms')

    nlogn_times = [ (size * (size).bit_length()) / 5e5 for size in input_sizes ]  
    
    plt.plot(input_sizes, nlogn_times, linestyle='--', color='g', label='O(n log n)')

    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()
