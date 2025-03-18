class MySort:
    ''' This class containing various sorting algorithms.'''

    @staticmethod
    def myBubbleSort(arr):
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
    def myQuickSort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x >pivot]
        middle = [x for x in arr if x == pivot]
        return MySort.myQuickSort(left) + middle + MySort.myQuickSort(right)

    @staticmethod
    def myMergeSort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = MySort.myMergeSort(arr[:mid])
        right = MySort.myMergeSort(arr[mid:])
        return MySort.my_merge(left, right)
    
    @staticmethod
    def my_merge(left, right):
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
    
