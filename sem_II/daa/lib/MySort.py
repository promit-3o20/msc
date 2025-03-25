class MySort:
    ''' This class containing various sorting algorithms.'''

    @staticmethod
    def my_bubblesort(arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                    break
        return arr

    @staticmethod
    def my_quicksort(arr, low, high):
        if low < high:
            pi = MySort._my_partition(arr, low, high)
            MySort.my_quicksort(arr, low, pi-1)
            MySort.my_quicksort(arr, pi+1, high)

    @staticmethod
    def _my_partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range (low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    @staticmethod
    def my_mergesort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = MySort.my_mergesort(arr[:mid])
        right = MySort.my_mergesort(arr[mid:])
        return MySort._my_merge(left, right)
    
    @staticmethod
    def _my_merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
