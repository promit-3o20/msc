def myQuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x >pivot]
    middle = [x for x in arr if x == pivot]
    return myQuickSort(left) + middle + myQuickSort(right)


if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Quick sorted: ", myQuickSort(arr))

