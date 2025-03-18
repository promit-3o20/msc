def myMergeSort(arr):
    if len(arr) <= 1:
       return arr
    mid = len(arr) // 2
    left = myMergeSort(arr[:mid])
    right = myMergeSort(arr[mid:])
    return my_merge(left, right)
    
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


if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
#    myMergeSort(arr)
    print("Merge sorted: ", myMergeSort(arr))
